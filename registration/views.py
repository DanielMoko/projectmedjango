from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader #for routing your templets

def registration(request):
    return HttpResponse("Welcome to the registration")

def mypage(request):
    template = loader.get_template("register.html")
    return HttpResponse(template.render())

def login(request):
    template = loader.get_template("login.html")
    return HttpResponse(template.render())
def navbar(request):
    template = loader.get_template("base.html")
    return HttpResponse(template.render())
def register(request):
    template = loader.get_template("register.html")
    return HttpResponse(template.render())