from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required


@login_required
def get_attendance(request):
    data = {'key1': 'value1', 'key2': 'value2'}
    return JsonResponse(data)
