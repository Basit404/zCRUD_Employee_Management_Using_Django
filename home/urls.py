from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("", views.home, name = "home"),
    path("home/", views.home, name = "home"),
    path("add/", views.add, name = "add"),
    path("edit/", views.edit, name = "edit"),
    path("update/<str:id>", views.update, name = "update"),
    path("delete/<str:id>", views.delete, name = "delete"),
]