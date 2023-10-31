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
from django.db.models import Q

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

def cart(request):
    user = request.user
    if(user.is_authenticated):
        customer = Customer.objects.get(id = user.id)
        cart_list = CartItem.objects.select_related("product").filter(customer = customer.pk)
        return render(request, "cart.html", {"user":user, "cart_list":cart_list})
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
    user = request.user
    if(user.is_authenticated):
        if request.method == "POST":
            form = confirmAdd(request.POST )
            if form.is_valid():
                temp_form = form.save(commit=False)
                temp_form.product = Product.objects.get(id = product_id)
                temp_form.customer= Customer.objects.get(id = user.id)
                temp_form.save()
                return HttpResponseRedirect("/")
        form = addCart(product=product_id,customer=user, initial={"quantity":1})
        return render(request, "product_page.html", {"form": form, "product":Product.objects.get(id = product_id)})
    else:
        return render(request, "product_page.html", {"product":Product.objects.get(id = product_id)})


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
    

