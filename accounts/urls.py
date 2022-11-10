from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.base),
    path('home/',views.home),
    path('signup/',views.addPatient),
    path('login/',views.login),
    path('payment/',views.payment),
    path('pay/',views.pay),
    path('doLogin',views.doLogin),
    path('contactus/',views.ContactUs),
    path('addappointment/',views.addAppointment),
    path('prescription/',views.prescription),
    path('addprescription/',views.addPrescription),
    path('appointment/',views.appointment),
    path('adddoctor/',views.addDoctor),
    path('doctor/',views.doctor),
    path('addreceptionist/',views.addReceptionist),
    path('receptionist/',views.receptionist),
    path('logout/',views.logout),
    path('details/',views.details),
    path('dappointment/',views.dappointment),
    path('updatereceptionist/<int:recepid>',views.updaterecp),
    path('deleterecp/<int:recpid>',views.deleterecp),
    path('updatedoct/<int:doctid>',views.updatedoct),
    path('deletedoct/<int:doctid>',views.deletedoct),
    path('updateappointment/<int:aptid>',views.updateappointment),
    path('deletedapt/<int:aptid>',views.deletedapt),

]
