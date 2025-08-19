from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Testimonial(models.Model):
    firstname=models.CharField(max_length=50,)
    lastname=models.CharField(max_length=50,)
    phonenumber=models.CharField(max_length=15,)
    comment=models.TextField()
    is_verified=models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)
    rating=models.PositiveIntegerField(default=5,validators=[MaxValueValidator(5),MinValueValidator(1)])

    def __str__(self):
        return f"{self.firstname} {self.lastname} - {self.phonenumber} - {self.created_at}"
