from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.contrib.auth.models import User

# Category Model
class Category(models.Model):
    ## Augment and use pk instead
    unique_id = models.IntegerField(null = True)
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

# Product Model
class Product(models.Model):
    asin = models.CharField(max_length=10, null=True, blank=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    # stock = models.IntegerField(default=10)
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product_images/', blank=True, null=True)

    def __str__(self):
        return self.name

# Salesperson Model
class Salesperson(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=300)
    email = models.EmailField()
    job_title = models.CharField(max_length=100, choices=[('Manager', 'Manager'), ('Associate', 'Associate')])
    store_assigned = models.ForeignKey('Store', related_name='salespersons', on_delete=models.SET_NULL, null=True)
    salary = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

# Store Model
class Store(models.Model):
    address = models.CharField(max_length=300)
    manager = models.CharField(max_length=200)
    region = models.ForeignKey('Region', related_name='stores', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.address

# Region Model
class Region(models.Model):
    name = models.CharField(max_length=200)
    region_manager = models.CharField(max_length=200)

    def __str__(self):
        return self.name

# Customer Model
class Customer(User):
    name = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=15)
    # phone number middle should be 555 
    street_address = models.CharField(max_length=300)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=10)
    kind = models.CharField(max_length=10, choices=[('Home', 'Home'), ('Business', 'Business')])
    # Fields for 'Home'
    ## should probably change marital_status and gender to choices
    marital_status = models.CharField(max_length=10, blank=True, null=True)
    gender = models.CharField(max_length=10, blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    # age is not good, we should try for dob instead
    # Fields for 'Business' kind users
    business_category = models.CharField(max_length=100, blank=True, null=True)
    annual_income = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return self.name

# Transaction Model
class Transaction(models.Model):
    STATUS_CHOICES = (
        ('Pending', 'Pending'),
        ('Processing', 'Processing'),
        ('Shipped', 'Shipped'),
        ('Delivered', 'Delivered'),
    )
    
    # Linking to Customer and Salesperson models
    customer = models.ForeignKey(Customer, related_name='transactions', on_delete=models.CASCADE)
    salesperson = models.ForeignKey(Salesperson, related_name='transactions', on_delete=models.SET_NULL, null=True)
    date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Pending')
    total_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    shipping_address = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zipcode = models.IntegerField()

    def __str__(self):
        return f'Transaction {self.id} - {self.status}'

# OrderItem Model
class TransactionItem(models.Model):
    transaction = models.ForeignKey(Transaction, related_name='transaction', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='order_items', on_delete=models.CASCADE)
    quantity = models.IntegerField()

    def __str__(self):
        return f'{self.product.name} ({self.quantity})'

# Inventory Model
class Inventory(models.Model):
    store = models.ForeignKey(Store, related_name='inventory_items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='inventory_items', on_delete=models.CASCADE)
    quantity = models.IntegerField()

    class Meta:
        unique_together = ('store', 'product')  # Ensure that each product is unique per store

    def __str__(self):
        return f'{self.product.name} ({self.quantity}) in {self.store}'

# Review Model
class Review(models.Model):
    customer = models.ForeignKey(Customer, related_name='reviews', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='reviews', on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])

# CartItem Model
class CartItem(models.Model):
    customer = models.ForeignKey(Customer, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='cart_items', on_delete=models.CASCADE)
    quantity = models.IntegerField()

    def __str__(self):
        return f'Review by {self.customer} for {self.product}'