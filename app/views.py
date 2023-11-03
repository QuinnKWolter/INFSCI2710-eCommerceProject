import csv, json
from .models import *
import random

from django.views.generic import TemplateView
from django.http import (
    HttpResponse,
    HttpResponseForbidden,
    HttpResponseServerError,
    JsonResponse
)
from django.db.models import Q

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.core.exceptions import ValidationError
from django.db.models import Sum, Count
from .forms import RegistrationForm, SearchForm, CheckoutForm, PaymentForm, ShippingForm, UpdateInventoryForm, ReviewForm
from .models import Product, Transaction, TransactionItem, Salesperson, Store, Region

# Index View
def index(request):
    return render(request, 'index.html')

# Registration View
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})

# Login View
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            # Optionally, add an error message
            pass
    return render(request, 'login.html')

# Logout View
def logout_view(request):
    logout(request)
    return redirect('login')

# Profile View
@login_required
def profile(request):
    return render(request, 'profile.html', {'user': request.user})

# Product Browsing and Searching
def product_list(request):
    products = Product.objects.all()
    paginator = Paginator(products, 10)  # Show 10 products per page

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'product_list.html', {'page_obj': page_obj})

def product_detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(request, 'product_detail.html', {'product': product})

def search(request):
    query = request.GET.get('q')
    products = Product.objects.filter(name__icontains=query)
    return render(request, 'search_results.html', {'products': products})

def cart(request):
    # Assumes cart info is stored in session. Adjust as needed.
    cart = request.session.get('cart', {})

    # Fetch all products in the cart at once
    product_ids = list(cart.keys())
    products = Product.objects.filter(id__in=product_ids)

    # Create a list of tuples (product, quantity) for the template
    cart_items = [(product, cart[str(product.id)]) for product in products]

    return render(request, 'cart.html', {'cart_items': cart_items})

