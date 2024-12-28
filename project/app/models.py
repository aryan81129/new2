from django.db import models
from datetime import datetime
# Create your models here.

class BaseInfo(models.Model):
    name=models.CharField( max_length=50)
    dob=models.DateTimeField()
    address=models.CharField( max_length=50)
    class Meta:
        abstract = True

class Student(BaseInfo):
    branch=models.CharField(max_length=50)
    dob=models.DateField()
    fees=models.IntegerField()
    
    
class Employee(BaseInfo):
    department=models.CharField(max_length=50)
    salary=models.IntegerField()
    dob=False
    
        