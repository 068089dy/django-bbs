"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
import mysite.views
import mycomment.views
urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$', mycomment.views.home.as_view()),
    path('login/', mycomment.views.login),
    path('post/', mycomment.views.post),
    path('register/', mycomment.views.register),
    path('logout/', mycomment.views.logout),
    #提交帖子
    url(r'^posts-(\d{0,8})', mycomment.views.posts),
    #提交评论
    path("comment/", mycomment.views.comments),
    path('test/', mycomment.views.test),
    path('ajax_test/', mycomment.views.ajax_test),
]
