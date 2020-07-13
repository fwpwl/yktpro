# -*- coding:utf-8 -*-
from django.conf.urls import url, include

from data_transfer.views import test_server

urlpatterns = [

    url(r'^test_server/?$', test_server),
]

# 分层各模块URL
urlpatterns += [
    # 天津商业大学
    url(r"^tjcu/", include("data_transfer.module_urls.tjcu_urls")),
    # 哈尔滨工程大学研究生院
    url(r"^hrbeuyjs/", include("data_transfer.module_urls.hrbeuyjs_urls")),
    # 新疆师范大学
    url(r"^xjnu/", include("data_transfer.module_urls.xjnu_urls")),
    # 重庆青年职业技术学院
    url(r"^cqyu/", include("data_transfer.module_urls.cqyu_urls")),
]
