# coding: utf-8
from django.conf.urls import url

from data_transfer.module_views.ynu_views import ynu_bks_get_department_data_view, ynu_bks_get_tra_classroom_data_view, \
    ynu_bks_get_course_basic_data_view, ynu_bks_get_course_year_data_view, ynu_bks_get_course_belong_data_view, \
    ynu_bks_get_student_data_view, ynu_bks_get_teacher_data_view, ynu_bks_get_choose_data_view, \
    ynu_yjs_get_department_data_view, ynu_yjs_get_student_data_view, ynu_yjs_get_teacher_data_view, \
    ynu_yjs_get_course_basic_data_view, ynu_yjs_get_course_data_view, ynu_yjs_get_choose_data_view

urlpatterns = [
    url(r'^ynu_bks_get_department_data/?$', ynu_bks_get_department_data_view),
    url(r'^ynu_bks_get_tra_classroom_data/?$', ynu_bks_get_tra_classroom_data_view),
    url(r'^ynu_bks_get_course_basic_data/?$', ynu_bks_get_course_basic_data_view),
    url(r'^ynu_bks_get_course_year_data/?$', ynu_bks_get_course_year_data_view),
    url(r'^ynu_bks_get_course_belong_data/?$', ynu_bks_get_course_belong_data_view),
    url(r'^ynu_bks_get_student_data/?$', ynu_bks_get_student_data_view),
    url(r'^ynu_bks_get_teacher_data/?$', ynu_bks_get_teacher_data_view),
    url(r'^ynu_bks_get_choose_data/?$', ynu_bks_get_choose_data_view),

    url(r'^ynu_yjs_get_department_data/?$', ynu_yjs_get_department_data_view),
    url(r'^ynu_yjs_get_student_data/?$', ynu_yjs_get_student_data_view),
    url(r'^ynu_yjs_get_teacher_data/?$', ynu_yjs_get_teacher_data_view),
    url(r'^ynu_yjs_get_course_basic_data/?$', ynu_yjs_get_course_basic_data_view),
    url(r'^ynu_yjs_get_course_data/?$', ynu_yjs_get_course_data_view),
    url(r'^ynu_yjs_get_choose_data/?$', ynu_yjs_get_choose_data_view),

]

