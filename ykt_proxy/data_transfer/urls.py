# -*- coding:utf-8 -*-
from django.conf.urls import url, include

from data_transfer.views import test_server

urlpatterns = [

    url(r'^test_server/?$', test_server),
]

# 分层各模块URL
urlpatterns += [
    # 学校教务系统验证模块
    url(r"^fzxy/", include("data_transfer.module_urls.fzxy_urls")),
    url(r"^cqrz/", include("data_transfer.module_urls.cqrz_urls")),
]
