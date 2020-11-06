from django.conf.urls import *
from django.urls import path
from . import views

urlpatterns = [
    url(r'^$', views.main, name='main'), 				#goto views.py -> main()
    path('repo',views.repo, name='repo'),
    path('<str:repo>/top-commits',views.user, name='user'),
]
