from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path("", views.index, name='index'),
    path("contact", views.contact, name='contact'),
    path("aboutranchi", views.aboutranchi, name='aboutranchi'),
    path("waterfalls", views.waterfalls, name='waterfalls'),
    path("valley", views.valley, name='valley'),

]