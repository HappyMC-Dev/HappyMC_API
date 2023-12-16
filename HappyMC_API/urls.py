from django.urls import path
from django.views.generic import TemplateView

from .views import Image
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('img', Image.as_view(), name='img'),
    path('img-phone', Image.as_view(), name='img-phone'),
    path('', TemplateView.as_view(template_name='index.html'), name='index'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)