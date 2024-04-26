# from locale import v
from django.contrib import admin
"""
URL configuration for phagyul project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1.  Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2.Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path, include

#from phagyul import views

#from users import views as users  # Import views from the users app

urlpatterns = [


    path('admin/', admin.site.urls),
    path('',include('users.urls')),
    path('',include('cuisines.urls')),
    path('',include('dance_froms.urls')),
    path('festivals/',include('festivals.urls')),
    path('monuments/',include('monuments.urls')),
    path('about/', include('users.urls')),
    #path('faq/',include('faq'))

]
