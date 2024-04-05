from django.urls import path
from .import views
urlpatterns = [
     path("registration", views.registration, name="registration"),
     path("login", views.login, name="myloginpage"),
     path("navbar/", views.navbar, name="navbar"),
     path("register/", views.register, name="register")
]