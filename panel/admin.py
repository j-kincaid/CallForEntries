from django.contrib import admin
from . import models

class PanelAdmin(admin.ModelAdmin):
    list_display = ('full_name',)

admin.site.register(models.Panel, PanelAdmin)