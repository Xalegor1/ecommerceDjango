from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.conf import settings
from userauth.models import User

# User = settings.AUTH_USER_MODEL


def regiser_view(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST or None) 
        if form.is_valid():
            new_user = form.save()
            username = form.cleaned_data.get("username")
            messages.success(request, f"Hey {username}, Your account was created successfully.")
            new_user = authenticate(username=form.cleaned_data['email'], password=form.cleaned_data['password1'])
            login(request, new_user)
            return redirect('index')
    else:
        form = UserRegisterForm() 
        print('Hello')
    
    context = {
        "form": form
    }
    return render(request, 'register.html', context)


def loginUser(request):
    if request.user.is_authenticated:
        return redirect("index")
    if request.method == 'POST':
        email = request.POST.get("email")
        password = request.POST.get('password')        

        try:
            user = User.objects.get(email=email)
            user = authenticate(request, email=email, password=password) 
            if user is not None:
                login(request, user)
                messages.success(request, "Вы вошли в систему!")
                return redirect("index")
            else:
                messages.warning(request, 'Пользователя не существует, создайте аккаунт!')  
        except:
            messages.warning(request, f"Пользователь c {email} не существует!")

           
    
    context = {
        
    }
    
    return render(request, 'login.html', context)          


def logoutUser(request):
    logout(request)
    messages.success(request, 'Вы вышли из аккаунта')
    return redirect("login")
