# coding: utf-8
from django.conf.urls import url

from data_transfer.module_views.sdtbu_views import sdtbu_get_choose_data_view, sdtbu_get_department_data_view, \
    sdtbu_get_tra_classroom_data_view, sdtbu_get_user_data_view, sdtbu_get_course_data_view

urlpatterns = [
    url(r'^get_department_data/?$', sdtbu_get_department_data_view),
    url(r'^get_tra_classroom_data/?$', sdtbu_get_tra_classroom_data_view),
    url(r'^get_user_data/?$', sdtbu_get_user_data_view),
    url(r'^get_course_data/?$', sdtbu_get_course_data_view),
    url(r'^get_choose_data/?$', sdtbu_get_choose_data_view),

]
