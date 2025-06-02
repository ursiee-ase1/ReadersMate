#Defines Url patterns for readers_log

from django.urls import path

from . import views

app_name = 'readers_log'
urlpatterns= [
    #home page
    path('', views.index, name='index'),
]