from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('dialogflow/', views.webhook),
    path('home/', views.home),

]
