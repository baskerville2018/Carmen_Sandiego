# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.urls import include, path
from django.conf.urls import include, url
from django.contrib.auth import views as auth_views
from . import views as core

app_name = 'carmen'

urlpatterns = [
    # Login
     path('login/', auth_views.LoginView.as_view(template_name='user/auth.html'), name='login'),

    # Logout
     path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    #Cadastro de usuario
     path('usuarios/novo/', core.UserCreateView.as_view(), name='user-create'),

    #Criar partida
     path('criarpartida/', core.PartidaCreate.as_view(), name='criarpartida'),

     path('teste/', core.Jogo.as_view(), name='teste'),

     path('pequim/', core.Fase1.as_view(), name='fase1'),

     path('testemunhaspequim/', core.Testemunhas1.as_view(), name='testemunhas1'),

     path('paris/', core.Fase2.as_view(), name='fase2'),

     path('testemunhasparis/', core.Testemunhas2.as_view(), name='testemunhas2'),

     path('bogota/', core.Fase3.as_view(), name='fase3'),

     path('testemunhasbogota/', core.Testemunhas3.as_view(), name='testemunhas3'),

     path('buenos/', core.Fase4.as_view(), name='fase4'),

     path('testemunhasbuenosaires/', core.Testemunhas4.as_view(), name='testemunhas4'),

     path('mapa/', core.Mapa.as_view(), name='mapa'),

     path('mapa-mundi/', core.MapaMundi.as_view(), name='mapamundi'),


     

]
