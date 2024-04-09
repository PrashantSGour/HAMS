from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Department(models.Model):
    
    Dpid = models.AutoField(primary_key=True)
    Dpname = models.CharField(max_length=50)
    Dphead = models.CharField(max_length=50)
    
    def __str__(self):
        return self.Dpname
    

class Doctor(models.Model):
    Gender = (
        ('Male','M'),
        ('Female','F'),
    )
    
    user = models.ForeignKey(User,on_delete=models.CASCADE, null=True)
    Dname = models.CharField(max_length=50)
    Dgender = models.CharField(max_length=6, choices=Gender)
    Dphone = models.PositiveIntegerField()
    Daddress = models.CharField(max_length=100)
    Dsalary = models.PositiveIntegerField()
    Demail = models.EmailField(max_length=254,primary_key=True)
    Dpassword = models.CharField(max_length=30)
    Ddob = models.DateField(max_length=8)
    Qualification = models.CharField(max_length=50)
    Specialisation = models.CharField(max_length=50)
    Dpid = models.ForeignKey(Department, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.Dname
