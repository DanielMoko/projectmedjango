from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.csrf import csrf_exempt
from .models import Student,Data

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
@csrf_exempt
def addstudent1(request):
    if request.method == 'POST':
        name = request.POST.get('studname')
        email = request.POST.get('studmail')
        age = request.POST.get('studage')
        obj1 = Data(name=name, email=email, age=age)
        obj1.save()

    data = Data.objects.all()
    context = {'data': data}
    return render(request, 'login.html', context)
def editstudent1(request, id):
    data = Data.objects.get(id=id)
    context = {'data': data}
    return render(request, 'login.html', context)

