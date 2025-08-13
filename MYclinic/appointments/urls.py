from django.urls import path
from . import views
app_name = 'appointments'
urlpatterns = [
    path('book/', views.MakingAppointmentView.as_view(), name='book_appointment'),
    path('paying/', views.PayingAppointmentView.as_view(), name='pay_appointment'),
    path('verify/', views.PayingAppointmentView.as_view(), name='verify_appointment')
]