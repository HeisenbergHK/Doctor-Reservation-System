from django.db import models


# Create your models here
class Doctor(models.Model):
    first_name = models.CharField(max_length=100, default=None)
    last_name = models.CharField(max_length=100, default=None)
    national_id = models.CharField(max_length=10, default=None, null=False, unique=True)
    phone_number = models.CharField(max_length=11, default=None)
    email = models.EmailField(blank=True, null=True)
    hired_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Patient(models.Model):
    first_name = models.CharField(max_length=100, default=None)
    last_name = models.CharField(max_length=100, default=None)
    national_id = models.CharField(max_length=10, default=None, null=False, unique=True)
    phone_number = models.CharField(max_length=11, default=None)
    email = models.EmailField(blank=True, null=True)
    register_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Reserve(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()

    def __str__(self):
        return f'{self.patient} has a reservation with Dr.{self.doctor} at {self.date}, {self.time}'
