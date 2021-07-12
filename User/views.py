from django.shortcuts import render, redirect
from .forms import LoginForm, RegisterForm

from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
# Create your views here.

def index(request):
    return render(request,"index.html")

def register(request):
    form = RegisterForm(request.POST or None)

    if form.is_valid():
        username = form.cleaned_data.get("username")
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        
        newUser = User(username=username,email=email)             
            
            
        newUser.set_password(password)  
        newUser.save()
        messages.success(request,"You're registered successfully")

        return redirect("user:login")    
                       
    return render(request,"signup.html",{"form":form})

    

def userlogin(request):
    form = LoginForm(request.POST or None)

    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        query =authenticate(username=username,password=password)

        if query is None:

            messages.info(request,"username or password is invalid!")
            return render(request,"login.html",{"form":form})
        else:
            login(request,query)
            messages.success(request,"you are login successfully")
            return redirect("home")
    return render(request,"login.html",{"form":form})



def userlogout(request):
    logout(request)
    messages.info(request,"you are logout")
    return redirect("home")