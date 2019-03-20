from django.urls import path
from . import views

urlpatterns = [
path('', views.home, name='home'),
path('all', views.info, name='info'),
path('detail/<int:id>', views.detail, name='detail'),
]
#shop/
#shop/info
#shop/detail/<int:id>
