from django.contrib import admin
from django.urls import path
from Staff import views

urlpatterns = [
    path('Sdashboard/', views.staff_dashboard,name='Sdash'),
    path('Ptlist/', views.SPatients,name='Ptlist'),
    path('Dtlist/', views.SDoctors,name='Dtlist'),
    path('Stlist/', views.SStaffs,name='Stlist'),
    path('SMR_list/',views.SMR_list,name='SMRlist'),
    path('Sself/',views.Sown,name='Sown'),
    path('Sedit/<str:Staff_email>/',views.Sownedit,name='Sownedit'),
    path('Supdate/<str:Staff_email>/',views.Sownupdate,name='Sownupdate'),
    
]