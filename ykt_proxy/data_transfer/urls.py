# -*- coding:utf-8 -*-
from django.conf.urls import url, include

from data_transfer.views import test_server

urlpatterns = [

    url(r'^test_server/?$', test_server),
]

urlpatterns += [
    # 北京化工大学研究生院
    url(r"^grabuct/", include("data_transfer.module_urls.grabuct_urls")),
    

]
