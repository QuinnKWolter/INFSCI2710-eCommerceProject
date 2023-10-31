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
from django.urls import path, include

from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index.as_view(), name='index'),
    path("accounts/", include("django.contrib.auth.urls")),
    path("accounts/new_user", views.new_user, name = 'new_user'),
    path("accounts/new_company", views.new_company, name = 'new_company'),
    path("products/", views.product_list.as_view(), name='product_list'),
    path("categories/", views.categories, name='categories'),
    path("categories/<int:category_id>", views.category_products, name='category_products'),
    path("products/<int:product_id>", views.product_page, name='product_page'),
    path("cart/", views.cart, name='cart'),
    path("empty_cart/", views.empty_cart, name='empty_cart'),
    path("delete_cart/<int:cart_item_id>", views.delete_cart, name='delete_cart'),

    # Ajax
    path('ajax/', views.ajax)
]
