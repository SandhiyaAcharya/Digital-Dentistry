from django import forms
from accounts.models import Patient,Appointment,Doctor,Receptionist,Prescription

class Patientform(forms.ModelForm):
    class Meta:
        model=Patient
        fields='__all__'

class Appointmentform(forms.ModelForm):
    class Meta:
        model=Appointment
        fields='__all__'

class Doctorform(forms.ModelForm):
    class Meta:
        model=Doctor
        fields='__all__'

class Receptionistform(forms.ModelForm):
    class Meta:
        model=Receptionist
        fields='__all__'

class Prescriptionform(forms.ModelForm):
    class Meta:
        model=Prescription
        fields='__all__'