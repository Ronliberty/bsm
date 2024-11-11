from django.db import models
from django.conf import settings
class Project(models.Model):
    STATUS_CHOICES = [
        ('available', 'Available'),
        ('ongoing', 'Ongoing'),
        ('completed', 'Completed'),
    ]
    title = models.CharField(max_length=200)
    description = models.TextField()
    file = models.FileField(upload_to='project_files/', blank=True, null=True)
    link = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='available')
    assigned_to = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.title
