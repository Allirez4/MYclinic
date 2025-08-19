from django.shortcuts import render
from django.views import View
from .models import Image  # Assuming you have a model for gallery images

class GalleryView(View):
    def get(self, request):
        # Get all images ordered by upload date (newest first)
        images = Image.objects.all().order_by('-uploaded_at')
        
        # Group images by category if needed (for future enhancement)
        context = {
            'images': images,
            'total_images': images.count(),
        }
        
        return render(request, 'gallery/gallery.html', context)
