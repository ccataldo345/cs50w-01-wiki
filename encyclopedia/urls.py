from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("new", views.new, name="new"),
    path("edit", views.edit, name="edit"),
    path("wiki/<str:title>", views.title, name="title"),
    path("random_page", views.rnd_title, name="rnd_title"),
    path("search", views.search, name="search")
]
