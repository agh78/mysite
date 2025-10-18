from django.urls import path
from .views import About_view, Contact_view, Home_view
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', Home_view),
    path('about', About_view),
    path('contact', Contact_view)
]

# add static and media to url patterns
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
