from django.forms import ModelForm
from django import forms
from .models import Appointment

class AppointmentForm(ModelForm):
    class Meta:
        model = Appointment
        fields = ['name', 'last_name', 'phone_number', 'appointment_datetime']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'نام خود را وارد کنید',
                'required': True,
                'style': 'direction: rtl; text-align: right;'
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'نام خانوادگی (اختیاری)',
                'style': 'direction: rtl; text-align: right;'
            }),
            'phone_number': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '09123456789',
                'pattern': '09[0-9]{9}',
                'required': True,
                'style': 'direction: ltr; text-align: left;'
            }),
            'appointment_datetime': forms.HiddenInput()
        }
        labels = {
            'name': 'نام',
            'last_name': 'نام خانوادگی',
            'phone_number': 'شماره تماس',
            'appointment_datetime': 'تاریخ و زمان نوبت'
        }
        error_messages = {
            'name': {
                'required': 'لطفاً نام خود را وارد کنید',
            },
            'phone_number': {
                'required': 'لطفاً شماره تماس خود را وارد کنید',
            },
            'appointment_datetime': {
                'required': 'لطفاً تاریخ و ساعت نوبت را انتخاب کنید',
            }
        }
