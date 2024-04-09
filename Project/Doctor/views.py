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
def doctor_dashboard(request):
    User_email = request.user.email
    data=Appointment.objects.filter(Demail=User_email)
    context={
        'data1':data,
    }
    
    return render(request, 'dashboard1.html',context)

# @login_required(login_url='login')
# def About(request):
#     return render(request,'about.html')

# @login_required(login_url='login')
# def Index(request):
#     return render(request,'index.html')

@login_required(login_url='login')
def Patients(request):
    Pdata=Patient.objects.all()
    
    context={
        'aPa':Pdata,
          }
    
    return render(request,'Patientslist.html',context)

@login_required(login_url='login')
def Doctors(request):
    Ddata=Doctor.objects.all()
    
    context={
        'aDa':Ddata,
          }
    
    return render(request,'Doctorslist.html',context)

@login_required(login_url='login')        
def Staffs(request):
    Sdata=Staff.objects.all()
    
    context={
        'aSa':Sdata,
          }
    
    return render(request,'Stafflist.html',context)

@login_required(login_url='login')
def MRlist(request):
    
    doctor=request.user.email
    Mdata=MR.objects.filter(Demail=doctor)
    
    context={
        'MAMA':Mdata,
        
    }
    return render(request,'MRlist.html',context)

@login_required(login_url='login')
def AppEdit(request,Aid):
    formatted_date = None  # Initialize formatted_date and formatted_time to None
    formatted_time = None
    data=Appointment.objects.get(Aid=Aid)
    if data.Adate:
        # Format the date to 'YYYY-MM-DD' format
        formatted_date = data.Adate.strftime('%Y-%m-%d')
    if data.Atime:
        # Format the date to 'YYYY-MM-DD' format
        formatted_time = data.Atime.strftime('%H:%M')
    
    context={
        
        'data':data,
        'formatted_date':formatted_date,
        'formatted_time':formatted_time,
        
    }
    return render(request,'update_A.html',context)

@login_required(login_url='login')
def AppUpdate(request,Aid):
    formatted_date=None
    data=Appointment.objects.get(Aid=Aid)
    update=Appointment.objects.get(Aid=Aid)
    if request.method == 'POST':
        
        update.Adate = request.POST.get('date')
        update.Atime = request.POST.get('time')
        update.Status = request.POST.get('Status')
        
        
        # department_id = None
        # doctor_email = None
        
        
        current_date = datetime.now().date()
        app_date = datetime.strptime(update.Adate, '%Y-%m-%d').date() if update.Adate else None
        current_time = datetime.now().time()
        app_time = datetime.strptime(update.Atime, '%H:%M').time() if update.Atime else None
        
         # Regular expression to check for special characters and numbers in the full name
        if re.search(r'[!@#$%^&*()_+=[\]{};:"\\|,.<>/?\d]', update.Ptname):
            messages.error(request, 'Name cannot contain special characters or numbers.')
            
        # Limit the phone number to 10 digits
        elif not re.match(r'^\d{10}$', update.Ptphone):
            messages.error(request, 'Phone number should be 10 digits long and contain only numbers.')
            
        # Check for other conditions
        elif app_date and app_date < current_date:
            messages.error(request, 'Invalid appointment date. Please enter a valid date for appointment.')
            
        elif app_time and app_time < current_time:
            messages.error(request, 'Invalid appointment time. Please enter a valid time for the appointment.')
            
        else :
            
            update.save()
            return redirect('dash')
        if data.Adate:
            # Format the date to 'YYYY-MM-DD' format
            formatted_date = data.Adate.strftime('%Y-%m-%d')    
    context = {
        'data': update,
        'formatted_date':formatted_date,
    }
    return render(request, 'update_A.html',context)

@login_required(login_url='login')
def D_MR(request):
    if request.method == 'POST':
        name = request.POST.get('pname')
        email = request.POST.get('email')
        date = request.POST.get('date')
        time = request.POST.get('time')
        doctor = request.user.email
        diag = request.POST.get('diagnosis')
    
        
        # Check if an account with the same email already exists
        current_date = datetime.now().date()
        birth_date = datetime.strptime(date, '%Y-%m-%d').date() if date else None
        data_doctor = Doctor.objects.get(Demail=doctor)
        data_patient = Patient.objects.get(Pemail=email)
        

        # Regular expression to check for special characters and numbers in the full name
        if re.search(r'[!@#$%^&*()_+=[\]{};:"\\|,.<>/?\d]', name):
            messages.error(request, 'Full Name cannot contain special characters or numbers.')
               
        # Check for other conditions
        elif birth_date and birth_date > current_date:
            messages.error(request, 'Invalid birth date. Please enter a valid date of birth.')
        
        else:
            
            data = MR.objects.create(Patientname=name, Demail=data_doctor, Pemail=data_patient, Diagnosis=diag, rdate=date, rtime=time)
            data.save()
            print()
            messages.success(request, 'Successfully registered')
            return redirect('RDMR')
        
    dep = Department.objects.all()
    Doc = Doctor.objects.all()
    Pat = Patient.objects.all()
    data_email = request.user.email
    data = Doctor.objects.get(Demail=data_email)
    context={
        'Dep':dep,
        'Doc':Doc,
        'Pat':Pat,
        'data':data,
    }
    
    return render(request,'D_mr.html',context)

