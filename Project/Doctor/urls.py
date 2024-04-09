from django.contrib import admin
from django.urls import path
from Doctor import views

urlpatterns = [
    path('Ddashboard/', views.doctor_dashboard,name='dash'),
    path('Dpatients/',views.Patients,name='Pt'),
    path('Ddoctors/',views.Doctors,name='Dc'),
    path('Dstaffs/',views.Staffs,name='St'),
    path('Doctor_MR_S/',views.MRlist,name='DMRS'),
    path('edit-ownapp/<str:Aid>/',views.AppEdit,name='OAL'),
    path('update-ownapp/<str:Aid>/',views.AppUpdate,name='OAU'),
    path('Register_DMR/', views.D_MR,name='RDMR'),
    path('edit-dmr/<str:Mid>/',views.D_MREdit,name='EDMR'),
    path('update-dmr/<str:Mid>/',views.D_MRUpdate,name='UDMR'),
    path('Dself/',views.own,name='own'),
    path('eodoctor/<str:Doctor_email>/',views.ownedit,name='ownedit'),
    path('uodoctor/<str:Doctor_email>/',views.ownupdate,name='ownupdate'),
]
