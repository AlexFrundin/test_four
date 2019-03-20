from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('shop/', include('shop.urls')),
    path('', RedirectView.as_view(url='shop/')),
    path('profiles/', include('profiles.urls')),
    path('drf_client/', include('drf_client.urls')),

]

#shop/
#shop/info
#shop/detail/<int:id>
