from django.urls import path
from . import views


urlpatterns = [
    path('panel', views.PanelView.as_view()),
    path('authorized', views.AuthorizedView.as_view()),
    path('panel/<int:pk>', views.PanelListView.as_view()),
]