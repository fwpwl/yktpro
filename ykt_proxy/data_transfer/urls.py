# -*- coding:utf-8 -*-
from django.conf.urls import url, include

from data_transfer.views import test_server

urlpatterns = [

    url(r'^test_server/?$', test_server),
]

# 分层各模块URL
urlpatterns += [
    # 学校教务系统验证模块
    url(r"^nxu/", include("data_transfer.module_urls.nxu_urls")),
    url(r"^ynufe/", include("data_transfer.module_urls.ynufe_urls")),
]
