# coding: utf-8
from django.conf.urls import url

from data_transfer.module_views.xjnu_views import xjnu_get_choose_data_view, xjnu_get_department_data_view, \
    xjnu_get_tra_classroom_data_view, xjnu_get_user_data_view, xjnu_get_course_data_view

urlpatterns = [
    url(r'^xjnu_get_department_data/?$', xjnu_get_department_data_view),
    url(r'^xjnu_get_tra_classroom_data/?$', xjnu_get_tra_classroom_data_view),
    url(r'^xjnu_get_user_data/?$', xjnu_get_user_data_view),
    url(r'^xjnu_get_course_data/?$', xjnu_get_course_data_view),
    url(r'^xjnu_get_choose_data/?$', xjnu_get_choose_data_view),

]
