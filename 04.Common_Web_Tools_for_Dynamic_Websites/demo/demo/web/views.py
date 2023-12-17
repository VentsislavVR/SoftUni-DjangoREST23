import random

from django.contrib.auth import get_user_model
from django.shortcuts import render
from django.utils import cache
from django.core.cache import cache

UserModel = get_user_model()


# Create your views here.


# @cache.cache_page(10)
def index(request):
    if not cache.get('users'):
        users = cache.set('users', UserModel.objects.all(), 30)

    users = cache.get('users')

    context = {

        'count': random.randint(0, 1000000000),
        'users': users,

    }
    return render(request,
                  'index.html',
                  context)
