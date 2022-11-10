from django.shortcuts import render,HttpResponse,redirect
from . import forms
from .models import Patient,Doctor,Receptionist,Appointment,HR,Prescription
from django.db import connection,transaction
from django.http import JsonResponse
# Create your views here.

cursor=connection.cursor()

def base(request):
    return render(request,'base.html')

def home(request):
    return render(request,'home.html')

def addPatient(request):
    Patient=forms.Patientform()
    if request.method=="POST":
        Patient=forms.Patientform(request.POST,request.FILES)
        if Patient.is_valid():
            try:
                Patient.save(commit=True)
                return redirect("/home")
                print("saved")
            except:
                return HttpResponse("Error")
        else:
            Patient=forms.Patientform()
    return render(request,'signup.html',{"Patient":Patient})

def login(request):
    return render(request,'login.html')

def ContactUs(request):
    return render(request,'contactus.html')

def doLogin(request):
    if request.method=="POST":
        userId=request.POST.get('userId','')
        passwd=request.POST.get('password','')
        utype=request.POST.get('type','')
        print("user=",userId,"pass=",passwd)
        if utype=="user":
            for p in Patient.objects.raw('select * from Patient where patientName="%s" and patientPassword="%s"'%(userId,passwd)):
                p=Patient.objects.get(patientName=userId)
                if p.patientName==userId:
                    request.session['userId']=userId
                    return render(request, 'index.html',{'success':'Welcome '+p.patientName})
            else:
                return render(request,'login.html',{'failure':'login failed!! try again'})
        elif utype=="Doctor":
            for d in Doctor.objects.raw('select * from Doctor where doctorName="%s" and doctorPassword="%s" ' %(userId,passwd)):
                d=Doctor.objects.get(doctorName=userId)
                if d.doctorName==userId:
                    request.session['doctorId']=userId
                    return render(request,'index.html',{'success':'Welcome '+d.doctorName})
            else:
                return render(request,'login.html',{'failure':'login failed !! try again'})
        elif utype=="Receptionist":
            for r in Receptionist.objects.raw('select * from Receptionist where ReceptionistName="%s" and ReceptionistPassword="%s" ' %(userId,passwd)):
                r=Receptionist.objects.get(ReceptionistName=userId)
                if r.ReceptionistName==userId:
                    request.session['ReceptionistId']=userId
                    return render(request,'index.html',{'success':'Welcome '+r.ReceptionistName})
            else:
                return render(request,'login.html',{'failure':'login failed !! try again'})
        elif utype=="HR":
            for h in HR.objects.raw('select * from HR where hrName="%s" and hrPassword="%s" ' %(userId,passwd)):
                h=HR.objects.get(hrName=userId)
                if h.hrName==userId:
                    request.session['hrId']=userId
                    return render(request,'index.html',{'success':'Welcome '+h.hrName})
            else:
                return render(request,'login.html',{'failure':'login failed !! try again'})
        
        
    else:
        return render(request,'login.html')
      
def addAppointment(request):
    Appoint=forms.Appointmentform()
    if request.method=="POST":
        Appoint=forms.Appointmentform(request.POST,request.FILES)
        if Appoint.is_valid():
            try:
                Appoint.save(commit=True)
                return redirect("/appointment")
                print("saved")
            except:
                return HttpResponse("Error")
        else:
            Appoint=forms.Appointmentform()
    return render(request,'addappoinment.html',{"Appoint":Appoint})

def appointment(request):
    allappointments=Appointment.objects.all()
    return render(request, "appointment.html", {"Appoint":allappointments})

def prescription(request):
    allpres=Prescription.objects.all()
#    for i in Prescription.objects.raw('select * from Prescription where patient_name="%s" ' % (request.session['userId'])):
#        print(i.patient_name)
#    allpres=Prescription.objects.raw('select * from Prescription where patient_name="%s" ' % (request.session['userId']))
    return render(request,"prescription.html",{"prescrip":allpres})

