from django.contrib.auth.decorators import user_passes_test
from django.http import JsonResponse

from members.models import Employee


def admin_permission_required(view_func):
    def _wrapped_view(request, *args, **kwargs):
        if Employee.objects.get(user=request.user) and Employee.objects.get(
                user=request.user).role == Employee.Role.COMPANY_ADMIN:
            return view_func(request, *args, **kwargs)
        else:

            return JsonResponse({'status': 'error', 'message': 'Unauthorized', 'reason': 'inviter not authorized for this action'},
                                status=401)

    return _wrapped_view
