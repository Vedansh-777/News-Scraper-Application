# newsapp/urls.py
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import news_view

urlpatterns = [
    path('', news_view, name='news_view'),
]

# Serve static files during development
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

