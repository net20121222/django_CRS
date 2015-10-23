
# @Date    : 2015-10-09 01:52:39
# @Author  : miaolian (mike19890421@163.com)
# @Version : 1.0

from django.conf.urls import patterns, url
from ansible import views

urlpatterns = patterns('ansible.views',
    #url(r'^$', 'index', name='index'),
    url(r'^$', 'list_projects', name='list_projects'),
)

