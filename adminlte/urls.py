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
               path('vis_eli_vendedor',views.vis_eli_vendedor, name='vis_eli_vendedor'),
               path('agregar_vehiculo',views.agregar_vehiculo, name='agregar_vehiculo'),
               path('editar_vehiculo',views.editar_vehiculo, name='editar_vehiculo'),
               path('eliminar_vehiculo',views.eliminar_vehiculo, name='eliminar_vehiculo'),
               path('agregar_vendedor',views.agregar_vendedor, name='agregar_vendedor'),
               path('editar_vendedor',views.editar_vendedor, name='editar_vendedor'),
               path('eliminar_vendedor',views.eliminar_vendedor, name='eliminar_vendedor'),
               path('agregar_cliente',views.agregar_cliente, name='agregar_cliente'),
               path('editar_cliente',views.editar_cliente, name='editar_cliente'),
               path('eliminar_cliente',views.eliminar_cliente, name='eliminar_cliente'),
               path('gra_rep_add',views.gra_rep_add, name='gra_rep_add'),
               path('add_repuesto/', views.add_repuesto, name='add_repuesto'),
               path('agregar_repuesto/', views.agregar_repuesto, name='agregar_repuesto'),
               path('eliminar_repuesto', views.eliminar_repuesto, name='eliminar_repuesto'),
               path('vis_eli_repuesto', views.vis_eli_repuesto, name='vis_eli_repuesto'),
               path('add_sucursal/', views.add_sucursal, name='add_sucursal'),
               path('agregar_sucursal/', views.agregar_sucursal, name='agregar_sucursal'),
               path('eliminar_sucursal', views.eliminar_sucursal, name='eliminar_sucursal'),
               path('vis_eli_sucursal', views.vis_eli_sucursal, name='vis_eli_sucursal'),
               ]
