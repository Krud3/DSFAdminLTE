from django.urls import path
from . import views

urlpatterns = [ path('login/', views.login, name='login'),
               path('index/', views.index, name='index'), 
               path('logout/', views.logout_view, name='logout'),
               path('forgot_password/', views.forgot_password_view, name='forgot_password'),
               path('recover_password_view/', views.recover_password_view, name='recover_password_view'),
               path('recover_password/', views.recover_password, name='recover_password'),
               path('add_automovil',views.add_automovil, name='add_automovil'),
               path('edit_automovil',views.edit_automovil, name='edit_automovil'),
               path('vis_eli',views.vis_eli, name='vis_eli'),
               path('add_cliente',views.add_cliente, name='add_cliente'),
               path('edit_cliente',views.edit_cliente, name='edit_cliente'),
               path('vis_eli_cliente',views.vis_eli_cliente, name='vis_eli_cliente'),
               path('gra_repuestos',views.gra_repuestos, name='gra_repuestos'),
               path('add_vendedor',views.add_vendedor, name='add_vendedor'),
               path('edit_vendedor',views.edit_vendedor, name='edit_vendedor'),
               path('vis_eli_vendedor',views.vis_eli_vendedor, name='vis_eli_vendedor')
               ]