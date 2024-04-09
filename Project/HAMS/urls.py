"""
URL configuration for HAMS project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from hospital import views
import Admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/',views.About,name='about'),
    path('',views.Index,name='home'),
    path('registration/', views.Register,name="register"),
    path('login/',views.user_login,name='login'),
    path('logout/',views.Logout,name='logout'),
    path('Doctor/', include('Doctor.urls')),
    path('patient_das/',views.patient_dashboard,name='patient_dashboard'),
    path('doctor_list',views.doctor_list,name='doctors'),
    path('appointment_form/',views.appointment_form,name='appointment'),
    path('Ad/', include('Admin.urls')),
    path('Contactstaff/',views.contact_staff,name='staff'),
    path('MedicalRecords/',views.M_R,name='Mr'),
    path('feedback/',views.feedback,name='feedback'),
    path('view_self/',views.Self,name='vself'),
    path('edit-self/<str:patient_email>/',views.U_Self,name='Selfedit'),
    path('update-self/<str:patient_email>/',views.U_SELF,name='selfupdate'),
    path('Staff/', include('Staff.urls')),
 ]
