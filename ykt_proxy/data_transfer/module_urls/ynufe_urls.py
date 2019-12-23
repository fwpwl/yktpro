# coding: utf-8
from django.conf.urls import url

from data_transfer.module_views.ynufe_views import ynufe_get_choose_data_view, ynufe_get_department_data_view, \
    ynufe_get_tra_classroom_data_view, ynufe_get_user_data_view, ynufe_get_course_data_view

urlpatterns = [
    url(r'^ynufe_get_department_data/?$', ynufe_get_department_data_view),
    url(r'^ynufe_get_tra_classroom_data/?$', ynufe_get_tra_classroom_data_view),
    url(r'^ynufe_get_user_data/?$', ynufe_get_user_data_view),
    url(r'^ynufe_get_course_data/?$', ynufe_get_course_data_view),
    url(r'^ynufe_get_choose_data/?$', ynufe_get_choose_data_view),

]
