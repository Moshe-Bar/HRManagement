import logging

from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.utils import json


# todo remove for production
@csrf_exempt  # For demonstration purposes only; use a more secure method in production
def register(request):
    if request.method == 'POST':
        # Parse JSON data from the request body
        data = json.loads(request.body.decode('utf-8'))

        # Create a UserCreationForm instance with JSON data
        form = UserCreationForm(data)

        if form.is_valid():
            user = form.save()
            login(request, user)

            # Return a JSON response indicating success
            return JsonResponse({'status': 'success', 'message': 'Registration successful'})

        # If form is not valid, return a JSON response with error details
        errors = form.errors.as_json()
        return JsonResponse({'status': 'error', 'errors': errors}, status=400)

    # If the request method is not POST, return a JSON response with an error
    return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=405)
