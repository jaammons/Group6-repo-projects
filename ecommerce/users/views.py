from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.urls import reverse
from django.core.exceptions import ObjectDoesNotExist
from django import forms
from datetime import datetime
from .models import *
import json
from .forms import *


def login_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse("index"))
 
    if request.method == "POST":
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data["username"]
            password = login_form.cleaned_data["password"]
            remember_me = login_form.cleaned_data["remember_me"]
        else:
            return render(request, "users/login.html", {"form":LoginForm()})

        user =  authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if not remember_me:
                request.session.set_expiry(0)
            return HttpResponseRedirect(reverse("index"))
        else:    
            return render(request, "users/login.html", {"form":LoginForm(), 
                          "message": "Invalid username and/or password."})

    return render(request, "users/login.html", {"form":LoginForm()})

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))

def register(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse("index"))
    
    # Check for form data
    if request.method=="POST":  
            
        # Read data into contact info and physical attributes
        form = RegistrationForm(request.POST) 
        print("test")
        
        if form.is_valid():
            username = form.cleaned_data["username"]
            email = form.cleaned_data["email"]

            # Ensure password matches confirmation
            password = form.cleaned_data["password"]
            confirmation = form.cleaned_data["confirmation"]
            # Attempt to create new user
            try:
                user = User.objects.create_user(username, email, password, is_staff=False)
                user.save()
                
                login(request, user)
                return HttpResponseRedirect(reverse("index"))
            except IntegrityError:
                return render(request, "users/register.html", {
                    "message": "Username already taken."
                })
          
    
    return render(request, "users/register.html")

# def register(request):
#     if request.method == "POST":
#         username = request.POST["username"]
#         email = request.POST["email"]

#         # Ensure password matches confirmation
#         password = request.POST["password"]
#         confirmation = request.POST["confirmation"]
#         if password != confirmation:
#             return render(request, "users/register.html", {
#                 "message": "Passwords must match."
#             })

#         # Attempt to create new user
#         try:
#             user = User.objects.create_user(username, email, password, is_staff=False)
#             user.save()
#         except IntegrityError:
#             return render(request, "users/register.html", {
#                 "message": "Username already taken."
#             })
#         login(request, user)
#         return HttpResponseRedirect(reverse("index"))
#     else:
#         return render(request, "users/register.html")
    
def delete_user(request):
    username = request.GET.get("username")
    if username == "RegistrationTest":
        User.objects.filter(username=username).delete()
        response = {"Success":"True"}
        json_data = json.dumps(response)
        return JsonResponse(json_data, safe=False)
    else:
        response = {"Success":"False"}
        json_data = json.dumps(response)
        return JsonResponse(json_data, safe=False)
    