from django.db import models
from django.contrib.auth.models import AbstractUser


class Company(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField()

    def __str__(self):
        return self.name


class User(AbstractUser):
    class Role(models.TextChoices):
        SUPERUSER = "SUPERUSER", 'SuperUser'
        COMPANY_ADMIN = "COMPANY_ADMIN", 'CompanyAdmin'
        SHIFT_MANAGER = "SHIFT_MANAGER", 'ShiftManager'
        EMPLOYEE = "EMPLOYEE", 'Employee'

    base_role = Role.SUPERUSER
    role = models.CharField(max_length=50, choices=Role.choices)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, null=True)

    def save(self, *args, **kwargs):
        if not self.pk:
            self.role = self.base_role
        return super().save(*args, **kwargs)



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
