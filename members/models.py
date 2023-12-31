from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=255)
    username = None
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []


class Company(models.Model):
    name = models.CharField(max_length=50, unique=True)
    contact = models.ForeignKey('User', null=True, blank=True, on_delete=models.CASCADE)
    description = models.TextField()

    def __str__(self):
        return self.name


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
    sector = models.ManyToManyField(Sector, blank=True)
    user = models.ForeignKey('User', on_delete=models.CASCADE)
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
    name = models.CharField(max_length=30, null=True, blank=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    sector = models.ManyToManyField(Sector)
