from django.conf.urls import patterns, url
from linkedn import views

urlpatterns = patterns('',
        url(r'^$',views.index, name='index'),
        url(r'^login/?$', views.linkedn_login, name = 'linkedn_login'),
        url(r'^logout/?$',views.linkedn_logout, name = 'linkedn_logout'),
        url(r'login/authenticated/?$', views.linkedn_authenticated, name = 'linkedn_authenticated'),
        )
