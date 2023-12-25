
from django.urls import path, include

from management.views import get_attendance

urlpatterns = [
    path('attendance/', get_attendance, name='attendance')

]
