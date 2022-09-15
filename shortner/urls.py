from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'shortner'
urlpatterns = [
    path('', views.index, name='index'),
    path('<str:url_short_code>', views.go, name='go'),
    path('do', views.do, name='do'),
    path('yuppi/<str:url_short_code>', views.successfully_created, name='yuppi'),
]
