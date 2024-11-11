# bookappointment/models.py
from django.db import models


class Appointment(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('canceled', 'Canceled'),
    ]

    date = models.DateField()
    time = models.TimeField()
    description = models.TextField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Appointment on {self.date} at {self.time}"



class MeetingRequest(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    date = models.DateField()
    time = models.TimeField()
    message = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.date} at {self.time}"


