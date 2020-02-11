# coding: utf-8
from django.conf.urls import url

from data_transfer.module_views.tjcu_views import tjcu_get_choose_data_view, tjcu_get_department_data_view, \
    tjcu_get_tra_classroom_data_view, tjcu_get_user_data_view, tjcu_get_course_data_view

urlpatterns = [
    url(r'^tjcu_get_department_data/?$', tjcu_get_department_data_view),
    url(r'^tjcu_get_tra_classroom_data/?$', tjcu_get_tra_classroom_data_view),
    url(r'^tjcu_get_user_data/?$', tjcu_get_user_data_view),
    url(r'^tjcu_get_course_data/?$', tjcu_get_course_data_view),
    url(r'^tjcu_get_choose_data/?$', tjcu_get_choose_data_view),

]
