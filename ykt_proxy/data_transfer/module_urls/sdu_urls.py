# coding: utf-8
from django.conf.urls import url

from data_transfer.module_views.sdu_views import sdu_get_student_data_view, sdu_get_teacher_data_view, \
    sdu_get_department_data_view, sdu_get_course_data_view, sdu_get_choose_data_view

urlpatterns = [

    url(r'^get_student_data/?$', sdu_get_student_data_view),
    url(r'^get_teacher_data/?$', sdu_get_teacher_data_view),
    url(r'^get_department_data/?$', sdu_get_department_data_view),
    url(r'^get_course_data/?$', sdu_get_course_data_view),
    url(r'^get_choose_data/?$', sdu_get_choose_data_view),

]
