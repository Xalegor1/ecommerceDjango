from core.models import Category, Product
from django.shortcuts import render, redirect
from userauth.forms import UserRegisterForm
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.conf import settings
from userauth.models import User

from django.db.models import Min, Max, Count


def default(request):
    categories = Category.objects.all()

    min_max_price = Product.objects.aggregate(Min("price"), Max("price"))

    return {
        "categories":  categories,
        "min_max_price": min_max_price,
    }


    
