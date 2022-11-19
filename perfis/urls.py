from django.urls import path, re_path
from perfis import views

urlpatterns = [
	path('', views.index, name='index'),
	path('perfis/<int:perfil_id>', views.exibir, name='exibir'),
	# re_path(r'^perfis/\d+$', views.exibir, name='perfis')
	path('perfis/<int:perfil_id>/convidar', views.convidar, name='convidar'),
	path('convite/<int:convite_id>/aceitar', views.aceitar, name='aceitar')
]