from django.urls import path
from . import views

urlpatterns = [
    path('', views.artworks, name="artworks"),
    path('artwork/<str:pk>/', views.artwork, name="artwork"),
]
