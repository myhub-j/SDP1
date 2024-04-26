from django.urls import path
from . import views

app_name = 'cuisines'

urlpatterns = [
    path('/cuisines/', views.index, name='cuisines'),
    path('/subscribe/',views.subscribe,name='subscribe'),

    ]