from django.http import HttpRequest
from django.shortcuts import render
from django.contrib.auth.models import Group
from .models import Product

# Create your views here.
def shop_index(request: HttpRequest):
    context = {
        'title': 'Shop Index',
        'products': Product.objects.all(),
    }
    return render(request, 'shopapp/shop_index.html', context=context)

def users_groups(request: HttpRequest):
    context = {
        'title': 'Users Groups',
        'groups': Group.objects.prefetch_related('permissions').all(),
    }
    return render(request, 'shopapp/users_groups.html', context=context)