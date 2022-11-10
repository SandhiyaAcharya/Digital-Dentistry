from django.contrib import admin
from .models import Patient,Doctor,Appointment,Receptionist,HR,Prescription

# Register your models here.
admin.site.register(Patient)
admin.site.register(Doctor)
admin.site.register(Appointment)
admin.site.register(Receptionist)
admin.site.register(HR)
admin.site.register(Prescription)
