# -*- coding:utf-8 -*-
from django.conf.urls import url, include

from data_transfer.views import test_server

urlpatterns = [

    url(r'^test_server/?$', test_server),
]

# 分层各模块URL
urlpatterns += [
    # 新疆师范大学
    url(r"^scut/", include("data_transfer.module_urls.scut_urls")),
]
