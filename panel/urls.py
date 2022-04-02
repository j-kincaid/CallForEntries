from django.urls import path
from . import views


urlpatterns = [
    path('panel/<int:pk>', views.PanelListView.as_view(), name="panel.list"),
    path('panel/<int:pk>', views.PanelDetailView.as_view(), name="panel.detail"),
    path('panel/new', views.PanelCreateView.as_view(), name="panel.new"),
    path('panel/<int:pk>/edit', views.PanelUpdateView.as_view(), name="panel.update"),
]