# -*- coding:utf-8 -*-
from django.conf.urls import url, include

from data_transfer.views import test_server

urlpatterns = [

    url(r'^test_server/?$', test_server),
]

urlpatterns += [
    # 云南师范大学文理学院
    url(r"^ysdwl/", include("data_transfer.module_urls.ysdwl_urls")),
    

]
