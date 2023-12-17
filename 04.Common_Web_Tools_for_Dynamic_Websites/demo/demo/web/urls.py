from django.urls import path

from demo.web.views import index

urlpatterns = (
    path('', index,name='index'),
)