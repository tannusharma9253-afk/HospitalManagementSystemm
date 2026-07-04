from django.contrib import admin
from .models import Doctor, Patient, Appointment

@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'specialization', 'phone', 'email')


@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'age', 'gender', 'phone')


@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'patient', 'doctor', 'date', 'time')