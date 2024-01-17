# from django.shortcuts import render
# from rest_framework.decorators import api_view
from time import sleep
from django.views import generic as views
from rest_framework import generics as api_views, serializers, permissions
from rest_framework.pagination import PageNumberPagination
from rest_framework import viewsets

from drf_demos.api.models import Author


class AuthorsView(views.ListView):
    queryset = Author.objects.all()
    template_name = 'authors.html'

    def get(self, request, *args, **kwargs):
        sleep(0)
        return super().get(request, *args, **kwargs)


# Create your views here.
# @api_view
# def rest_view(request):
#     return render(request, 'index.html')

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'


# author_serializer = AuthorSerializer(
#     instance=Author.objects.all(),
# )
# print(author_serializer.data)

# author_serializer_json = AuthorSerializer(
#     data={"id": 1,
#           "first_name": "Marli",
#           "last_name": "Racheva",
#           "followers_count": 0}
# )
# print(author_serializer_json.is_valid())
class CustomPageNumberPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'


class AuthorsApiViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()

    serializers_class = AuthorSerializer


class AuthorsApiView(api_views.ListCreateAPIView):
    queryset = Author.objects.order_by('first_name', 'last_name', 'followers_count', 'pk')
    serializer_class = AuthorSerializer
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
    )
    pagination_class = CustomPageNumberPagination

    def get(self, request, *args, **kwargs):
        print(request.session.get('count', None))
        request.session['count'] = 5
        print(request.user)
        return super().get(request, *args, **kwargs)
