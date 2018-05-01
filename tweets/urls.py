from django.urls import path

from . import views

app_name = 'tweets'
urlpatterns = [
    path('', views.index, name='index'),
    path('tweets', views.list, name='list'),
    path('tweets/create', views.create, name='create'),
]
