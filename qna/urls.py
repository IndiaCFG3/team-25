from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('dialogflow', views.webhook),
    path('dialogflow/', views.webhook),
    path('twilio/', views.twilio),
    path('home/', views.home),

]
