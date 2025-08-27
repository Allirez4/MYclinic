from django.contrib import admin
from .models import Appointment
import jdatetime

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ['name', 'last_name', 'phone_number', 'get_jalali_appointment_date', 'get_appointment_time', 'created_jalali', 'is_paid']
    list_filter = ['is_paid', 'appointment_datetime', 'created_at']
    search_fields = ['name', 'last_name', 'phone_number']
    list_editable = ['is_paid']
    readonly_fields = ['created_at', 'get_jalali_appointment_date', 'created_jalali']
    ordering = ['-appointment_datetime']
    date_hierarchy = 'appointment_datetime'
    
    def get_jalali_appointment_date(self, obj):
        if obj.appointment_datetime:
            jalali_date = jdatetime.date.fromgregorian(date=obj.appointment_datetime.date())
            
            # استفاده از ماه‌های فارسی
            months = {
                "Farvardin": "فروردین",
                "Ordibehesht": "اردیبهشت",
                "Khordad": "خرداد",
                "Tir": "تیر",
                "Mordad": "مرداد",
                "Shahrivar": "شهریور",
                "Mehr": "مهر",
                "Aban": "آبان",
                "Azar": "آذر",
                "Dey": "دی",
                "Bahman": "بهمن",
                "Esfand": "اسفند"
            }
            
            day = jalali_date.day
            month = jalali_date.month
            year = jalali_date.year
            month_name = list(months.values())[month-1]
            
            # تبدیل اعداد به فارسی
            day_str = str(day).replace("0", "۰").replace("1", "۱").replace("2", "۲").replace("3", "۳").replace("4", "۴").replace("5", "۵").replace("6", "۶").replace("7", "۷").replace("8", "۸").replace("9", "۹")
            year_str = str(year).replace("0", "۰").replace("1", "۱").replace("2", "۲").replace("3", "۳").replace("4", "۴").replace("5", "۵").replace("6", "۶").replace("7", "۷").replace("8", "۸").replace("9", "۹")
            
            return f"{day_str} {month_name} {year_str}"
        return "-"
    get_jalali_appointment_date.short_description = 'تاریخ نوبت (شمسی)'
    
    def get_appointment_time(self, obj):
        if obj.appointment_datetime:
            time_str = obj.appointment_datetime.strftime("%H:%M")
            # تبدیل اعداد به فارسی
            return time_str.replace("0", "۰").replace("1", "۱").replace("2", "۲").replace("3", "۳").replace("4", "۴").replace("5", "۵").replace("6", "۶").replace("7", "۷").replace("8", "۸").replace("9", "۹")
        return "-"
    get_appointment_time.short_description = 'ساعت نوبت'
    
    def created_jalali(self, obj):
        if obj.created_at:
            jalali_date = jdatetime.date.fromgregorian(date=obj.created_at.date())
            # استفاده از ماه‌های فارسی
            months = {
                "Farvardin": "فروردین",
                "Ordibehesht": "اردیبهشت",
                "Khordad": "خرداد",
                "Tir": "تیر",
                "Mordad": "مرداد",
                "Shahrivar": "شهریور",
                "Mehr": "مهر",
                "Aban": "آبان",
                "Azar": "آذر",
                "Dey": "دی",
                "Bahman": "بهمن",
                "Esfand": "اسفند"
            }
            
            day = jalali_date.day
            month = jalali_date.month
            year = jalali_date.year
            month_name = list(months.values())[month-1]
            
            # تبدیل اعداد به فارسی
            day_str = str(day).replace("0", "۰").replace("1", "۱").replace("2", "۲").replace("3", "۳").replace("4", "۴").replace("5", "۵").replace("6", "۶").replace("7", "۷").replace("8", "۸").replace("9", "۹")
            year_str = str(year).replace("0", "۰").replace("1", "۱").replace("2", "۲").replace("3", "۳").replace("4", "۴").replace("5", "۵").replace("6", "۶").replace("7", "۷").replace("8", "۸").replace("9", "۹")
            
            return f"{day_str} {month_name} {year_str}"
        return "-"
    created_jalali.short_description = 'تاریخ ثبت (شمسی)'

    fieldsets = (
        ('اطلاعات بیمار', {
            'fields': ('name', 'last_name', 'phone_number')
        }),
        ('جزئیات نوبت', {
            'fields': ('appointment_datetime', 'is_paid')
        }),
        ('اطلاعات سیستمی', {
            'fields': ('created_at', 'created_jalali', 'authority'),
            'classes': ('collapse',)
        }),
    )

