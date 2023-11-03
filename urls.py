"""app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from app import views

urlpatterns = [
    # Site Home
    path('', views.index, name='index'),
    
    # Ajax
    path('ajax/', views.ajax),

    # User Authentication
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),

    # User Profile
    path('profile/', views.profile, name='profile'),

    # Product Browsing and Searching
    path('products/', views.product_list, name='product_list'),
    path('products/<int:product_id>/', views.product_detail, name='product_detail'),
    path('search/', views.search, name='search'),

    # Transaction and Cart
    path('cart/', views.cart, name='cart'),
    path('cart/add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/remove/<int:product_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('transaction/history/', views.transaction_history, name='transaction_history'),

    # Payment and Shipping
    path('payment/', views.payment, name='payment'),
    path('shipping/', views.shipping, name='shipping'),

    # Salesperson Interface
    path('sales/dashboard/', views.sales_dashboard, name='sales_dashboard'),

    # Store and Inventory Management
    path('inventory/', views.inventory, name='inventory'),
    path('inventory/update/<int:product_id>/', views.update_inventory, name='update_inventory'),

    # Review
    path('review/<int:product_id>/', views.review, name='review'),

    # Data Aggregation and Reporting
    path('reports/sales/', views.sales_report, name='sales_report'),
    path('reports/products/', views.product_report, name='product_report'),
    path('reports/regions/', views.region_report, name='region_report'),

    # Administrative Interface
    path('admin/', admin.site.urls, name='admin'),
    path('admin/dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('admin/users/', views.manage_users, name='manage_users'),
    path('admin/products/', views.manage_products, name='manage_products'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
