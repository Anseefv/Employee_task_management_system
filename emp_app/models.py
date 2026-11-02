from django.db import models
# Create your models here.
from django.contrib.auth.models import AbstractUser




class Employees(models.Model):
    
    name=models.CharField(max_length=100)
    email=models.EmailField()
    department=models.CharField(max_length=100)
    designation=models.CharField(max_length=100)
    joining_date=models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name

class Operations(models.Model):

    title=models.CharField(max_length=200)
    description=models.TextField()
    assigned_to=models.ForeignKey(Employees,on_delete=models.CASCADE,related_name="operation")

    PRIORITY_OPTIONS=[
        ("Low","Low"),
        ("Medium","Medium"),
        ("High","High"),
    ]
    priority=models.CharField(max_length=20,choices=PRIORITY_OPTIONS,default="Medium")

    STATUS_OPTIONS=[
        ("Pending","Pending"),
        ("in_Progress","in_Progress"),
        ("Completed","Completed"),
    ]
    status=models.CharField(max_length=50,choices=STATUS_OPTIONS,default="Pending")

    due_date=models.DateField()


