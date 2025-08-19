from django import forms
from django.forms import ModelForm, TextInput, Textarea
from .models import Testimonial

class TestimonialForm(ModelForm):
    class Meta:
        model = Testimonial
        fields = ['firstname', 'lastname', 'phonenumber', 'rating', 'comment']
        widgets = {
            'firstname': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'نام خود را وارد کنید...'
            }),
            'lastname': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'نام خانوادگی خود را وارد کنید...'
            }),
            'phonenumber': TextInput(attrs={
                'class': 'form-control',
                'placeholder': '09xxxxxxxxx',
                'pattern': '^09[0-9]{9}$'
            }),
            'rating': forms.Select(attrs={
                'class': 'form-control rating-select d-none',
                'id': 'rating-input'
            }),
            'comment': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'نظر خود را در مورد کیفیت خدمات، رفتار پرسنل و محیط مطب بنویسید...',
                'rows': 5
            }),
        }
        labels = {
            'firstname': 'نام',
            'lastname': 'نام خانوادگی',
            'phonenumber': 'شماره تلفن',
            'rating': 'امتیاز شما',
            'comment': 'نظر شما',
        }