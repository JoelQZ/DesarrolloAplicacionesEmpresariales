from django.urls import path

from .views import order_create, order_list


urlpatterns = [
    path('', order_list, name='order_list'),
    path('create/', order_create, name='order_create'),
]