@login_required(login_url='login')
def D_MREdit(request,Mid):
    
    data=MR.objects.get(Mid=Mid)
    if data.rdate:
        # Format the date to 'YYYY-MM-DD' format
        formatted_date = data.rdate.strftime('%Y-%m-%d')
    if data.rtime:
        # Format the date to 'YYYY-MM-DD' format
        formatted_time = data.rtime.strftime('%H:%M:%S')  # Adjust the format as required
    dep = Department.objects.all()
    Doc = Doctor.objects.all()
    Pat = Patient.objects.all()
    context={
        'Dep':dep,
        'Doc':Doc,
        'Pat':Pat,
        'formatted_time': formatted_time,
        
        
    'data':data,
    'formatted_date':formatted_date
    }
    return render(request,'U_dmr.html',context)

@login_required(login_url='login')        
def D_MRUpdate(request,Mid):
    update=MR.objects.get(Mid=Mid)
    if request.method == 'POST':
        update.Patientname = request.POST.get('pname')
        update.Pemail.Pemail = request.POST.get('email')
        update.rdate = request.POST.get('date')
        update.rtime = request.POST.get('time')
        # update.Demail.Demail = request.POST.get('dname')
        update.Diagnosis = request.POST.get('diagnosis')
        
        current_date = datetime.now().date()
        # date_obj = datetime.strptime(date_string, '%b. %d, %Y')
        # formatted_date = date_obj.strftime('%Y-%m-%d')
        birth_date = datetime.strptime(update.rdate, '%Y-%m-%d').date() if update.rdate else None

        # However, you need to check if 'birth_date' is not None before formatting it
        # formatted_date = birth_date.strftime('%Y-%m-%d') if birth_date else None
        # Dp_id = Department.objects.get(Dpname=UDpname)
        # D_email = Doctor.objects.filter(Demail=update.Demail)
        # D_others = D_email.exclude(Dname=update.Dname)
        
            
        # if D_others.exists():
        #     messages.error(request, 'Email is already in use. Please choose a different one.')
            
        if re.search(r'[!@#$%^&*()_+=[\]{};:"\\|,.<>/?\d]', update.Patientname):
            messages.error(request, 'Full Name cannot contain special characters or numbers.')
            
        # Check for other conditions
        elif birth_date and birth_date > current_date:
            messages.error(request, 'Invalid birth date. Please enter a valid date of birth.')
            
        else:
            
            
            update.save()
    return redirect('DMRS')

@login_required(login_url='login')
def own(request):
    doctor_email=request.user.email
    data = Doctor.objects.get(Demail=doctor_email)
    if data.Ddob:
        # Format the date to 'YYYY-MM-DD' format
        formatted_date = data.Ddob.strftime('%Y-%m-%d')
    context={
        'data':data,
        'formatted_date':formatted_date
    }
    return render(request,'Down.html',context)

@login_required(login_url='login')    
def ownedit(request,Doctor_email):
    
    dep=Department.objects.all()
    data = Doctor.objects.get(Demail=Doctor_email)
    if data.Ddob:
        # Format the date to 'YYYY-MM-DD' format
        formatted_date = data.Ddob.strftime('%Y-%m-%d')
    context={
        'data':data,
        'formatted_date':formatted_date,
        'dep':dep
    }
    
    return render(request,'U_Down.html',context)

@login_required(login_url='login')
def ownupdate(request,Doctor_email):
    update=Doctor.objects.get(Demail=Doctor_email)
    if request.method == 'POST':
        update.Dname = request.POST.get('Dname')
        update.Daddress = request.POST.get('address')
        update.Ddob = request.POST.get('dob')
        update.Dphone = request.POST.get('phone')
        update.Dgender = request.POST.get('gender')
        update.Dpassword = request.POST.get('password')
        cpassword = request.POST.get('cpassword')
        update.Dsalary = request.POST.get('salary')
        update.Specialisation = request.POST.get('specs')
        update.Qualification = request.POST.get('qual')
        update.Dpid.Dpid = request.POST.get('dep')
        
        # original_doctor = request.user.email
        current_date = datetime.now().date()
        # date_obj = datetime.strptime(date_string, '%b. %d, %Y')
        # formatted_date = date_obj.strftime('%Y-%m-%d')
        birth_date = datetime.strptime(update.Ddob, '%Y-%m-%d').date() if update.Ddob else None

        # However, you need to check if 'birth_date' is not None before formatting it
        # formatted_date = birth_date.strftime('%Y-%m-%d') if birth_date else None
        # Dp_id = Department.objects.get(Dpname=UDpname)
        # D_email = Doctor.objects.filter(Demail=update.Demail)
        # D_others = D_email.exclude(Dname=update.Dname)
        
            
        # if D_others.exists():
        #     messages.error(request, 'Email is already in use. Please choose a different one.')
            
        if re.search(r'[!@#$%^&*()_+=[\]{};:"\\|,.<>/?\d]', update.Dname):
            messages.error(request, 'Full Name cannot contain special characters or numbers.')
            
        # Limit the phone number to 10 digits
        elif not re.match(r'^\d{10}$', update.Dphone):
            messages.error(request, 'Phone number should be 10 digits long and contain only numbers.')
            
        # Check for other conditions
        elif birth_date and birth_date > current_date:
            messages.error(request, 'Invalid birth date. Please enter a valid date of birth.')
            
        elif update.Dpassword == cpassword:
            
            # data = Staff.objects.update(Dpid=Dp_id)
            # data.save()
            
            update.save()
            
    return redirect('own')

def Logout(request):
    if request.method == 'POST':
        logout(request)
        
    return redirect('home')

