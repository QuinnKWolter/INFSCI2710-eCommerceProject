import csv, json
from .models import *
from django.shortcuts import render
import random
from .forms import *
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView, ListView
from django.http import (
    HttpResponse,
    HttpResponseForbidden,
    HttpResponseServerError,
    JsonResponse
)
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
from .forms import *
from .models import Product, Transaction, TransactionItem, Salesperson, Store, Region
from datetime import datetime

# Create your views here.
class index(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['zipcodes'] = ["Test1", "Test2", "Test3"]

def test_ajax(request):
    if request.method == 'POST':
        return HttpResponse("This is a simple test message from test_ajax.")
    else:
        return HttpResponseForbidden("Invalid method.")    

# Helper objects and functions for AJAX functionality
switch = {
    'test_ajax': {'call': test_ajax},
}

class login(TemplateView):
    template_name = "login.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['zipcodes'] = ["Test1", "Test2", "Test3"]


def new_user(request):
    ## disallow dupe emails and make the input fields only accept valid input
    if request.method == "POST":
        form = newUser(request.POST)

        if form.is_valid():
            temp= form.save(commit=False)
            temp.kind ="Home"
            temp.save()
            return HttpResponseRedirect("/")
    # if a GET (or any other method) we'll create a blank form
    else:
        form = newUser()

    return render(request, "new_user.html", {"form": form})

def new_company(request):
    ## disallow dupe emails and make the input fields only accept valid input
    if request.method == "POST":
        form = newCompany(request.POST)
        if form.is_valid():
            temp= form.save(commit=False)
            temp.kind ="Company"
            temp.save()
            return HttpResponseRedirect("/")
    # if a GET (or any other method) we'll create a blank form
    else:
        form = newCompany()

    return render(request, "new_user.html", {"form": form})
# Helper objects and functions for AJAX functionality
switch = {
    'test_ajax': {'call': test_ajax},
}


class product_list(ListView):
    model = Product
    
def categories(request):
    category = Category.objects.all()
    return render(request, "categories.html", {"category_list":category})


def category_products(request, category_id):
    products = Product.objects.filter(category= category_id) 
    category_name = Category.objects.get(id = category_id)
    return render(request, "category_product_list.html", {"category_name":category_name, "products_list":products})




def cart(request):
    ## add ability to edit amount in order.
    ## possible change this to transactions
    user = request.user
    if(user.is_authenticated):
        
        customer = Customer.objects.get(id = user.id)
        if request.method == "POST":
            form = cartForm(request.POST)
            if form.is_valid():

                changed_item = CartItem.objects.get(pk = form.cleaned_data["product_id"])
                changed_item.quantity = form.cleaned_data["quantity"]
                changed_item.save()
        cart_list = CartItem.objects.select_related("product").filter(customer = customer.pk)
        total = 0
        for item in cart_list:
            item.subtotal  =(item.quantity * item.product.price)
            total = total + (item.quantity * item.product.price)
        return render(request, "cart.html", {"user":user, "cart_list":cart_list, "total":total})
    else:
        return login



def empty_cart(request):
    user = request.user
    if(user.is_authenticated):
        ## it does reach here
        customer = Customer.objects.get(id = user.id)
        CartItem.objects.filter(customer = customer.pk).delete()
    return HttpResponseRedirect("/cart")

def delete_cart(request, cart_item_id):
    user = request.user
    if(user.is_authenticated):
        customer = Customer.objects.get(id = user.id)
        cart_list = CartItem.objects.filter(customer = customer.pk).filter(id = cart_item_id)
        cart_list.delete()
    return HttpResponseRedirect("/cart")



def product_page(request, product_id):
    ## add check for if user already has item in cart and let them edit
    user = request.user
    if(user.is_authenticated):
        customer = Customer.objects.get(id = user.id)
        cart = CartItem.objects.filter(customer =customer.pk).filter(product = product_id)
        default_quant = 1
        if len(cart) > 0:
            default_quant = cart[0].quantity
            my_cart = cart[0]
        if request.method == "POST":
            
            form = confirmAdd(request.POST )
            if form.is_valid():

                    
                temp_form = form.save(commit=False)
                if len(cart) > 0:
                    my_cart.quantity = temp_form.quantity
                    my_cart.save()
                    return HttpResponseRedirect("/")
                temp_form.product = Product.objects.get(id = product_id)
                temp_form.customer= customer
                
                temp_form.save()
                return HttpResponseRedirect("/")
        form = addCart(product=product_id,customer=user, initial={"quantity":default_quant})
        return render(request, "product_page.html", {"form": form, "product":Product.objects.get(id = product_id)})
    else:
        return render(request, "product_page.html", {"product":Product.objects.get(id = product_id)})


def checkout(request):
    # definitely need to add some safety checks
    user = request.user
    if(user.is_authenticated):
        customer = Customer.objects.get(id = user.id)
        checkout_cart = CartItem.objects.select_related("product").filter(customer = customer.pk)
        print(len(checkout_cart))
        if(len(checkout_cart)<= 0):
            # should probably show an error message
            return HttpResponseRedirect("/")
        for item in checkout_cart:
            if item.quantity > item.product.stock:
                # again should probably lead to an error message
                return HttpResponseRedirect("/")
            
        if request.method == 'POST':

            form = CheckoutForm(request.POST)
            if form.is_valid():
                total = 0
                for item in checkout_cart:
                    total = total + (item.quantity * item.product.price)
                new_transaction = Transaction(customer = customer, total_price = total,
                                              date_ordered = datetime.utcnow,
                                                shipping_address = form.cleaned_data['shipping_address'] ,            
                                                city = form.cleaned_data['shipping_city'],
                                                state = form.cleaned_data['shipping_state'],
                                                zipcode = form.cleaned_data['shipping_zipcode'])
                new_transaction.save()
                for item in checkout_cart:
                    product = item.product
                    new_trans_item = TransactionItem(transaction = new_transaction, product = product, quantity = item.quantity,
 )
                    product.stock = product.stock - item.quantity
                    product.save()
                    new_trans_item.save()
                CartItem.objects.filter(customer = customer.pk).delete()
                return HttpResponseRedirect("/")
        else:
            form = CheckoutForm()
        return render(request, 'checkout.html', {'form': form})
    else:
        return HttpResponseRedirect("/")

def transaction_history(request):
    customer = Customer.objects.get(id = request.user.id)
    transactions = Transaction.objects.filter(customer=customer)
    return render(request, 'transaction_history.html', {'transactions': transactions})

    
    
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
            # payment_success = process_payment(card_number, expiration_date, cvv, transaction.total_price)
            payment_success = True
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
    

