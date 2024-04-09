from django.db import models
from Doctor.models import Doctor, Department
from hospital.models import Patient


# Create your models here.
class MR(models.Model):
    
    Mid = models.AutoField(primary_key=True)
    Patientname = models.CharField(max_length=50)
    Demail = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    Pemail = models.ForeignKey(Patient, on_delete=models.CASCADE)
    Diagnosis = models.CharField(max_length=100)
    rdate = models.DateField(max_length=8)
    rtime = models.TimeField()
   
    def __str__ (self):
        return self.Patientname
    
class Appointment(models.Model):
    status= (
        ('Confirm','Confirm'),
        ('Decline','Decline'),
    )
    
    Aid = models.AutoField(primary_key=True)
    Demail = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    Pemail = models.ForeignKey(Patient, on_delete=models.CASCADE)
    Ptname =models.CharField(max_length=50)
    Ptphone = models.CharField(max_length=10)
    Dpid = models.ForeignKey(Department, on_delete=models.CASCADE, null=True)
    issue = models.CharField(max_length=50)
    Adate = models.DateField(max_length=8)
    Atime = models.TimeField(null=True)
    Status = models.CharField(max_length=7,choices=status)
    
    def __str__(self):
        return self.Ptname