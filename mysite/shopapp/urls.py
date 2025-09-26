from django.urls import path
from .views import shop_index, users_groups

app_name = 'shopapp'

urlpatterns = [
    path('', shop_index, name='shop_index'),
    path('users_groups/', users_groups, name='users_groups'),
]