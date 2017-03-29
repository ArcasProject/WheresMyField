from django.contrib import admin
from django.conf.urls import url, include
from rest_framework import routers
from library import views

urlpatterns = [
    # url(r'^index', views.viewDashboard),
    url(r'^admin/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^index/(?P<slug>[-\w]+)/$', views.viewDashboard, name='thing_detail'),
]
