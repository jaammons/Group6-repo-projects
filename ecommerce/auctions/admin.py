from django.contrib import admin
from .models import AuctionListing, AuctionComment, AuctionBid

# Register your models here.
admin.site.register(AuctionListing)
admin.site.register(AuctionComment)
admin.site.register(AuctionBid)