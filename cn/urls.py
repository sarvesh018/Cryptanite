from django.urls import path, re_path
from cn.views import index
from cn.views import home

urlpatterns = [
    #path('', index, name='index'),
    path('', home, name="home"),
]