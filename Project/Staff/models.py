from django.db import models
from django.contrib.auth.models import User
from Doctor.models import Department
# Create your models here.

class Staff(models.Model):
    Gender = (
        ('Male','M'),
        ('Female','F'),
    )
    
    user = models.ForeignKey(User,on_delete=models.CASCADE, null=True)
    Semail = models.EmailField(max_length=254,primary_key=True)
    Sname = models.CharField(max_length=50)
    Sgender = models.CharField(max_length=6, choices=Gender)
    Saddresss = models.CharField(max_length=100)
    Sphone = models.PositiveIntegerField()
    Sdob = models.DateField(max_length=8)
    Spassword = models.CharField(max_length=30)
    Sjob = models.CharField(max_length=50)
    Dpid = models.ForeignKey(Department, on_delete=models.CASCADE)
    Ssalary = models.PositiveIntegerField()
    
    def __str__(self):
        return self.Sname
