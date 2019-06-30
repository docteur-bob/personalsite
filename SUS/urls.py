from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView
from SUS.views import SUShome

urlpatterns = [
    path('',SUShome.as_view()),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
