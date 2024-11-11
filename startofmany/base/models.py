from django.db import models

class HeroContent(models.Model):
    title = models.CharField(max_length=255)
    subtitle = models.TextField()
    cta_text = models.CharField(max_length=100)
    cta_link = models.URLField()

class GalleryItem(models.Model):
    video_url = models.URLField()
    video = models.FileField(upload_to='videos/', blank=True, null=True)

    def __str__(self):
        return f"Gallery Item: {self.video_url or self.video.name}"

class PricingPlan(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    features = models.TextField()  # Features separated by new lines

class AboutSection(models.Model):
    description = models.TextField()
    location = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    email = models.EmailField()

class ContactInfo(models.Model):
    address = models.TextField()
    phone = models.CharField(max_length=20)
    email = models.EmailField()
