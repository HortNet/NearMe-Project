from django.urls import path
from .import views

urlpatterns=[
    path('nearmeApp/',views.index,name='index')

]