from django.db import models
from users.models import CustomUser

class Service(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    file = models.FileField(upload_to='uploads/')  # for generic file uploads
    image = models.ImageField(upload_to='images/', null=True, blank=True)  # for image uploads

    def __str__(self):
        return self.title

class ServiceRequest(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, default=1)  # Change to ForeignKey
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='requests')
    request_description = models.TextField()
    request_file = models.FileField(upload_to='requests/', blank=True, null=True)

    def __str__(self):
        return f"Request for {self.service.title}"