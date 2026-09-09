from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('pizza/', include('pizza.urls')),
    path('order/', include('order.urls')),
]
