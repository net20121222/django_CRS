from django.conf.urls import patterns, url

from roomsys import views

urlpatterns = patterns('',
    url(r'^$', "index", name='index'),
)
