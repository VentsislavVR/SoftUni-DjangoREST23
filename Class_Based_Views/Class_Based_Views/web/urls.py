from django.urls import path

from Class_Based_Views.web.views import IndexView, IndexViewWithTemplate

urlpatterns = (
    path('',IndexViewWithTemplate.as_view()),
)