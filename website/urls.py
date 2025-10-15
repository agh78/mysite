from django.urls import path
from .views import About_view, Contact_view, Home_view
urlpatterns = [
    path('', Home_view),
    path('About', About_view),
    path('Contact', Contact_view)
]
