from django.urls import path
from . import views

app_name = 'monuments'

urlpatterns = [
    path('monuments', views.index, name='monuments'),
    # Add more URL patterns for the 'monuments' app as needed
]
