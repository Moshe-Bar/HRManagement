from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager, User


class Company(models.Model):
    name = models.CharField(max_length=50, unique=True)
    contact = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    description = models.TextField()

    def __str__(self):
        return self.name


# class UserManager(BaseUserManager):
#     def get_queryset(self, user_role, *args, **kwargs):
#         results = super().get_queryset(*args, **kwargs)
#         return results.filter(role=user_role)


# class User(AbstractUser):
#     id = models.CharField(max_length=9, primary_key=True)
#     phone_number = models.CharField(max_length=10, null=True, blank=True)


class Sector(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)


class Employee(models.Model):
    class Role(models.TextChoices):
        COMPANY_ADMIN = "COMPANY_ADMIN", 'CompanyAdmin'
        SHIFT_MANAGER = "SHIFT_MANAGER", 'ShiftManager'
        EMPLOYEE = "EMPLOYEE", 'Employee'

    role = models.CharField(max_length=50, default='Employee', choices=Role.choices)
    productivity_rate = models.SmallIntegerField(default=1, null=True, blank=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    sector = models.ManyToManyField(Sector, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    active = models.BooleanField(default=False)

    class Meta:
        unique_together = ('company', 'user')

    def __str__(self):
        return self.user.username


class Attendance(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    sector = models.ManyToManyField(Sector)


class Shift(models.Model):
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    sector = models.ManyToManyField(Sector)
