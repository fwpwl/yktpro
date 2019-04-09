# coding: utf-8
from django.conf.urls import url

from data_transfer.module_views.cqrz_views import get_user_map_data_view, get_course_class_data_view, \
    get_choose_course_data_view

urlpatterns = [
    url(r'^get_user_map_data/?$', get_user_map_data_view),
    url(r'^get_course_class_data/?$', get_course_class_data_view),
    url(r'^get_choose_course_data/?$', get_choose_course_data_view),
]
