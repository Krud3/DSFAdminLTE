from django.urls import path
from . import views

urlpatterns = [ path('login/', views.login, name='login'),
               path('index/', views.index, name='index'), 
               path('logout/', views.logout_view, name='logout'),
               path('forgot_password/', views.forgot_password_view, name='forgot_password'),
               path('recover_password_view/', views.recover_password_view, name='recover_password_view'),
               path('recover_password/', views.recover_password, name='recover_password'),
               path('add_automovil',views.add_automovil, name='add_automovil'),
               path('vis_eli_mod_aut',views.vis_eli_mod_aut, name='vis_eli_mod_aut'),
               path('add_cliente',views.add_cliente, name='add_cliente'),
               path('edit_cliente',views.edit_cliente, name='edit_cliente'),
               path('vis_eli_cliente',views.vis_eli_cliente, name='vis_eli_cliente'),
               path('gra_repuestos',views.gra_repuestos, name='gra_repuestos'),
               path('add_vendedor',views.add_vendedor, name='add_vendedor'),
               path('edit_vendedor',views.edit_vendedor, name='edit_vendedor'),
               path('vis_eli_vendedor',views.vis_eli_vendedor, name='vis_eli_vendedor'),
               path('sucursal_add',views.sucursal_add, name='sucursal_add'),
               path('vis_eli_mod_suc',views.vis_eli_mod_suc, name='vis_eli_mod_suc'),
              
               path('repuestos_add',views.repuestos_add, name='repuestos_add'),
               path('vis_eli_mod',views.vis_eli_mod, name='vis_eli_mod'),
               path('jefe_taller_add',views.jefe_taller_add, name='jefe_taller_add'),
               path('vis_eli_mod_jefe',views.vis_eli_mod_jefe, name='vis_eli_mod_jefe'),
               path('reporte_text',views.reporte_text, name='reporte_text'),
               path('reporte_add',views.reporte_add, name='reporte_add'),
               path('reporte_repu_add',views.reporte_repu_add, name='reporte_repu_add'),
               path('reporte_inve',views.reporte_inve, name='reporte_inve'),
               path('gra_rep_add',views.gra_rep_add, name='gra_rep_add'),
               
               
               
               
               
               
               ]