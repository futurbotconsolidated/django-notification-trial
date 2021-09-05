from django.contrib import admin
from django.urls import include
from django.urls.conf import path
from django.urls.resolvers import URLPattern
from . import views


urlpatterns= [
    path('', views.index, name='index'),
    path('<str:room_name>/',views.room, name='room')
]