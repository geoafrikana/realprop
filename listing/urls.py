from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('list-property', views.list_property, name='list_property'),
]