def add_to_cart(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    cart = request.session.get('cart', {})
    cart[str(product_id)] = cart.get(str(product_id), 0) + 1
    request.session['cart'] = cart
    request.session.modified = True
    return redirect('cart')

def remove_from_cart(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    cart = request.session.get('cart', {})
    product_id_str = str(product_id)
    if product_id_str in cart:
        del cart[product_id_str]
        request.session['cart'] = cart
        request.session.modified = True
    return redirect('cart')

def checkout(request):
    if request.method == 'POST':
        form = CheckoutForm(request.POST)
        if form.is_valid():
            # Process checkout
            pass  # Replace with your checkout processing code
    else:
        form = CheckoutForm()
    return render(request, 'checkout.html', {'form': form})

def transaction_history(request):
    transactions = Transaction.objects.filter(customer=request.user.customer)
    return render(request, 'transaction_history.html', {'transactions': transactions})

# Payment and Shipping
@login_required
def payment(request):
    user = request.user
    try:
        transaction = Transaction.objects.get(customer__user=user, status='Pending')  # Assuming each user has one pending transaction at a time
    except Transaction.DoesNotExist:
        # Handle the case where no transaction exists
        return redirect('cart')  # Redirect to cart if no pending transaction

    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            card_number = form.cleaned_data['card_number']
            expiration_date = form.cleaned_data['expiration_date']
            cvv = form.cleaned_data['cvv']
            
            # Assume a function process_payment which contacts a payment gateway and returns a boolean indicating success
            payment_success = process_payment(card_number, expiration_date, cvv, transaction.total_price)
            
            if payment_success:
                transaction.status = 'Processing'  # Change to 'Processing' upon successful payment
                transaction.save()
                return redirect('checkout')  # Redirect to checkout on successful payment
            else:
                form.add_error(None, 'Payment processing failed. Please try again.')  # Add a non-field error to the form
    else:
        form = PaymentForm()

    return render(request, 'payment.html', {'form': form})

@login_required
def shipping(request):
    try:
        # Assuming there's a transaction in progress for the logged-in user
        transaction = Transaction.objects.filter(customer=request.user.customer, status='Pending').latest('date')
    except Transaction.DoesNotExist:
        # Handle the case where there is no transaction in progress
        return redirect('cart')  # Or wherever you want to redirect

    if request.method == 'POST':
        form = ShippingForm(request.POST)
        if form.is_valid():
            # Save shipping information to the transaction
            transaction.shipping_address = form.cleaned_data['shipping_address']
            transaction.city = form.cleaned_data['city']
            transaction.state = form.cleaned_data['state']
            transaction.zip_code = form.cleaned_data['zip_code']
            transaction.save()  # Save the updated transaction object

            # Optionally update the order status
            transaction.status = 'Processing'
            transaction.save()

            return redirect('checkout')
    else:
        # Pre-fill the form with existing shipping info if available
        form = ShippingForm(initial={
            'shipping_address': transaction.shipping_address,
            'city': transaction.city,
            'state': transaction.state,
            'zip_code': transaction.zip_code,
        })

    return render(request, 'shipping.html', {'form': form})

# Salesperson Interface
@login_required
def sales_dashboard(request):
    try:
        # Assuming the logged in user has an associated Salesperson record
        salesperson = Salesperson.objects.get(email=request.user.email)
    except Salesperson.DoesNotExist:
        # Handle the case where the salesperson does not exist
        # This might redirect to a different page or show an error message
        return render(request, 'error.html', {'error_message': 'Salesperson not found'})

    # Fetch transactions associated with the salesperson
    transactions = Transaction.objects.filter(salesperson=salesperson)

    # Calculate total sales for the dashboard
    total_sales = sum(transaction.total_price for transaction in transactions if transaction.total_price)

    context = {
        'salesperson': salesperson,
        'transactions': transactions,
        'total_sales': total_sales,
    }

    return render(request, 'sales_dashboard.html', context)

# Store and Inventory Management
@login_required
def inventory(request):
    products = Product.objects.all()
    return render(request, 'inventory.html', {'products': products})

@login_required
def update_inventory(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = UpdateInventoryForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('inventory')
    else:
        form = UpdateInventoryForm(instance=product)
    return render(request, 'update_inventory.html', {'form': form})

# Review
def review(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.product = product
            review.save()
            return redirect('product_detail', product_id=product.id)
    else:
        form = ReviewForm()
    return render(request, 'review.html', {'form': form, 'product': product})

# Check if user is an admin
def admin_check(user):
    return user.is_staff

# Data Aggregation and Reporting
@login_required
@user_passes_test(admin_check)
def sales_report(request):
    total_sales = Transaction.objects.aggregate(Sum('total_price'))['total_price__sum']
    return render(request, 'report_sales.html', {'total_sales': total_sales})

@login_required
@user_passes_test(admin_check)
def product_report(request):
    product_sales = Product.objects.annotate(sold=Sum('transaction_items__quantity'))
    return render(request, 'report_product.html', {'product_sales': product_sales})

@login_required
@user_passes_test(admin_check)
def region_report(request):
    region_sales = Region.objects.annotate(sales=Sum('stores__salespersons__transactions__total_price'))
    return render(request, 'report_region.html', {'region_sales': region_sales})

# Administrative Interface
@login_required
@user_passes_test(admin_check)
def admin_dashboard(request):
    # Assuming some basic stats for the dashboard
    total_sales = Transaction.objects.aggregate(Sum('total_price'))['total_price__sum']
    total_products = Product.objects.count()
    total_users = User.objects.count()
    return render(request, 'admin/admin_dashboard.html', {
        'total_sales': total_sales,
        'total_products': total_products,
        'total_users': total_users,
    })

@login_required
@user_passes_test(admin_check)
def manage_users(request):
    users = User.objects.all()
    return render(request, 'admin/manage_users.html', {'users': users})

@login_required
@user_passes_test(admin_check)
def manage_products(request):
    products = Product.objects.all()
    return render(request, 'admin/manage_products.html', {'products': products})

def test_ajax(request):
    if request.method == 'POST':
        return HttpResponse("This is a simple test message from test_ajax.")
    else:
        return HttpResponseForbidden("Invalid method.")    

# Helper objects and functions for AJAX functionality
switch = {
    'test_ajax': {'call': test_ajax},
}

def ajax(request):
    """Switch to correct function given POST call

    Receives the following from POST:
    call -- What function to redirect to
    """
    post_call = request.POST.get('call', '')

    # Abort if there is no valid call sent to us from Javascript
    if not post_call:
        return HttpResponseServerError()

    # Route the request to the correct handler function
    # and pass request to the functions
    try:
        # select the function from the dictionary
        selection = switch[post_call]
    # If all else fails, handle the error message
    except KeyError:
        return HttpResponseServerError()

    else:
        procedure = selection.get('call')
        validation = selection.get('validation', None)
        if validation:
            valid = validation(request)

            if not valid:
                return HttpResponseForbidden()

        # execute the function
        return procedure(request)
    

