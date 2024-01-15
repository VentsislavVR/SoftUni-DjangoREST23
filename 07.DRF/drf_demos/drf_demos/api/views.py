# from django.shortcuts import render
# from rest_framework.decorators import api_view

from rest_framework import generics as api_views, serializers

from drf_demos.api.models import Author


# Create your views here.
# @api_view
# def rest_view(request):
#     return render(request, 'index.html')

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'


class AuthorsApiView(api_views.ListAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
