from django.db import models

class Image(models.Model):
    CATEGORY_CHOICES = [
        ('waiting-room', 'سالن انتظار'),
        ('office', 'اتاق مطالعه'),
        ('equipment', 'تجهیزات'),
        ('exterior', 'نمای بیرونی'),
    ]
    
    title = models.CharField(max_length=100, null=True, blank=True)
    image = models.ImageField(upload_to='gallery/')
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='office')
    description = models.TextField(max_length=200, blank=True, null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title if self.title else f"Image {self.id}"