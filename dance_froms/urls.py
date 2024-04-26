from django.urls import path
from . import views

app_name = 'dance_froms'

urlpatterns = [
    path('/dance_froms/', views.index, name='dance_froms'),
    ]