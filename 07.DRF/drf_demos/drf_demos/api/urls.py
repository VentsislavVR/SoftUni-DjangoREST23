from django.urls import path

from drf_demos.api.views import AuthorsApiView

urlpatterns = (
    path('authors/',AuthorsApiView.as_view(),name='api_list_authors'),
)