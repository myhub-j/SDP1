from django.urls import path
from . import views

app_name = 'festivals'

urlpatterns = [
    path('festivals/', views.index, name='festivals'),
    ]