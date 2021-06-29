from django.contrib import admin
from . import views
from django.urls import path

urlpatterns = [
    path("", views.index , name="shophome"),
    path("about/", views.about, name="AboutUs"),
    path("contact/", views.contact, name="ContactUs"),
    path("products/<int:id>", views.productView, name="ProductView"),
    path("buy/<int:id>", views.buy, name="buy"),
    path("search/", views.search, name="search"),
    path("signup", views.signup, name="signup"),
    path("view_login", views.view_login, name="view_login"),
    path("view_logout", views.view_logout, name="view_logout"),
    path("orders", views.orderview, name="orders"),

]
