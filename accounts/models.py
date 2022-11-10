from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone
User = get_user_model()

# Create your models here.
class Patient(models.Model):
    patientId=models.AutoField(primary_key=True)
    patientName= models.CharField(max_length=30)
    patientEmail= models.EmailField()
    patientPassword= models.CharField(max_length=30)
    patientContact= models.CharField(max_length=30)
    patientAddress= models.CharField(max_length=50)
    patientGender=models.CharField(max_length=20)
    patientAge=models.IntegerField()


    class Meta:
        db_table="Patient"

class Receptionist(models.Model):
    ReceptionistId=models.AutoField(primary_key=True)
    ReceptionistName=models.CharField(max_length=10)
    ReceptionistEmail= models.EmailField()
    ReceptionistContact= models.CharField(max_length=30)
    ReceptionistAddress= models.CharField(max_length=50)
    ReceptionistGender=models.CharField(max_length=20)
    ReceptionistAge=models.IntegerField()
    Receptionistsalary=models.CharField(max_length=20)
    ReceptionistPassword=models.CharField(max_length=10)

    class Meta:
        db_table="Receptionist"




class Doctor(models.Model):
    doctorId=models.AutoField(primary_key=True)
    doctorName=models.CharField(max_length=10)
    doctorEmail= models.EmailField()
    doctorContact= models.CharField(max_length=30)
    doctorGender=models.CharField(max_length=20)
    doctorAge=models.IntegerField()
    doctorsalary=models.CharField(max_length=20)
    doctorAddress= models.CharField(max_length=50)
    doctorPassword=models.CharField(max_length=10)

    class Meta:
        db_table="Doctor"

class HR(models.Model):
    hrId=models.AutoField(primary_key=True)
    hrName=models.CharField(max_length=10)
    hrPassword=models.CharField(max_length=10)

    class Meta:
        db_table="HR"


class Appointment(models.Model):
    AppointmentId= models.AutoField(primary_key=True)
    date = models.DateField()
    time = models.TimeField()
    status = models.CharField(choices=[('Pending','Pending'),('Completed', 'Completed')], max_length=60)
    doctorname= models.CharField(choices=[('Uma','Uma'),('kumar', 'kumar')], max_length=60)
    PatId = models.IntegerField()
    DoctId = models.IntegerField()

    class Meta:
        db_table="Appointment"  

class Prescription(models.Model):
    PrescriptionId= models.AutoField(primary_key=True)
    date = models.DateField()
    symptoms = models.CharField(max_length=20)
    discription=models.CharField(max_length=50)
    medicine=models.CharField(max_length=20)
    treatement=models.CharField(max_length=20)
    patient_name=models.CharField(max_length=10)

    class Meta:
        db_table="Prescription"  