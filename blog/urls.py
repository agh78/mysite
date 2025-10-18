from django.urls import path
from .views import blog_home_view, blog_single_view
from django.conf import settings
from django.conf.urls.static import static

app_name = 'blog'

urlpatterns = [
    path('', blog_home_view, name='home'),
    path('single', blog_single_view, name='single'),
]

# add static and media to url patterns
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
