from django.contrib import admin
from . import models
# Register your models here.

# These models can be displayed and modified via the Django Admin interface. 
class ArtistAdmin(admin.ModelAdmin):
    list_display = ('full_name',)

admin.site.register(models.Artists, ArtistAdmin)