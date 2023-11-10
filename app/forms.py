from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *
from django.forms import HiddenInput, formset_factory

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

class cartForm(forms.Form):
    quantity = forms.IntegerField()
    product_id = forms.IntegerField()

class CheckoutForm(forms.Form):
    full_name = forms.CharField(
        label='Full Name',
        max_length=255,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    email = forms.EmailField(
        label='Email',
        widget=forms.EmailInput(attrs={'class': 'form-control'})
    )
    phone_number = forms.CharField(
        label='Phone Number',
        max_length=15,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    street_address = forms.CharField(
        label='Street Address',
        max_length=300,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    city = forms.CharField(
        label='City',
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    state = forms.CharField(
        label='State',
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    zip_code = forms.CharField(
        label='Zip Code',
        max_length=10,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    payment_method = forms.ChoiceField(
        label='Payment Method',
        choices=[('Credit Card', 'Credit Card'), ('PayPal', 'PayPal')],
        widget=forms.RadioSelect(attrs={'class': 'form-check-input'})
    )
    card_number = forms.CharField(
        label='Card Number',
        max_length=16,
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    expiration_date = forms.CharField(
        label='Expiration Date',
        max_length=5,
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'MM/YY'})
    )
    cvv = forms.CharField(
        label='CVV',
        max_length=3,
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    shipping_address = forms.CharField(
        label = "Shipping Address",
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    shipping_city = forms.CharField(
        label='Shipping City',
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    shipping_state = forms.CharField(
        label='Shipping State',
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    shipping_zipcode = forms.CharField(
        label='Shipping Zip Code',
        max_length=10,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )


class PaymentForm(forms.Form):
    card_number = forms.CharField(max_length=16, widget=forms.TextInput(attrs={'class': 'form-control'}))
    expiration_date = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control'}))
    cvv = forms.CharField(max_length=3, widget=forms.TextInput(attrs={'class': 'form-control'}))

class ShippingForm(forms.Form):
    shipping_address = forms.CharField(label='Shipping Address', max_length=300, widget=forms.TextInput(attrs={'class': 'form-control'}))
    city = forms.CharField(label='City', max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    state = forms.CharField(label='State', max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    zip_code = forms.CharField(label='Zip Code', max_length=10, widget=forms.TextInput(attrs={'class': 'form-control'}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['shipping_address'].widget.attrs.update({'placeholder': '1234 Main St'})
        self.fields['city'].widget.attrs.update({'placeholder': 'Springfield'})
        self.fields['state'].widget.attrs.update({'placeholder': 'IL'})
        self.fields['zip_code'].widget.attrs.update({'placeholder': '62704'})

class UpdateInventoryForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['stock']

    stock = forms.IntegerField(min_value=0, required=True, label='Inventory Amount')

    def clean_stock(self):
        stock = self.cleaned_data.get('stock')
        if stock < 0:
            raise forms.ValidationError("Inventory amount cannot be negative.")
        return stock
    
class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['rating']

    rating = forms.IntegerField(min_value=1, max_value=5, required=True, label='Rating')

    def clean_rating(self):
        rating = self.cleaned_data.get('rating')
        if rating < 1 or rating > 5:
            raise forms.ValidationError("Rating must be between 1 and 5.")
        return rating

class SearchForm(forms.Form):
    q = forms.CharField(
        label='Search',
        max_length=255,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Search products...'})
    )