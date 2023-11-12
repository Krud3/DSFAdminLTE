from django.urls import path
from . import views

urlpatterns = [ path('', views.index, name='index'), 
                path('index3.html', views.index3, name='index3'),
                path('login.html', views.login, name='login')
               ]