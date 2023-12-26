
from django.urls import path

from management.views import new_employee

urlpatterns = [
    path('new_employee/', new_employee, name='new_employee')

]
