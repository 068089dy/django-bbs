from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
import mysite.views

urlpatterns = [
    url(r'^$', mysite.views.home),
]