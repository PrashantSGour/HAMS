from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    
    path('Adashboard/',views.Admin_dashboard,name='admin_dashboard'),
    path('patients_list/',views.Patient_list,name='Plist'),
    path('doctors_list/',views.Doctor_list,name='Dlist'),
    path('staff_list/',views.Staff_list,name='Slist'),
    path('MR_list/',views.MR_list,name='MRlist'),
    path('Feedback_list/',views.F_list,name='Flist'),
    path('Register_Doctor/', views.Register_doctor,name='RD'),
    path('Register_Staff/', views.Register_staff,name='RS'),
    path('Register_MR/', views.Register_MR,name='RMR'),
    path('deleteItem/<str:Aid>/',views.Adelete,name='deleteItemA'),
    path('delete-doctor/<str:doctor_email>/',views.Ddelete,name='deleteItemD'),
    path('deleteMR/<str:Mid>/',views.MRdelete,name='deleteItemMR'),
    path('deleteP/<str:patient_id>/',views.Pdelete,name='deleteItemP'),
    path('deleteS/<str:staff_id>/',views.Sdelete,name='deleteItemS'),
    path('deleteF/<str:Fid>/',views.Fdelete,name='deleteItemF'),
    path('edit-doctor/<str:doctor_email>/',views.DoctorEdit,name='Doctoredit'),
    path('update-doctor/<str:doctor_email>/',views.DoctorUpdate,name='Doctorupdate'),
    path('edit-patient/<str:patient_email>/',views.PatientEdit,name='PatientEdit'),
    path('update-patient/<str:patient_email>/',views.PatientUpdate,name='PatientUpdate'),
    path('edit-mr/<str:Mid>/',views.MREdit,name='MRedit'),
    path('update-mr/<str:Mid>/',views.MRUpdate,name='MRupdate'),
    path('edit-app/<str:Aid>/',views.AppEdit,name='Appedit'),
    path('update-app/<str:Aid>/',views.AppUpdate,name='Appupdate'),
    path('edit-staff/<str:staff_email>/',views.StaffEdit,name='Staffedit'),
    path('update-staff/<str:staff_email>/',views.StaffUpdate,name='Staffupdate'),
    path('edit-feedback/<str:Fid>/',views.FeedbackEdit,name='Feedbackedit'),
    path('update-feedback/<str:Fid>/',views.FUpdate,name='Feedbackupdate'),
]
