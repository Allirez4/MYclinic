from django.shortcuts import render
from django.views import View
from testimonials.models import Testimonial
class HomeView(View):
    def get(self, request):
        testimonials = Testimonial.objects.filter(is_verified=True).order_by('-created_at')[:5]  # Fetch latest 5 verified testimonials
        return render(request, 'home/home.html', {'testimonials': testimonials})
class ServicesView(View):
    def get(self, request):
        return render(request, 'home/services.html')
