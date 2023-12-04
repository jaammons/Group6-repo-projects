from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.urls import reverse
from django.core.exceptions import ObjectDoesNotExist
from django.core.serializers import serialize
from django import forms
from datetime import datetime
from .models import *
from users.models import User
from selenium import webdriver
import json
import os


def index(request):
    auctions = AuctionListing.objects.all()
    watchlist = []
    for auction in auctions:
        if auction.watchlist.filter(username=request.user).exists():
            watchlist.append(auction.auction_id)

    return render(request, "auctions/index.html", {"auctions": auctions, "watchlist": watchlist})
    
def listing(request, id):
    # Get listing information from DB
    comments = AuctionComment.objects.filter(auction=id)
    auction = AuctionListing.objects.filter(pk=id).first()
    bid = AuctionBid.objects.filter(auction=id).order_by("-bid")

    # If a bid has been placed on the auction, get the highest bid.     
    if len(bid) > 0:
        bid = bid[0]

    # If a valid auction was found, using listing template to create auction listing.
    if auction is not None:
        watchlist = auction.watchlist.all()
        return render(request, "auctions/listing.html", {"auction": auction, "watchlist": watchlist, "comments": comments, "bid": bid})
    else:
        return render(request, "auctions/listing.html")

def update_watchlist(request, id):
    if request.method == "POST":
        # Get auction from DB and update user watchlist status
        auction = AuctionListing.objects.filter(pk=id).first()
        if request.POST["watchlist"] == "add":
            auction.watchlist.add(request.user)
        else:
            auction.watchlist.remove(request.user)
        return HttpResponseRedirect(reverse("listing", args=(id, )))
    return render(request, "auctions/index.html") 

def bid(request, id):
    if request.method == "POST":
        auction = AuctionListing.objects.filter(pk=id).first()
        # Check if bid is a valid amount and then update DB
        if float(request.POST["bid"]) > auction.bid:
            auction.bid = request.POST["bid"]
            auction.save()
            new_bid = AuctionBid()
            new_bid.username  = request.user
            new_bid.auction = AuctionListing.objects.get(auction_id=id)
            new_bid.bid = request.POST["bid"]
            new_bid.save()

            return HttpResponseRedirect(reverse("listing", args=(id, )))
        else:
            return HttpResponseRedirect(reverse("listing", args=(id, )))
    return render(request, "auctions/index.html") 
    

def watchlist(request):
    # Get all items user has watchlisted
    auctions = request.user.user_watchlist.all()
    return render(request, "auctions/watchlist.html", {"auctions":auctions})


def category(request, category_name):
    # Get category value from dropdown menu
    if request.method == "POST":
        category_name = request.POST['category']
    
    # Get auction list for category
    auctions = list(AuctionListing.objects.filter(category=category_name))
    
    # Display auctions if any exist
    if len(auctions) > 0:
        return render(request, "auctions/category.html", {"auctions": auctions, "category_name": category_name})
    else:
        return render(request, "auctions/category.html", {"category_name": category_name})
    
def add_listing(request):
    if request.method == "POST":
        # Process listing after form entry and add to DB
        form = CreateAuction(request.POST, request.FILES)
        if form.is_valid():
            auction = AuctionListing()
            auction.username  = request.user
            auction.item_name = form.cleaned_data['item_name']
            auction.item_desc = form.cleaned_data['item_desc']
            auction.item_image = form.cleaned_data['item_image']
            auction.date_ends = form.cleaned_data['date_ends']
            auction.category = form.cleaned_data['category']
            auction.bid = form.cleaned_data['bid']
            auction.save()
            return render(request, "auctions/add_listing.html", {"message": "Auction Created.", "form": CreateAuction()})
    return render(request, "auctions/add_listing.html", {"form": CreateAuction()})  

def add_comment(request, id):
    # Add comment to current auction listing
    if request.method == "POST":
        new_comment = AuctionComment()
        new_comment.username  = request.user
        new_comment.auction = AuctionListing.objects.get(auction_id=id)
        new_comment.comment = request.POST["comment"]
        new_comment.save()
    return HttpResponseRedirect(reverse("listing", args=(id, )))

def close_auction(request, id):
    # Set current auction to closed
    if request.method == 'POST':
        auction = AuctionListing.objects.get(auction_id=id)
        auction.status = False
        auction.save()
    return HttpResponseRedirect(reverse("listing", args=(id, )))

# Class to create a Django form to add auctions
class CreateAuction(forms.Form):
    item_name = forms.CharField(label="Item Name")
    item_desc = forms.CharField(widget=forms.Textarea(attrs={'rows': 4, 'cols': 50, 'label':'Description'}))
    item_image = forms.ImageField(label="Image")
    date_ends = forms.DateField(label="Date Ends")
    category = forms.CharField(label="Category")
    bid = forms.FloatField(label="Starting Bid Amount")

def test_result(request):
    current_directory = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.abspath(os.path.join(current_directory, '..'))
    with open(file_path + "/test_log") as log_json:
        log = json.load(log_json)

    return render(request, "auctions/test_result.html", {"tests":log, "path":file_path})

def get(request):
    pk=request.GET.get("pk")
    data = {}
    if pk == None:
        data["Error":"Invalid/Missing argument."]
        return JsonResponse(data)

    if pk == "all":
        data["models"] = serialize('json', AuctionListing.objects.all())[1:-1]
    elif pk.isdigit():
        auction = serialize('json', AuctionListing.objects.filter(pk=pk))[1:-1]
        data = json.loads(auction)
    else:
        data["models"] = serialize('json', AuctionListing.objects.filter(category=pk.capitalize()))[1:-1]
        
    return JsonResponse(data)

def bids(request):
    auction = request.GET.get("auction")
    username = request.GET.get("username")
    response = ""
    try:
        bid = float(request.GET.get("bid"))
    except:
        response = {"Error":"Invalid bid amount, must be a positive number at least 1 more than previous bid."}
        json_data = json.dumps(response)
        return JsonResponse(json_data, safe=False)

    if not User.objects.filter(username=username).exists():
        response = {"Error":"Invalid username."}
        json_data = json.dumps(response)
        return JsonResponse(json_data, safe=False)

    auction_item = AuctionListing.objects.filter(pk=auction)[0]
    if auction_item:
        if auction_item.bid >= bid - 1:
            response = {"Error":"Bid too low."}
        else:
            auction_item.bid = bid
            auction_item.save()
            new_bid = AuctionBid()
            new_bid.username  = User.objects.get(username=username)
            new_bid.auction = AuctionListing.objects.get(auction_id=auction)
            new_bid.bid = bid
            new_bid.save()
    else:
        response = {"Error":"Auction does not exist."}
    json_data = json.dumps(response)
    return JsonResponse(json_data, safe=False)

def reset_bid(request):
    # Deletes most recent bid on test auction
    bid = AuctionBid.objects.filter(auction=1).order_by("-bid")[0]
    bid.delete()

    auction = AuctionListing.objects.filter(pk=1)[0]
    auction.bid = 40
    
    response = {"Success":"True"}
    json_data = json.dumps(response)
    return JsonResponse(json_data, safe=False)

def welcome(request):
    return HttpResponse("Welcome to Our Ecommerce Site!")