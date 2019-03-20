from django.urls import path
from . import views
urlpatterns = [
    path('', views.drf_client, name='drf_client' ),
]
