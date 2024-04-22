from django.db import models

# Create your models here.

class Data(models.Model):
    studentname = models.CharField(max_length=100)
    emailaddress = models.EmailField(unique=True)
    studentage = models.CharField(max_length=15, blank=True, null=True)
