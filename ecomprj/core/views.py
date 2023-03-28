from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Product, Category, Vendor, ProductImages, CartOrder, CartOrderItems, ProductReview, WishList, Address


def index(request):
    products = Product.objects.all().order_by("-id")
    categories = Category.objects.all()
    

    context = {
        "products": products,
        "categories": categories

    }
    return render(request, 'index.html', context)


def product_list(request):
    products = Product.objects.filter(product_status="published")
    context = {
        "products": products
    }
    return render(request, 'products-list.html', context)



def category_list_view(request):
    categories = Category.objects.all()
    context = {
        "categories": categories
    }
    return render(request, "category-list.html", context)


def prod_lst_categ_view(request, cid):
    category = Category.objects.get(cid=cid)
    products = Product.objects.filter(product_status="published", category=category)
    mama = Category.objects.all()
    count = Category.objects.filter(cid=cid).count()

    context = {
        "category": category,
        "products": products,
        "categories": mama,
        'count': count
    }
    return render(request, "category-prd-lst.html", context)


def prod_detail_view(request, pid):
    # product = Product.objects.get(pid=pid)
    product = get_object_or_404(Product, pid=pid)
    p_image = product.p_images.all()

    context = {
        "prod": product,
        "p_image": p_image,
    }
    return render(request, "product-detail.html", context)