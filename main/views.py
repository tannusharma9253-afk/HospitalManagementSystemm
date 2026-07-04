from django.shortcuts import render, redirect
from .models import Doctor, Patient, Appointment
from .forms import AppointmentForm

def home(request):
    doctors = Doctor.objects.all()
    return render(request, 'index.html', {'doctors': doctors})


def book_appointment(request):
    form = AppointmentForm()
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    return render(request, 'appointment.html', {'form': form})