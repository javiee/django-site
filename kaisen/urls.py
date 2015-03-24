from django.conf.urls import patterns, include, url
from django.contrib import admin
from linkedn import views

urlpatterns = patterns('',
    url(r'^$', 'linkedn.views.index'),
    url(r'^contact/', views.contacform, name = 'linkedn_contacform'),
    url(r'^linkedn/', include('linkedn.urls', namespace = "linkedn")),
    url(r'^admin/', include(admin.site.urls)),
    )

