from django.urls import path

from drf_demos.api.views import AuthorsApiView, AuthorsView

urlpatterns = (
    path('authors/',AuthorsApiView.as_view(),name='api_list_authors'),
    path('authors-ssr/',AuthorsView.as_view(),name='list_authors'),
)