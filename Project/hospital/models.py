from django.contrib.auth.models import User
from django.db import models

# Create your models here.


# class Department(models.Model):
    
#     Dpid = models.AutoField(primary_key=True)
#     Dpname = models.CharField(max_length=50)
#     Dphead = models.CharField(max_length=50)
    
#     def __str__(self):
#         return self.Dpname
    
    
# class Doctor(models.Model):
#     Gender = (
#         ('Male','M'),
#         ('Female','F'),
#     )
    
#     user = models.ForeignKey(User,on_delete=models.CASCADE, null=True)
#     Dname = models.CharField(max_length=50)
#     Dgender = models.CharField(max_length=6, choices=Gender)
#     Dphone = models.PositiveIntegerField()
#     Daddress = models.CharField(max_length=100)
#     Dsalary = models.PositiveIntegerField()
#     Demail = models.EmailField(max_length=254,primary_key=True)
#     Dpassword = models.CharField(max_length=30)
#     Ddob = models.DateField(max_length=8)
#     Qualification = models.CharField(max_length=50)
#     Specialisation = models.CharField(max_length=50)
#     Dpid = models.ForeignKey(Department, on_delete=models.CASCADE)
    
#     def __str__(self):
#         return self.Dname
    
    
    
class Patient(models.Model):
    Gender = (
        ('Male','Male'),
        ('Female','Female'),
        ('Others','Others'),
    )
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    Pname = models.CharField(max_length=50)
    Pgender = models.CharField(max_length=6, choices=Gender)
    Paddresss = models.CharField(max_length=100)
    Pphone = models.PositiveIntegerField()
    Pdob = models.DateField(max_length=8)
    Pemail = models.EmailField(max_length=254,primary_key=True)
    Ppassword = models.CharField(max_length=30)
    
    def __str__ (self):
        return self.Pname
    
# class Staff(models.Model):
#     Gender = (
#         ('Male','M'),
#         ('Female','F'),
#     )
    
#     user = models.ForeignKey(User,on_delete=models.CASCADE, null=True)
#     Semail = models.EmailField(max_length=254,primary_key=True)
#     Sname = models.CharField(max_length=50)
#     Sgender = models.CharField(max_length=6, choices=Gender)
#     Saddresss = models.CharField(max_length=100)
#     Sphone = models.PositiveIntegerField()
#     Sdob = models.DateField(max_length=8)
#     Semail = models.EmailField(max_length=254)
#     Spassword = models.CharField(max_length=30)
#     Sjob = models.CharField(max_length=50)
#     Dpid = models.ForeignKey(Department, on_delete=models.CASCADE)
#     Ssalary = models.PositiveIntegerField()
    
#     def __str__(self):
#         return self.Sname
    
# class MR(models.Model):
    
#     Mid = models.AutoField(primary_key=True)
#     Demail = models.ForeignKey(Doctor, on_delete=models.CASCADE)
#     Pemail = models.ForeignKey(Patient, on_delete=models.CASCADE)
#     Diagnosis = models.CharField(max_length=100)
#     rdate = models.DateField(max_length=8)
#     rtime = models.TimeField()
   
#     def __str__ (self):
#         return self.Pid
    
# class Appointment(models.Model):
    
#     Aid = models.AutoField(primary_key=True)
#     Demail = models.ForeignKey(Doctor, on_delete=models.CASCADE)
#     Pemail = models.ForeignKey(Patient, on_delete=models.CASCADE)
#     issue = models.CharField(max_length=50)
#     Adate = models.DateField(max_length=8)
#     Atime = models.TimeField()
    
#     def __str__(self):
#         return self.Pid
    
    
class Feedback(models.Model):
    Fid = models.AutoField(primary_key=True,null=False)
    Pemail = models.ForeignKey(Patient,on_delete=models.CASCADE)
    feedback = models.TextField(max_length=250)
    fdatetime = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.Pemail.Pname
    

    
    