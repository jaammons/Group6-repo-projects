# Generated by Django 4.2.5 on 2023-10-29 02:41

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="AuctionListing",
            fields=[
                ("auction_id", models.AutoField(primary_key=True, serialize=False)),
                ("item_name", models.CharField(max_length=32)),
                ("item_desc", models.TextField()),
                ("item_image", models.ImageField(upload_to="")),
                ("date_created", models.DateField(auto_now_add=True)),
                (
                    "date_ends",
                    models.DateField(
                        default=datetime.datetime(2023, 11, 4, 22, 41, 59, 256882)
                    ),
                ),
                ("category", models.CharField(max_length=32)),
                ("bid", models.FloatField()),
                ("status", models.BooleanField(default=True)),
                (
                    "username",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="user_listing",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "watchlist",
                    models.ManyToManyField(
                        blank=True,
                        related_name="user_watchlist",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="AuctionComment",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("comment", models.TextField()),
                (
                    "auction",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="id_num",
                        to="auctions.auctionlisting",
                    ),
                ),
                (
                    "username",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="user_comment",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="AuctionBid",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("bid", models.FloatField()),
                (
                    "auction",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="auction_num",
                        to="auctions.auctionlisting",
                    ),
                ),
                (
                    "username",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="user_bid",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]