def addDoctor(request):
    Doct=forms.Doctorform()
    if request.method=="POST":
        Doct=forms.Doctorform(request.POST,request.FILES)
        if Doct.is_valid():
            try:
                Doct.save(commit=True)
                return redirect("/doctor")
                print("saved")
            except:
                return HttpResponse("Error")
        else:
            Doct=forms.Doctorform()
    return render(request,'adddoctor.html',{"Doct":Doct})

def doctor(request):
    alldoctors=Doctor.objects.all()
    return render(request, "doctor.html", {"Doct":alldoctors})

def addReceptionist(request):
    recep=forms.Receptionistform()
    if request.method=="POST":
        recep=forms.Receptionistform(request.POST,request.FILES)
        if recep.is_valid():
            try:
                recep.save(commit=True)
                return redirect("/receptionist")
                print("saved")
            except:
                return HttpResponse("Error")
        else:
            recep=forms.Receptionistform()
    return render(request,'addreceptionist.html',{"recep":recep})

def receptionist(request):
    allreceptionist=Receptionist.objects.all()
    return render(request, "receptionist.html", {"recep":allreceptionist})

def details(request):
    alldoctors=Doctor.objects.all()
    allpatients=Patient.objects.all()
    return render(request, "details.html", {"Doct":alldoctors,"pat":allpatients})

def logout(request):
    session_keys=list(request.session.keys())
    for key in session_keys:
        del request.session[key]
    return render(request,'index.html',{"success":'Logged out successfully..!!!'})


def dappointment(request):
    alldoctors=Doctor.objects.all()
    allpatients=Patient.objects.all()
    allapointments=Appointment.objects.all()
#   allapointments=Appointment.objects.raw('select * from Appointment where doctorname="%s"' % (request.session['doctorId']))
    return render(request,'dappointment.html',{"Doct":alldoctors,"pat":allpatients,"apt":allapointments})

def updaterecp(request,recepid):
    data = Receptionist.objects.get(ReceptionistId=recepid)
    if request.method == "POST":
        rdata = forms.Receptionistform(request.POST,instance=data)
        print(rdata)
        if rdata.is_valid():
            print("hello")
            rdata.save()
            return redirect("/receptionist")
    return render(request, "updatereceptionist.html", {"recp": data})

def deleterecp(request,recpid):
    data = Receptionist.objects.get(ReceptionistId=recpid)
    data.delete()
    return redirect("/receptionist")


def updatedoct(request,doctid):
    data = Doctor.objects.get(doctorId=doctid)
    if request.method == "POST":
        ddata = forms.Doctorform(request.POST,instance=data)
        print(ddata)
        if ddata.is_valid():
            print("hello")
            ddata.save()
            return redirect("/doctor")
    return render(request, "updatedoct.html", {"doct": data})

def deletedoct(request,doctid):
    data = Doctor.objects.get(doctorId=doctid)
    data.delete()
    return redirect("/doctor")

def updateappointment(request,aptid):
    data = Appointment.objects.get(PatId=aptid)
    if request.method == "POST":
        adata = forms.Appointmentform(request.POST,instance=data)
        print(adata)
        if adata.is_valid():
            print("hello")
            adata.save()
            return redirect("/appointment")
    return render(request, "updateappointment.html", {"apt": data})

def deletedapt(request,aptid):
    data = Appointment.objects.get(PatId=aptid)
    data.delete()
    return redirect("/appointment")



def addPrescription(request):
    prescrip=forms.Prescriptionform()
    if request.method=="POST":
        prescrip=forms.Prescriptionform(request.POST,request.FILES)
        if prescrip.is_valid():
            try:
                prescrip.save(commit=True)
                return redirect("/prescription")
                print("saved")
            except:
                return HttpResponse("Error")
        else:
            prescrip=forms.Prescriptionform()
    return render(request,'addprescription.html',{"prescrip":prescrip})


def payment(request):
    ptnme=Patient.objects.raw('select * from Patient where patientName="%s" ' % (request.session['userId']))
    return render(request,'payment.html',{"ptnme":ptnme})

def pay(request):
    ptnme=Patient.objects.raw('select * from Patient where patientName="%s" ' % (request.session['userId']))
    return render(request,'pay.html',{"ptnme":ptnme})