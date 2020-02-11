# coding: utf-8
from django.conf.urls import url

from data_transfer.module_views.nxu_views import nxu_get_student_data_view, nxu_get_choose_data_view, \
    nxu_get_course_data_view, nxu_get_teacher_data_view

urlpatterns = [
    url(r'^nxu_get_student_data/?$', nxu_get_student_data_view),
    url(r'^nxu_get_teacher_data/?$', nxu_get_teacher_data_view),
    url(r'^nxu_get_course_data/?$', nxu_get_course_data_view),
    url(r'^nxu_get_choose_data/?$', nxu_get_choose_data_view),

]
