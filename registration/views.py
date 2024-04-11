from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader #for routing your templets

def registration(request):
    return HttpResponse("Welcome to the registration")


def login(request):
    template = loader.get_template("login.html")
    return HttpResponse(template.render())
def navbar(request):
    template = loader.get_template("base.html")
    return HttpResponse(template.render())
def contactus(request):
    template = loader.get_template("Contact us.html")
    return HttpResponse(template.render())

def home(request):
    template = loader.get_template("home.html")
    return HttpResponse(template.render())


def FAQs(request):
    template = loader.get_template("FAQs.html")
    return HttpResponse(template.render())