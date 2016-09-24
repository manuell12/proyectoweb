from django.conf.urls import include, url
from . import views

urlpatterns = [
        url(r'^$',views.login_web, name='index'),
        url(r'^login/$',views.login, name='login'),
        url(r'^login_required$',views.user_not_logged,name='user_not_logged'),
        url(r'^home/$',views.home, name='home'),
        url(r'^home/logout/$',views.logout, name='logout'),
        url(r'^home/companias/$',views.compania_list, name='compania'),
        url(r'^home/voluntarios/$',views.voluntarios_list, name='voluntario'),
        url(r'^home/voluntario/(?P<pk>[0-9-k]+)/edit/$', views.voluntario_edit, name='voluntario_edit'),
        url(r'^home/voluntarios/agregar_voluntario$',views.voluntario_new, name='agregar-voluntario'),
        url(r'^home/voluntarios/agregado$',views.voluntario_guardar, name='voluntario_nuevo'),
        url(r'^home/voluntario/(?P<pk>[0-9-k]+)/edit/editado$',views.voluntario_editado, name='voluntario_editado'),
        url (r'^home/informe1/$', views.informe1_list, name='informe1_list'),
        url(r'^home/informe1/(?P<pk>[0-9]+)$/edit', views.informe1_edit, name='informe1_edit'),
#        url(r'^post/(?P<pk>[0-9]+)/edit/$', views.post_edit, name='post_edit'),
]