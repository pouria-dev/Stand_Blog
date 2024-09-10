from django.contrib.auth.models import User
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate , login ,logout
from django.urls import  reverse
from django.contrib import  messages



def login_user(request):
    username = request.POST.get("username")

    password = request.POST.get("password")
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        messages.success(request, 'You have singed up successfully.')

        return redirect(reverse('blog:home'))



    return render(request , 'user_app/login.html' , {})


def log_out(request):
    if request.method == "POST":

        logout(request)
        return redirect(reverse('blog:home'))



