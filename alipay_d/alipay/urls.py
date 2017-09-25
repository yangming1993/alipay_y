#!/usr/bin/env python
#encoding: utf-8
'''
@author:ym

@time:2017/9/22
'''

from django.conf.urls import url
from alipay import views
urlpatterns = [
	url('^$', views.index),
	url('^notice/$', views.notice),
	url('^return_url/$', views.return_url),

]