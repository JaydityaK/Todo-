from django.db import models

# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=100)
    age = models.CharField(max_length=50)
    salary = models.CharField(max_length=100)
    city = models.CharField(max_length=500)
    is_deleted=models.CharField(max_length=2,default="n")
