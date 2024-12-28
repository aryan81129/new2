from django.contrib import admin
from .models import *
# Register your models here.


@admin.register(Student)
class Student(admin.ModelAdmin):
    list_display=['id', 'name', 'dob', 'address','branch','fees']
    
@admin.register(Employee)
class Emmployee(admin.ModelAdmin):
    list_display=['id', 'name','address','department','salary']