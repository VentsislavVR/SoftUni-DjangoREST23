import random

from django import views
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView

from Class_Based_Views.web.models import Employee


# Create your views here.
class IndexView(views.View):
    def get(self, request, *args, **kwargs):
        context = {
            'title': 'Bare View'
        }
        return render(request, 'index.html', context)

    def post(self, request, *args, ):
        pass


class IndexViewWithTemplate(TemplateView):
    template_name = 'index.html'
    extra_context = {'title': 'Template View'} # static context



    def get_context_data(self, **kwargs):
        context = super().extra_context(**kwargs)
        context['employees'] = Employee.objects.all()

        return context #dynamic context


# Used in Django Rest
# def put(self, request, *args, **kwargs):
#     ...

# class IndexView():
#     def __init__(self):
#         self.values = [
#             random.randint(1,15)
#         ]
#     @classmethod
#     def get_view(cls):
#         return cls().view
#     def view (self,request):
#         return HttpResponse(f'It works : {self.values}')
#
#
# class Index2View(IndexView):
#     def __init__(self):
#         super().__init__()
#         self.values.append(random.randint(15,30))
