
from django.urls import path

from management.views import new_employee

urlpatterns = [
    path('new_employee/<str:company_name>/', new_employee, name='new_employee')

]
