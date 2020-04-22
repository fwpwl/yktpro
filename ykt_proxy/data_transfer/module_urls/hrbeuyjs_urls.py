# coding: utf-8
from django.conf.urls import url

from data_transfer.module_views.hrbeuyjs_views import hrbeuyjs_get_course_data_view, hrbeuyjs_get_choose_data_view, \
    hrbeuyjs_get_user_data_view, hrbeuyjs_get_department_data_view, hrbeuyjs_get_tra_data_view

urlpatterns = [
    url(r'^get_department_data/?$', hrbeuyjs_get_department_data_view),
    url(r'^get_user_data/?$', hrbeuyjs_get_user_data_view),
    url(r'^get_course_data/?$', hrbeuyjs_get_course_data_view),
    url(r'^get_choose_data/?$', hrbeuyjs_get_choose_data_view),
    url(r'^get_tra_classroom_data/?$', hrbeuyjs_get_tra_data_view),

]
