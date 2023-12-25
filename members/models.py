from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager


class Company(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField()

    def __str__(self):
        return self.name


# class UserManager(BaseUserManager):
#     def get_queryset(self, user_role, *args, **kwargs):
#         results = super().get_queryset(*args, **kwargs)
#         return results.filter(role=user_role)


class User(AbstractUser):
    class Role(models.TextChoices):
        SUPERUSER = "SUPERUSER", 'SuperUser'
        COMPANY_ADMIN = "COMPANY_ADMIN", 'CompanyAdmin'
        SHIFT_MANAGER = "SHIFT_MANAGER", 'ShiftManager'
        EMPLOYEE = "EMPLOYEE", 'Employee'

    base_role = Role.SUPERUSER
    role = models.CharField(max_length=50, choices=Role.choices)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, default=1)
    productivity_rate = models.SmallIntegerField(default=1, null=True, blank=True)
    phone_number = models.CharField(max_length=10, null=True, blank=True)

    def save(self, *args, **kwargs):
        self.role = self.base_role
        return super().save(*args, **kwargs)


# class UserManager(BaseUserManager):
#     def get_queryset(self, *args, **kwargs):
#         results = super().get_queryset(*args, **kwargs)
#         return results.filter(role=User.Role.EMPLOYEE)


class Employee(User):
    base_role = User.Role.EMPLOYEE

    class Meta:
        proxy = True


class ShiftManager(User):
    base_role = User.Role.SHIFT_MANAGER

    class Meta:
        proxy = True


class CompanyAdmin(User):
    base_role = User.Role.COMPANY_ADMIN

    class Meta:
        proxy = True


class Attendance(models.Model):
    attendee = models.ForeignKey(User, on_delete=models.CASCADE)
    start_time = models.DateTimeField(null=True, blank=True)
    end_time = models.DateTimeField(null=True, blank=True)

