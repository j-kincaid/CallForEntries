from django.db import models

# Create your models here.
class Panel(models.Model):
    full_name = models.CharField(max_length=200)
    medium = models.TextField()
    bio = models.TextField()