from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("index", views.index, name="index"),
    path("listing/<int:id>", views.listing, name="listing"),
    path("category/<str:category_name>", views.category, name="category"),
    path("add_listing", views.add_listing, name="add_listing"),
    path("watchlist", views.watchlist, name="watchlist"),
    path("update_watchlist/<int:id>", views.update_watchlist, name="update_watchlist"),
    path("bid/<int:id>", views.bid, name="bid"),
    path("add_comment/<int:id>", views.add_comment, name="add_comment"),
    path("close_auction/<int:id>", views.close_auction, name="close_auction"),
    path("test_result", views.test_result, name="test_result"),
    path("reset_bid", views.reset_bid, name="reset_bid"),
    path("get", views.get, name="get"),
    path("bids", views.bids, name="bids")
]