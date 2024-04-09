from django.shortcuts import render
from hospital.models import Patient
from Doctor.models import Doctor
from .models import Appointment,MR
from Staff.models import Staff
from django.db.models import Q
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from hospital.models import Patient,Feedback
from Admin.models import Appointment,MR
from Doctor.models import Doctor,Department
from django.contrib import messages
from datetime import datetime
import re
from django.http import HttpResponse
from Staff.models import Staff



# Create your views here.
@login_required(login_url='login')
def Admin_dashboard(request):
    Adata = Appointment.objects.all()
    context={
        'data':Adata,
    }
    return render(request,'Dashboard.html',context)

@login_required(login_url='login')
def Patient_list(request):
    Pdata=Patient.objects.all()
    
    context={
        'aPa':Pdata,
          }
    
    return render(request,'Patients_list.html',context)

@login_required(login_url='login')
def Doctor_list(request):
    Ddata=Doctor.objects.all()
    
    context={
        'aDa':Ddata,
          }
    
    return render(request,'Doctors_list.html',context)

@login_required(login_url='login')        
def Staff_list(request):
    Sdata=Staff.objects.all()
    
    context={
        'aSa':Sdata,
          }
    
    return render(request,'Staff_list.html',context)

@login_required(login_url='login')
def MR_list(request):
    
    Mdata=MR.objects.all()
    
    context={
        'aMRa':Mdata,
        
    }
    return render(request,'MR_list.html',context)

@login_required(login_url='login')
def F_list(request):
    
    Fdata=Feedback.objects.all()
    
    context={
        'aFa':Fdata,
        
    }
    return render(request,'Feedback_list.html',context)

@login_required(login_url='login')
def Register_doctor(request):
    if request.method == 'POST':
        name = request.POST.get('Dname')
        address = request.POST.get('address')
        email = request.POST.get('email')
        dob = request.POST.get('dob')
        phone = request.POST.get('phone')
        gender = request.POST.get('gender')
        password = request.POST.get('password')
        cpassword = request.POST.get('cpassword')
        salary = request.POST.get('salary')
        specialisation = request.POST.get('specs')
        qualification = request.POST.get('qual')
        depart = request.POST.get('dep')
        print(gender)
        # Check if an account with the same email already exists
        current_date = datetime.now().date()
        birth_date = datetime.strptime(dob, '%Y-%m-%d').date() if dob else None
        Dp_id = Department.objects.get(Dpname=depart)

        # Regular expression to check for special characters and numbers in the full name
        if re.search(r'[!@#$%^&*()_+=[\]{};:"\\|,.<>/?\d]', name):
            messages.error(request, 'Full Name cannot contain special characters or numbers.')
            
        # Limit the phone number to 10 digits
        elif not re.match(r'^\d{10}$', phone):
            messages.error(request, 'Phone number should be 10 digits long and contain only numbers.')
            
        # Check for other conditions
        elif birth_date and birth_date > current_date:
            messages.error(request, 'Invalid birth date. Please enter a valid date of birth.')
            
        elif Doctor.objects.filter(Demail=email).exists():
            messages.error(request, 'Email is already in use. Please choose a different one.')
        
        elif password == cpassword:
            
            user = User.objects.create_user(username=email, password=password, email=email)
            data = Doctor.objects.create(Dname=name, Daddress=address, Demail=email, Dpassword=password, Ddob=dob, Dphone=phone, Dgender=gender, Dsalary=salary, Specialisation=specialisation, Qualification=qualification, Dpid=Dp_id)
            data.save()
            print()
            messages.success(request, 'Successfully registered')
            return redirect('RD')
        
        else:
            messages.error(request, 'Passwords do not match. Registration failed.')

    dep = Department.objects.all()
    context={
        'Dep':dep
    }
    
    return render(request,'R_doctor.html',context)


