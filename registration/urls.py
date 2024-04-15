from django.urls import path
from .import views
urlpatterns = [
     path("registration/", views.registration, name="registration"),
     path("login/", views.login, name="myloginpage"),
     path("navbar/", views.navbar, name="navbar"),
     path("contact us/", views.contactus, name="contactus"),
     path("home/", views.home, name="home"),
     path("FAQs/", views.FAQs, name="FAQs"),

    ]