from django.db import models

class Appointment(models.Model):
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    appointment_datetime = models.DateTimeField()
    is_paid = models.BooleanField(default=False)  # بعد از پرداخت میشه 
    authority = models.CharField(max_length=100,blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.appointment_datetime.strftime('%Y-%m-%d %H:%M')}"
