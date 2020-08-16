from django.urls import path, include
from announcements import views

urlpatterns = [
    path('compose/', views.create, name="compose"),
    path('',views.index, name="index"),
    path('send/', views.send, name="send")
]