from django.contrib import admin
from .models import Testimonial

@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('firstname', 'lastname', 'phonenumber', 'is_verified', 'created_at')
    readonly_fields = ('created_at',)
    search_fields = ('firstname', 'lastname', 'phonenumber')
    list_filter = ('is_verified',)
