from core.models import Category
from django.shortcuts import render, redirect
from userauth.forms import UserRegisterForm
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.conf import settings
from userauth.models import User

def default(request):
    categories = Category.objects.all()
    return {
        "categories":  categories
    }


    
