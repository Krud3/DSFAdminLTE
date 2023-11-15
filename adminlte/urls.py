from django.urls import path
from . import views

urlpatterns = [ path('login/', views.login, name='login'),
               path('index/', views.index, name='index'), 
               path('logout/', views.logout_view, name='logout'),
               path('forgot_password/', views.forgot_password_view, name='forgot_password'),
               path('recover_password_view/', views.recover_password_view, name='recover_password_view'),
               path('recover_password/', views.recover_password, name='recover_password'),
               ]