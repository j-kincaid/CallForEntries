from django.db import models

class Artists(models.Model):
    full_name = models.CharField(max_length=200)
    medium = models.TextField()
    bio = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
