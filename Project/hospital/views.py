from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from .models import Patient,Feedback
from Admin.models import Appointment,MR
from Doctor.models import Doctor,Department
from django.contrib import messages
from datetime import datetime
import re
from django.http import HttpResponse
from Staff.models import Staff

# Create your views here.

def About(request):
    return render(request,'about.html')


def Index(request):
    return render(request,'index.html')

def Register(request):
    if request.method == 'POST':
        name = request.POST.get('Fname')
        address = request.POST.get('address')
        email = request.POST.get('email')
        dob = request.POST.get('dob')
        phone = request.POST.get('phone')
        gender = request.POST.get('gender')
        password = request.POST.get('password')
        cpassword = request.POST.get('cpassword')

        # Check if an account with the same email already exists
        current_date = datetime.now().date()
        birth_date = datetime.strptime(dob, '%Y-%m-%d').date() if dob else None

        # Regular expression to check for special characters and numbers in the full name
        if re.search(r'[!@#$%^&*()_+=[\]{};:"\\|,.<>/?\d]', name):
            messages.error(request, 'Full Name cannot contain special characters or numbers.')
            
        # Limit the phone number to 10 digits
        elif not re.match(r'^\d{10}$', phone):
            messages.error(request, 'Phone number should be 10 digits long and contain only numbers.')
            
        # Check for other conditions
        elif birth_date and birth_date > current_date:
            messages.error(request, 'Invalid birth date. Please enter a valid date of birth.')
            
        elif Patient.objects.filter(Pemail=email).exists():
            messages.error(request, 'Email is already in use. Please choose a different one.')
        
        elif password == cpassword:
            
            user = User.objects.create_user(username=email, password=password, email=email)
            data = Patient.objects.create(Pname=name, Paddresss=address, Pemail=email, Ppassword=password, Pdob=dob, Pphone=phone, Pgender=gender)
            data.save()
            print()
            messages.success(request, 'Successfully registered')
            return redirect('login')
        
        else:
            messages.error(request, 'Passwords do not match. Registration failed.')

    return render(request, 'Registration.html')

def user_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Check if the email and password match a superuser
        superuser_email = 'admin@gmail.com'
        superuser_password = 'Password@123'

        if email == superuser_email and password == superuser_password:
            try:
                user = User.objects.get(email=superuser_email)
                if user.is_superuser:
                    login(request, user)
                    return redirect('admin_dashboard')
                else:
                    messages.error(request, 'Invalid user type. Please contact the administrator.')
            except User.DoesNotExist:
                messages.error(request, 'Superuser does not exist.')
        else:
            # Check if the user is a Patient or Doctor using authenticate
            user = authenticate(request, username=email, password=password)

            if user is not None:
                if Patient.objects.filter(Pemail=email).exists():
                    login(request, user)
                    return redirect('patient_dashboard')
                elif Doctor.objects.filter(Demail=email).exists():
                    login(request, user)
                    return redirect('dash')
                elif Staff.objects.filter(Semail=email).exists():
                    login(request, user)
                    return redirect('Sdash')
                else:
                    messages.error(request, 'Invalid user type. Please contact the administrator.')
            else:
                messages.error(request, 'Invalid email or password. Please try again.')

    return render(request, 'login.html')

@login_required(login_url='login')
def patient_dashboard(request):
    User_email = request.user.email
    data=Appointment.objects.filter(Pemail=User_email)
    context={
        'data':data,
    }
    return render(request,'patient.html',context)

@login_required(login_url='login')
def doctor_list(request):
    doctor=Doctor.objects.all()
    
    context={
        'doctor':doctor,
        
    }
    return render(request,'doctor_list.html',context)

@login_required(login_url='login')
def contact_staff(request):
    staff=Staff.objects.all()
    
    context={
        'staff':staff,
        
    }
    return render(request,'Contactstaff.html',context)

@login_required(login_url='login')
def M_R(request):
    user_email = request.user.email
    
    Medical=MR.objects.filter(Pemail=user_email)
    
    context={
        'MR':Medical,
        
    }
    return render(request,'MR.html',context)

