from django.urls import path
from django.views import generic as views
from Class_Based_Views.web.views import IndexView, IndexViewWithTemplate, IndexViewWithListView, EmployeeDetailView, \
    EmployeeCreateView, EmployeeUpdateView

urlpatterns = (
    path('',IndexViewWithListView.as_view(),name='index'),
    path('details/<int:pk>/',EmployeeDetailView.as_view(),name='employee details'),
    path('create/',EmployeeCreateView.as_view(),name='employee create'),
    path('edit/<int:pk>',EmployeeUpdateView.as_view(),name='employee update'),
    path('redirect-to-index/',views.RedirectView.as_view(url = '/'),name='redirect-to-index'),

)