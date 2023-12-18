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

    request.session['count'] = request.session.get('count', 0) + 1

    if not cache.get('users'):
        users = cache.set('users', UserModel.objects.all(), 30)

    users = cache.get('users')
    prev_tasks_id = request.session.get('prev_tasks', [])

    context = {

        # 'count': random.randint(0, 1000000000),
        'users': users,
        'count': request.session['count'],
        'tasks':Task.objects.all(),
        'prev_tasks': Task.objects.filter(pk__in=prev_tasks_id),

    }


    return render(request,
                  'index.html',
                  context)
def details_task(request,pk):
    task = Task.objects.filter(pk=pk).get()

    prev_tasks = request.session.get('prev_tasks',[])

    prev_tasks.append(task.pk)
    start_index = max(
        0,
        len(prev_tasks) - 3,
    )

    request.session['prev_tasks'] = prev_tasks[start_index:]
    print(request.session['prev_tasks'])

    return redirect('index')

def create_task(request):
    Task.objects.create(
        title=f'Title {random.randint(0, 10000)}',
    )

    return redirect('index')