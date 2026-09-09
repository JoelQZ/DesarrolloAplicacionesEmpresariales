from django.urls import path

from .views import pizza_create, pizza_list


urlpatterns = [
    path('', pizza_list, name='pizza_list'),
    path('create/', pizza_create, name='pizza_create'),
]