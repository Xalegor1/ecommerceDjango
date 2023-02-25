from django.shortcuts import render
from django.http import HttpResponse
from .models import Product, Category, Vendor, ProductImages, CartOrder, CartOrderItems, ProductReview, WishList, Address


def index(request):
    products = Product.objects.all().order_by("-id")

    context = {
        "products": products
    }
    return render(request, 'index.html', context)


def product_list(request):
    products = Product.objects.filter(product_status="published")
    context = {
        "products": products
    }
    return render(request, 'products-list.html', context)