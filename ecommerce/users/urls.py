from django.urls import path
from . import views

urlpatterns = [
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("delete_user", views.delete_user, name="delete_user"),
    path("register_user", views.register_user, name="register_user"),
    path("get_cookie", views.get_cookie, name="get_cookie")
]