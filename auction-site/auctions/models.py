from django.contrib.auth.models import AbstractUser
from django.db import models
from datetime import datetime, timedelta

class User(AbstractUser):
    pass

class AuctionListing(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_listing")
    auction_id = models.AutoField(primary_key=True)
    item_name = models.CharField(max_length=32)
    item_desc = models.TextField()
    item_image = models.ImageField()
    date_created = models.DateField(auto_now_add=True)
    date_ends = models.DateField(default=(datetime.now() + timedelta(days=7)))
    category = models.CharField(max_length=32)
    bid = models.FloatField()
    watchlist = models.ManyToManyField(User, blank=True, related_name="user_watchlist")
    status = models.BooleanField(default=True)


class AuctionBid(models.Model):
    username  = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_bid")
    auction = models.ForeignKey(AuctionListing, on_delete=models.CASCADE, related_name="auction_num")
    bid = models.FloatField()

class AuctionComment(models.Model):
    username  = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_comment")
    auction = models.ForeignKey(AuctionListing, on_delete=models.CASCADE, related_name="id_num")
    comment = models.TextField()