from django import views
from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name="index"),
    path('allblog', views.allblog, name="allblog"),
    path(r'^post/(?P<post>[-\w]+)/$', views.post, name="post"),
    path('contact', views.contact, name="contact"),
    
]