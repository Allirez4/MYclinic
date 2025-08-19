from django.urls import path
from . import views
app_name = 'testimonials'
urlpatterns = [
    path('testimonials/', views.TestimonialsView.as_view(), name='testimonials'),  # URL for the testimonials page
]