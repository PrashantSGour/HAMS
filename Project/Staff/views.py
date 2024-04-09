from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from hospital.models import Patient
from Admin.models import Appointment,MR
from Doctor.models import Doctor,Department
from django.contrib import messages
from datetime import datetime
import re
from django.http import HttpResponse
from Staff.models import Staff

# Create your views here.
@login_required(login_url='login')
def staff_dashboard(request):
    User_email = request.user.email
    data=Appointment.objects.all()
    context={
        'data1':data,
    }
    
    return render(request, 'Sdashboard.html',context)

@login_required(login_url='login')
def SPatients(request):
    Pdata=Patient.objects.all()
    
    context={
        'aPa':Pdata,
          }
    
    return render(request,'SPatientslist.html',context)

@login_required(login_url='login')
def SDoctors(request):
    Ddata=Doctor.objects.all()
    
    context={
        'aDa':Ddata,
          }
    
    return render(request,'SDoctorslist.html',context)

@login_required(login_url='login')
def SStaffs(request):
    Sdata=Staff.objects.all()
    
    context={
        'aSa':Sdata,
          }
    
    return render(request,'SStafflist.html',context)

@login_required(login_url='login')
def Sown(request):
    staff_email=request.user.email
    data = Staff.objects.get(Semail=staff_email)
    if data.Sdob:
        # Format the date to 'YYYY-MM-DD' format
        formatted_date = data.Sdob.strftime('%Y-%m-%d')
    context={
        'data':data,
        'formatted_date':formatted_date
    }
    return render(request,'Sown.html',context)

@login_required(login_url='login')
def Sownedit(request,Staff_email):
    
    dep=Department.objects.all()
    data = Staff.objects.get(Semail=Staff_email)
    if data.Sdob:
        # Format the date to 'YYYY-MM-DD' format
        formatted_date = data.Sdob.strftime('%Y-%m-%d')
    context={
        'data':data,
        'formatted_date':formatted_date,
        'dep':dep
    }
    
    return render(request,'Supdate.html',context)

@login_required(login_url='login')
def Sownupdate(request,Staff_email):
    update=Staff.objects.get(Semail=Staff_email)
    if request.method == 'POST':
        update.Sname = request.POST.get('Sname')
        update.Saddresss = request.POST.get('Saddress')
        update.Sdob = request.POST.get('Sdob')
        update.Sphone = request.POST.get('phone')
        update.Sgender = request.POST.get('gender')
        update.Spassword = request.POST.get('password')
        cpassword = request.POST.get('cpassword')
        update.Ssalary = request.POST.get('salary')
        update.Sjob = request.POST.get('specs')
        update.Dpid.Dpid = request.POST.get('dep')
        
        # original_doctor = request.user.email
        current_date = datetime.now().date()
        # date_obj = datetime.strptime(date_string, '%b. %d, %Y')
        # formatted_date = date_obj.strftime('%Y-%m-%d')
        birth_date = datetime.strptime(update.Sdob, '%Y-%m-%d').date() if update.Sdob else None

        # However, you need to check if 'birth_date' is not None before formatting it
        # formatted_date = birth_date.strftime('%Y-%m-%d') if birth_date else None
        # Dp_id = Department.objects.get(Dpname=UDpname)
        # D_email = Doctor.objects.filter(Demail=update.Demail)
        # D_others = D_email.exclude(Dname=update.Dname)
        
            
        # if D_others.exists():
        #     messages.error(request, 'Email is already in use. Please choose a different one.')
            
        if re.search(r'[!@#$%^&*()_+=[\]{};:"\\|,.<>/?\d]', update.Sname):
            messages.error(request, 'Full Name cannot contain special characters or numbers.')
            
        # Limit the phone number to 10 digits
        elif not re.match(r'^\d{10}$', update.Sphone):
            messages.error(request, 'Phone number should be 10 digits long and contain only numbers.')
            
        # Check for other conditions
        elif birth_date and birth_date > current_date:
            messages.error(request, 'Invalid birth date. Please enter a valid date of birth.')
            
        elif update.Spassword == cpassword:
            
            # data = Staff.objects.update(Dpid=Dp_id)
            # data.save()
            
            update.save()
            
    return redirect('Sown')

@login_required(login_url='login')
def SMR_list(request):
    
    Mdata=MR.objects.all()
    
    context={
        'aMRa':Mdata,
        
    }
    return render(request,'SMR_list.html',context)


def Logout(request):
    if request.method == 'POST':
        logout(request)
        
    return redirect('home')