from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'shortner'
urlpatterns = [
    # main page of the url shortner
    path('', views.index, name='index'),
    # create a short url via the long url
    path('do', views.do, name='do'),
    #go to the long url via the short url
    path('<str:url_short_code>', views.go, name='go'),
    # the successful, ending page
    path('yuppi/<str:url_short_code>', views.successfully_created, name='yuppi'),
]
