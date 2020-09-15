# -*- coding:utf-8 -*-
from django.conf.urls import url, include

from data_transfer.views import test_server

urlpatterns = [

    url(r'^test_server/?$', test_server),
]

# 分层各模块URL
urlpatterns += [
    # 山东工商学院
    url(r"^sdtbu/", include("data_transfer.module_urls.sdtbu_urls")),
]
