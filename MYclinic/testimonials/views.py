from django.shortcuts import render, redirect
from django.views import View
from .models import Testimonial
from .forms import TestimonialForm
from django.contrib import messages

class TestimonialsView(View):
    form_class = TestimonialForm
    
    def get(self, request):
        return render(request, 'testimonials/testimonials.html', {'form': self.form_class()})
    
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            try:
                form.save()
                messages.success(request, 'نظر شما با موفقیت ثبت شد و پس از بررسی منتشر خواهد شد.')
                return redirect('home:home')
            except Exception as e:
                messages.error(request, 'خطا در ثبت نظر. لطفاً مجدداً تلاش کنید.')
                return render(request, 'testimonials/testimonials.html', {'form': form})
        else:
            messages.error(request, 'لطفاً تمام فیلدها را به درستی پر کنید.')
            return render(request, 'testimonials/testimonials.html', {'form': form})
