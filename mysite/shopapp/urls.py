from django.urls import path
from .views import shop_index, users_groups, orders_list

app_name = 'shopapp'

urlpatterns = [
    path('', shop_index, name='shop_index'),
    path('users_groups/', users_groups, name='users_groups'),
    path('orders_list/', orders_list, name='orders_list'),
]