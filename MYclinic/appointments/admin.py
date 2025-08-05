from django.contrib import admin
from .models import Appointment

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ['name', 'last_name', 'phone_number', 'appointment_datetime', 'is_paid', 'created_at']
    list_filter = ['is_paid', 'appointment_datetime', 'created_at']
    search_fields = ['name', 'last_name', 'phone_number']
    list_editable = ['is_paid']
    readonly_fields = ['created_at']
    ordering = ['-appointment_datetime']
    date_hierarchy = 'appointment_datetime'
    
    fieldsets = (
        ('Patient Information', {
            'fields': ('name', 'last_name', 'phone_number')
        }),
        ('Appointment Details', {
            'fields': ('appointment_datetime', 'is_paid')
        }),
        ('System Information', {
            'fields': ('created_at',),
            'classes': ('collapse',)
        }),
    )

