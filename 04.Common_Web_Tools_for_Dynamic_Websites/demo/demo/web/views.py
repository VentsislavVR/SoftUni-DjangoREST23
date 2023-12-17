import random

from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect
from django.utils import cache
from django.core.cache import cache

from demo.web.models import Task

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


def create_task(request):
    Task.objects.create(
        title=f'Title {random.randint(0, 10000)}',
    )

    return redirect('index')