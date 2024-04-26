from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('subscribe/',views.subscribe,name='subscribe'),
    path('login/', views.login, name='login'),
    path('login1/', views.login1, name='login1'),
    path('signup/', views.signup, name='signup'),
    path('signup1/', views.signup1, name='signup1'),
    path('logout/', views.logout, name='logout'),
    path('about/', views.about, name='about'),
    path('cuisines/',views.cuisines, name='cuisines'),
    path('dance_froms/',views.dance_froms, name='dance_froms'),
    path('monuments/', views.monuments, name='monuments'),
    path('festivals/', views.festivals, name='festivals'),
    path('faq/', views.faq, name='faq'),
    path('Blogs/',views.Blogs, name='blog-post'),
    path('contact/',views.contact, name='contact'),
    # add more paths here
]
