from django.contrib import admin

# Register your models here.

from .models import Artwork, Review, Tag

admin.site.register(Artwork)
admin.site.register(Review)
admin.site.register(Tag)