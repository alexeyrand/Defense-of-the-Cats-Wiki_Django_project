from django.db import models

class Cat(models.Model):
    name = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    stats = models.TextField(blank=True)
    photo = models.ImageField(upload_to="photos/")
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)
