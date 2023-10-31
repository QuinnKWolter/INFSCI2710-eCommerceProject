from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import *


class newUser(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text='Required')
    kind = "Home"
    class Meta:
        model = Customer
        fields = ('username', 'email',"name","phone_number","street_address","city","state","zip_code","marital_status","gender","age", 'password1', 'password2')
class newCompany(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text='Required')
    class Meta:
        model = Customer
        fields = ('username', 'email',"name","phone_number","street_address","city","state","zip_code","business_category","annual_income", 'password1', 'password2')
        
class addCart(forms.ModelForm):
    def __init__(self, product, customer, *args, **kwargs):
        self.customer = customer
        self.product = product
        super(addCart,self).__init__(*args, **kwargs)
        self.fields["quantity"] = forms.IntegerField(min_value=1,max_value=Product.objects.get(id = product).stock)
    class Meta:
        model = CartItem
        fields = ("quantity",)

        
class confirmAdd(forms.ModelForm):
    class Meta:
        model = CartItem
        fields = ("quantity",)