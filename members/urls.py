from django.urls import path

from .views import (
    register, login_view, test_logged_user,
    # Import other views as needed
)

urlpatterns = [
    # path('register', HomeView.as_view(), name='home'),
    # path('about/', AboutView.as_view(), name='about'),
    # path('contact/', ContactView.as_view(), name='contact'),
    path('register/', register, name='register'),
    path('login/', login_view, name='login'),
    path('session_test/', test_logged_user, name='session_test'),
    # Add other URL patterns as needed
]