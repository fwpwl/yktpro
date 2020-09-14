# coding: utf-8
from django.conf.urls import url

from data_transfer.module_views.scut_views import scut_get_choose_data_view, scut_get_department_data_view, \
    scut_get_tra_classroom_data_view, scut_get_user_data_view, scut_get_course_data_view

urlpatterns = [
    url(r'^get_department_data/?$', scut_get_department_data_view),
    url(r'^get_tra_classroom_data/?$', scut_get_tra_classroom_data_view),
    url(r'^get_user_data/?$', scut_get_user_data_view),
    url(r'^get_course_data/?$', scut_get_course_data_view),
    url(r'^get_choose_data/?$', scut_get_choose_data_view),

]
