from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from .models import Appointment
from .forms import AppointmentForm

class MakingAppointmentView(View):
    def get(self, request):
        form = AppointmentForm()
        return render(request, 'appointments/make_appointment.html', {'form': form})

    def post(self, request):
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save()
            messages.success(
                request, 
                f'نوبت شما با موفقیت ثبت شد! شماره تماس: {appointment.phone_number}'
            )
            return render(request, 'appointments/appointment_success.html', {'appointment': appointment})
        else:
            messages.error(
                request, 
                'خطا در ثبت نوبت! لطفاً اطلاعات وارد شده را بررسی کنید.'
            )
        return render(request, 'appointments/make_appointment.html', {'form': form})
