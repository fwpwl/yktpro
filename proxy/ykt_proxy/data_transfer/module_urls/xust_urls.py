# coding: utf-8
from django.conf.urls import url

from data_transfer.module_views import xust_views

urlpatterns = [
    url(r'^get_department_data/?$', xust_views.get_department_data_view),
    url(r'^get_tra_classroom_data/?$', xust_views.get_tra_classroom_data_view),
    url(r'^get_user_data/?$', xust_views.get_user_data_view),
    url(r'^get_course_data/?$', xust_views.get_course_data_view),
    url(r'^get_choose_data/?$', xust_views.get_choose_data_view),

]
