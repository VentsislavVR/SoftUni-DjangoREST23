import random

from django import views
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView

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
        #Get supers context
        context = super().get_context_data(**kwargs)
        # Add specific view stuff
        context['employees'] = Employee.objects.all()
        # Return the ready to use context
        return context #dynamic context
class IndexViewWithListView(ListView):
    context_object_name = 'employees' # rename 'object_list' in templates

    model = Employee
    template_name = 'index.html'
    extra_context = {'title': 'List View'}

    # ordering = ['first_name', 'last_name']
    def get(self,*args,**kwargs):
        return super().get(*args,**kwargs) #  TODO
    def get_queryset(self):
        queryset = super().get_queryset()

        pattern = self.__get_pattern()

        if pattern:
            queryset = queryset.filter(first_name__icontains=pattern.lower())

        return queryset
    def __get_pattern(self):


        return self.request.GET.get('pattern',None)

class EmployeeDetailView(DetailView):
    context_object_name = 'employees' # rename 'object'
    model = Employee
    template_name = 'employees/details.html'

class EmployeeCreateView(CreateView):
    template_name =  'employees/create.html'
    model = Employee
    fields = '__all__'
    # success_url = '/' # static

    # dynamic
    def get_success_url(self):

        return reverse('employee details',
                       kwargs={'pk':self.object.pk
                               })

    # form_class = Employee

    # def get(self,*args, **kwargs):
    #     return super().get(*args, **kwargs)



class EmployeeUpdateView(UpdateView):
    model = Employee
    fields = '__all__'
    template_name = 'employees/create.html'
    def get(self, *args, **kwargs):
        result = super().get(*args, **kwargs)
        print(self.kwargs)

        return result

    def get_success_url(self):
        return reverse('employee details',
                       kwargs={'pk': self.object.pk
                               })
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