def Register_staff(request):
    if request.method == 'POST':
        name = request.POST.get('Sname')
        address = request.POST.get('address')
        email = request.POST.get('email')
        dob = request.POST.get('dob')
        phone = request.POST.get('phone')
        gender = request.POST.get('gender')
        password = request.POST.get('password')
        cpassword = request.POST.get('cpassword')
        salary = request.POST.get('salary')
        job = request.POST.get('job')
        depart = request.POST.get('dep')
        

        # Check if an account with the same email already exists
        current_date = datetime.now().date()
        birth_date = datetime.strptime(dob, '%Y-%m-%d').date() if dob else None
        Dp_id = Department.objects.get(Dpname=depart)
        

        # Regular expression to check for special characters and numbers in the full name
        if re.search(r'[!@#$%^&*()_+=[\]{};:"\\|,.<>/?\d]', name):
            messages.error(request, 'Full Name cannot contain special characters or numbers.')
            
        # Limit the phone number to 10 digits
        elif not re.match(r'^\d{10}$', phone):
            messages.error(request, 'Phone number should be 10 digits long and contain only numbers.')
            
        # Check for other conditions
        elif birth_date and birth_date > current_date:
            messages.error(request, 'Invalid birth date. Please enter a valid date of birth.')
            
        elif Doctor.objects.filter(Demail=email).exists():
            messages.error(request, 'Email is already in use. Please choose a different one.')
        
        elif password == cpassword:
            
            user = User.objects.create_user(username=email, password=password, email=email)
            data = Staff.objects.create(Sname=name, Saddresss=address, Semail=email, Spassword=password, Sdob=dob, Sphone=phone, Sgender=gender, Ssalary=salary, Sjob=job, Dpid=Dp_id)
            data.save()
            print()
            messages.success(request, 'Successfully registered')
            return redirect('RS')
        
        else:
            messages.error(request, 'Passwords do not match. Registration failed.')    
    
    dep = Department.objects.all()
    context ={
        'Dep':dep
    }
    
    return render(request,'R_staff.html',context)

@login_required(login_url='login')
def Register_MR(request):
    if request.method == 'POST':
        name = request.POST.get('pname')
        email = request.POST.get('email')
        date = request.POST.get('date')
        time = request.POST.get('time')
        doctor = request.POST.get('dname')
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
            return redirect('RMR')
        
    dep = Department.objects.all()
    Doc = Doctor.objects.all()
    Pat = Patient.objects.all()
    context={
        'Dep':dep,
        'Doc':Doc,
        'Pat':Pat,
        
    }
    
    return render(request,'R_mr.html',context)


@login_required(login_url='login')
def DoctorEdit(request,doctor_email):
    
    data=Doctor.objects.get(Demail=doctor_email)
    dep = Department.objects.all()
    if data.Ddob:
        # Format the date to 'YYYY-MM-DD' format
        formatted_date = data.Ddob.strftime('%Y-%m-%d')
        
    context={'dep':dep,'data':data,'formatted_date':formatted_date}
    return render(request,'U_doctor.html',context)
    
@login_required(login_url='login')
def DoctorUpdate(request,doctor_email):
    update=Doctor.objects.get(Demail=doctor_email)
    if request.method == 'POST':
        update.Dname = request.POST.get('Dname')
        update.Daddress = request.POST.get('address')
        update.Demail = request.POST.get('email')
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
            
    return redirect('Dlist')

@login_required(login_url='login')
def PatientEdit(request,patient_email):
    
    data=Patient.objects.get(Pemail=patient_email)
    if data.Pdob:
        # Format the date to 'YYYY-MM-DD' format
        formatted_date = data.Pdob.strftime('%Y-%m-%d')
        
    context={'data':data,'formatted_date':formatted_date}
    return render(request,'U_patient.html',context)

@login_required(login_url='login')
def PatientUpdate(request,patient_email):
    update=Patient.objects.get(Pemail=patient_email)
    if request.method == 'POST':
        update.Pname = request.POST.get('Fname')
        update.Paddresss = request.POST.get('address')
        update.Pemail = request.POST.get('email')
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
    return redirect('Plist')

@login_required(login_url='login')
def MREdit(request,Mid):
    
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
    return render(request,'U_mr.html',context)

@login_required(login_url='login')        
def MRUpdate(request,Mid):
    update=MR.objects.get(Mid=Mid)
    if request.method == 'POST':
        update.Patientname = request.POST.get('pname')
        update.Pemail.Pemail = request.POST.get('email')
        update.rdate = request.POST.get('date')
        update.rtime = request.POST.get('time')
        update.Demail.Demail = request.POST.get('dname')
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
    return redirect('MRlist')

@login_required(login_url='login')
def AppEdit(request,Aid):
    
    data=Appointment.objects.get(Aid=Aid)
    if data.Adate:
        # Format the date to 'YYYY-MM-DD' format
        formatted_date = data.Adate.strftime('%Y-%m-%d')
    if data.Atime:
        # Format the date to 'YYYY-MM-DD' format
        formatted_time = data.Atime.strftime('%H:%M:%S')  # Adjust the format as required
    dep = Department.objects.all()
    doc = Doctor.objects.all()
    
    context={
        'Dep':dep,
        'Doc':doc,
        'formatted_time': formatted_time,
        
        
    'data':data,
    'formatted_date':formatted_date
    }
    return render(request,'U_app.html',context)

