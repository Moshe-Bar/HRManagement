from django.http import JsonResponse
from members.models import Employee


def admin_permission_required(view_func):
    def _wrapped_view(request, *args, **kwargs):
        employee = Employee.objects.get(user=request.user)
        if employee and employee.role == Employee.Role.COMPANY_ADMIN:
            return view_func(request, *args, **kwargs)
        else:

            return JsonResponse(
                {'status': 'error', 'message': 'Unauthorized', 'reason': 'inviter not authorized for this action'},
                status=401)

    return _wrapped_view


def shift_manager_permission_required(view_func):
    def _wrapped_view(request, *args, **kwargs):
        employee = Employee.objects.get(user=request.user)
        if employee and (employee.role == Employee.Role.SHIFT_MANAGER or employee.role == Employee.Role.COMPANY_ADMIN):
            return view_func(request, *args, **kwargs)
        else:

            return JsonResponse(
                {'status': 'error', 'message': 'Unauthorized', 'reason': 'inviter not authorized for this action'},
                status=401)

    return _wrapped_view
