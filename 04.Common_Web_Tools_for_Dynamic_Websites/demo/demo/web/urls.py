from django.urls import path

from demo.web.views import index, create_task

urlpatterns = (
    path('', index,name='index'),
    path('create/', create_task,name='create_task'),
)