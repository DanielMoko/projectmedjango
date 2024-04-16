from django.urls import path
from .import views
urlpatterns = [
     path("registration/", views.registration, name="registration"),
     path("login/", views.login, name="myloginpage"),
     path("navbar/", views.navbar, name="navbar"),
     path("contact us/", views.contactus, name="contactus"),
     path("", views.home, name="home"),
     path("FAQs/", views.FAQs, name="FAQs"),
     path('addstudent1/', views.addstudent1, name='addinguser'),
     path('addstudent1', views.addstudent1, name='addstudent1'),
     path('editstudent1/<id>', views.editstudent1, name='editstudent1'),
     path('updatestudent/<id>', views.updatestudent1, name='updatestudent1'),
     path('deletestudent1/<id>', views.deletestudent1, name='deletestudent1')

    ]