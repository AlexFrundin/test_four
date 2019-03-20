#urls of profiles_app
from django.urls import path
from . import views

urlpatterns = [
    path('', views.start_profile, name='start_profile'),
    path('<str:name>', views.profiles, name='profiles'),
]
