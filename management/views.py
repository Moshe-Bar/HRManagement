import json
from json import JSONDecodeError

from django.contrib.auth.models import User
from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt

from management.permissions import admin_permission_required
from members.models import Employee


# todo authorization only for managers
# todo remove csrf decorator
@csrf_exempt  # For demonstration purposes only; use a more secure method in production
@login_required
@admin_permission_required
def new_employee(request, company_name):
    if request.method == 'POST':
        try:
            data = json.loads(request.body.decode('utf-8'))
            username = data['username']
            company = data['company']
            # not really need because the link is with the company name
        except (JSONDecodeError, KeyError):
            return JsonResponse({'error': 'Invalid JSON data'}, status=400)

        inviter = Employee.objects.get(user=request.user, company__name=company_name)

        user = User.objects.get(username=username)

        if not user:
            return JsonResponse({'status': 'error', 'message': 'Invalid username'}, status=400)
        try:
            em = Employee(role=Employee.Role.EMPLOYEE,
                          company=inviter.company,
                          user=user,
                          active=False)
            em.save()
        except Exception:
            return JsonResponse({'status': 'error', 'message': 'Can not create new employee'}, status=400)
        return JsonResponse({'status': 'success', 'message': 'New employee created', 'pk': em.pk}, status=200)

    return JsonResponse({'error': 'Invalid request method'}, status=405)
