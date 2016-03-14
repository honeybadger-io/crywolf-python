from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^fail', views.fail, name='fail'),
    url(r'^$', views.index, name='index'),
]