@login_required(login_url='login')
def AppUpdate(request,Aid):
    update=Appointment.objects.get(Aid=Aid)
    if request.method == 'POST':
        
        update.Ptname = request.POST.get('name')
        update.Pemail.Pemail = request.POST.get('email')
        update.Ptphone = request.POST.get('phone')
        update.Adate = request.POST.get('date')
        update.Atime = request.POST.get('time')
        update.Demail.Demail = request.POST.get('doctor')
        update.issue = request.POST.get('issue')
        update.Status = request.POST.get('Status')
        
        
        # department_id = None
        # doctor_email = None
        
        
        current_date = datetime.now().date()
        app_date = datetime.strptime(update.Adate, '%Y-%m-%d').date() if update.Adate else None
        
         # Regular expression to check for special characters and numbers in the full name
        if re.search(r'[!@#$%^&*()_+=[\]{};:"\\|,.<>/?\d]', update.Ptname):
            messages.error(request, 'Name cannot contain special characters or numbers.')
            
        # Limit the phone number to 10 digits
        elif not re.match(r'^\d{10}$', update.Ptphone):
            messages.error(request, 'Phone number should be 10 digits long and contain only numbers.')
            
        # Check for other conditions
        elif app_date and app_date < current_date:
            messages.error(request, 'Invalid appointment date. Please enter a valid date for appointment.')
            
        else :
            
            update.save()
            
            
    return redirect('admin_dashboard')


@login_required(login_url='login')
def StaffEdit(request,staff_email):
    data=Staff.objects.get(Semail=staff_email)
    dep=Department.objects.all()
    if data.Sdob:
        # Format the date to 'YYYY-MM-DD' format
        formatted_date = data.Sdob.strftime('%Y-%m-%d')
        
    context={'data':data,'formatted_date':formatted_date,'Dep':dep}
    return render(request,'U_staff.html',context)

@login_required(login_url='login')
def StaffUpdate(request,staff_email):
    update=Staff.objects.get(Semail=staff_email)
    if request.method == 'POST':
        update.Sname = request.POST.get('Sname')
        update.Saddresss = request.POST.get('address')
        update.Semail = request.POST.get('email')
        update.Sdob = request.POST.get('dob')
        update.Sphone = request.POST.get('phone')
        update.Sgender = request.POST.get('gender')
        update.Spassword = request.POST.get('password')
        update.Sjob = request.POST.get('job')
        update.Ssalary = request.POST.get('salary')
        update.Dpid.Dpid = request.POST.get('dep')
        cpassword = request.POST.get('cpassword')
        
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
            
            
            update.save()
    return redirect('Slist')

@login_required(login_url='login')
def FeedbackEdit(request,Fid):
    data=Feedback.objects.get(Fid=Fid)
    if data.fdatetime:
        # Format the date to 'YYYY-MM-DD' format
        formatted_date = data.fdatetime.strftime('%Y-%m-%d')
        
    context={'data':data,'formatted_date':formatted_date}
    return render(request,'U_feedback.html',context)

@login_required(login_url='login')
def FUpdate(request,Fid):
    update=Feedback.objects.get(Fid=Fid)
    if request.method == 'POST':
        update.feedback = request.POST.get('feedback')
        update.Pemail.Pemail = request.POST.get('email')
        
               
        update.save()
    return redirect('Flist')


@login_required(login_url='login')
def MRdelete(request,Mid):
    data=MR.objects.get(Mid=Mid)
    data.delete()
    return redirect('MRlist')

@login_required(login_url='login')
def Pdelete(request,patient_id):
    data=Patient.objects.get(Pemail=patient_id)
    data.delete()
    return redirect('Plist')

@login_required(login_url='login')
def Sdelete(request,staff_id):
    data=Staff.objects.get(Semail=staff_id)
    data.delete()
    return redirect('Slist')

@login_required(login_url='login')        
def Adelete(request,Aid):
    data=Appointment.objects.get(Aid=Aid)
    data.delete()
    return redirect('admin_dashboard')

@login_required(login_url='login')
def Ddelete(request,doctor_email):
    data=Doctor.objects.get(Demail=doctor_email)
    data.delete()
    return redirect('Dlist')    

@login_required(login_url='login')
def Fdelete(request,Fid):
    data=Feedback.objects.get(Fid=Fid)
    data.delete()
    return redirect('Flist')

def Logout(request):
    if request.method == 'POST':
        logout(request)
        
    return redirect('home')