from django.urls import path
from authapp import models
from authapp import views

urlpatterns = [
    path('signup/', views.signup, name="signup"),
    path('login/', views.login_view, name="login"),
]