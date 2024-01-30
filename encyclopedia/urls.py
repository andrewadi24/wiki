from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("random", views.random_template, name = "random"),
    path("search/", views.search, name = "search"),
    path("create/", views.create, name = "create"),
]