#     return render(request, 'doctor_list.html', context)
@login_required(login_url='login')
def appointment_form(request):
    if request.method == 'POST':
        
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        date = request.POST.get('date')
        issue = request.POST.get('issue')
        doctor_name = request.POST.get('doctor')
        
        # department_id = None
        # doctor_email = None
        
        
        current_date = datetime.now().date()
        app_date = datetime.strptime(date, '%Y-%m-%d').date() if date else None
        
         # Regular expression to check for special characters and numbers in the full name
        if re.search(r'[!@#$%^&*()_+=[\]{};:"\\|,.<>/?\d]', name):
            messages.error(request, 'Name cannot contain special characters or numbers.')
            
        # Limit the phone number to 10 digits
        elif not re.match(r'^\d{10}$', phone):
            messages.error(request, 'Phone number should be 10 digits long and contain only numbers.')
            
        # Check for other conditions
        elif app_date and app_date < current_date:
            messages.error(request, 'Invalid appointment date. Please enter a valid date for appointment.')
            
        else :
            
            patient_data = Patient.objects.get(Pemail=email)
            doctor_data = Doctor.objects.get(Dname=doctor_name)
            # demail=doctor_data.Demail
            data = Appointment.objects.create(Ptname=name, Pemail=patient_data, Adate=date, issue=issue, Demail=doctor_data, Ptphone=phone)
            data.save()
            messages.success(request, 'Appointment placed. Please wait for our Doctors to confirm.')
            return redirect('appointment')
            
            # try:
                
            #     doctor = Doctor.objects.all()
            #     department = Department.objects.get(Dpname=department_name)
            #     doctor = Doctor.objects.filter(Dpid=department)

            #     if doctor_name:
            #         doctor = doctor.filter(Dname=doctor_name)

            #     if doctor.exists():
            #         doctor_email = doctor[0].Demail
            #         data = Appointment.objects.create(Ptname=name, Pemail=email, Adate=date, issue=issue, Demail=doctor_email, Ptphone=phone, Dpname=department_name)
            #         data.save()
            #         messages.success(request, 'Appointment placed. Please wait for our Doctors to confirm.')
            #         return redirect('appointment')
            #     else:
            #         messages.error(request, 'Doctor not found in the selected department.')
            # except Department.DoesNotExist:
            #     messages.error(request, 'Department not found.')
                

    # departments = Department.objects.all()
    doctors = Doctor.objects.all()
    context = {
        'Doc': doctors,
        #'Dep': departments
    }

    return render(request, 'Appointment.html', context)


def Logout(request):
    if request.method == 'POST':
        logout(request)
        
    return redirect('home')

@login_required(login_url='login')
def Self(request):
    patient_email=request.user.email
    data = Patient.objects.get(Pemail=patient_email)
    if data.Pdob:
        # Format the date to 'YYYY-MM-DD' format
        formatted_date = data.Pdob.strftime('%Y-%m-%d')
    context={
        'data':data,
        'formatted_date':formatted_date
    }
    
    return render(request,'Self.html',context)

@login_required(login_url='login')
def U_Self(request,patient_email):
    
    data = Patient.objects.get(Pemail=patient_email)
    if data.Pdob:
        # Format the date to 'YYYY-MM-DD' format
        formatted_date = data.Pdob.strftime('%Y-%m-%d')
    context={
        'data':data,
        'formatted_date':formatted_date
    }
    
    return render(request,'U_self.html',context)

@login_required(login_url='login')
def U_SELF(request,patient_email):
    update=Patient.objects.get(Pemail=patient_email)
    if request.method == 'POST':
        update.Pname = request.POST.get('fullname')
        update.Paddresss = request.POST.get('address')
        update.Pdob = request.POST.get('dob')
        update.Pphone = request.POST.get('phone')
        update.Pgender = request.POST.get('gender')
        update.Ppassword = request.POST.get('password')
        cpassword = request.POST.get('cpassword')
        
        current_date = datetime.now().date()
        # date_obj = datetime.strptime(date_string, '%b. %d, %Y')
        # formatted_date = date_obj.strftime('%Y-%m-%d')
        birth_date = datetime.strptime(update.Pdob, '%Y-%m-%d').date() if update.Pdob else None

        # However, you need to check if 'birth_date' is not None before formatting it
        # formatted_date = birth_date.strftime('%Y-%m-%d') if birth_date else None
        # Dp_id = Department.objects.get(Dpname=UDpname)
        # D_email = Doctor.objects.filter(Demail=update.Demail)
        # D_others = D_email.exclude(Dname=update.Dname)
        
            
        # if D_others.exists():
        #     messages.error(request, 'Email is already in use. Please choose a different one.')
            
        if re.search(r'[!@#$%^&*()_+=[\]{};:"\\|,.<>/?\d]', update.Pname):
            messages.error(request, 'Full Name cannot contain special characters or numbers.')
            
        # Limit the phone number to 10 digits
        elif not re.match(r'^\d{10}$', update.Pphone):
            messages.error(request, 'Phone number should be 10 digits long and contain only numbers.')
            
        # Check for other conditions
        elif birth_date and birth_date > current_date:
            messages.error(request, 'Invalid birth date. Please enter a valid date of birth.')
            
        elif update.Ppassword == cpassword:
            
            
            update.save()
    return redirect('vself')

@login_required(login_url='login')
def feedback(request):
    if request.method=='POST':
      email= request.POST.get('email')
      feedback=request.POST.get('feedback')
      patient_data=Patient.objects.get(Pemail=email)
      data=Feedback.objects.create(Pemail=patient_data,feedback=feedback)
      data.save()
      messages.success(request,'Feedback Submitted')
      

    return render(request,'feedback.html')
    