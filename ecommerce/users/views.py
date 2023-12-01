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

# Create your views here.
def login_view(request):
    if request.user.is_authenticated:
        return render(request, "auctions/index.html")

    if request.method == "POST":
        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            print("testsetestes")
            if not "remember_me" in request.POST:
                print("testkjestheskjhkej3849832843yu2")
                request.session.set_expiry(0)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "users/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "users/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "users/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password, is_staff=False)
            user.save()
        except IntegrityError:
            return render(request, "users/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "users/register.html")
    
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