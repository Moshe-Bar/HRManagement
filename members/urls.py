from django.urls import path

from .views import (
    register,
    # Import other views as needed
)

urlpatterns = [
    # path('register', HomeView.as_view(), name='home'),
    # path('about/', AboutView.as_view(), name='about'),
    # path('contact/', ContactView.as_view(), name='contact'),
    path('register/', register, name='register'),
    # Add other URL patterns as needed
]