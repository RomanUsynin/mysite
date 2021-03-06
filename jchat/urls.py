# -*- encoding: UTF-8 -*-
"""
URLConf for Chat.

@author: Federico Cáceres <fede.caceres@gmail.com>
"""
from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^$', 'jchat.views.main', name="main"),
    url(r'^room/(?P<id>\d)$', 'jchat.views.room_view', name="room"),

    url(r'^send/$', 'jchat.views.send'),
    url(r'^receive/$', 'jchat.views.receive'),
    url(r'^sync/$', 'jchat.views.sync'),

    url(r'^join/$', 'jchat.views.join'),
    url(r'^leave/$', 'jchat.views.leave'),
)