
from django.urls import path

from management.views import new_employee, new_attendance

urlpatterns = [
    path('new_employee/<str:company_name>/', new_employee, name='new_employee'),
    path('new_attendance/<str:company_name>/', new_attendance, name='new_attendance'),
]
