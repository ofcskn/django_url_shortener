from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'shortner'
urlpatterns = [
    path('', views.index, name='index'),
    path('do', views.do, name='do'),
]
