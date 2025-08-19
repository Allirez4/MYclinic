from django.urls import path
from . import views
app_name = 'home'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),  # Home page
    path('services/', views.ServicesView.as_view(), name='services'),  # Services page
]
