from django.contrib import admin
from .models import Image
from django.utils.html import format_html
@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):

    list_display = ("id", "title", "uploaded_at", "preview","category")

    def preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="100" height="70" style="object-fit:cover;" />', obj.image.url)
        return "No Image"
    
    preview.short_description = "Preview"