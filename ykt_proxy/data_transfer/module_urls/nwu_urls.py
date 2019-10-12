# coding: utf-8
from django.conf.urls import url

from data_transfer.module_views.nwu_views import nwu_bks_get_student_data_view, nwu_bks_get_choose_data_view, \
    nwu_yjs_get_course_data_view, \
    nwu_yjs_get_choose_data_view, nwu_bks_get_course_data_view

urlpatterns = [
    url(r'^nwu_bks_get_student_data/?$', nwu_bks_get_student_data_view),
    url(r'^nwu_bks_get_course_data/?$', nwu_bks_get_course_data_view),
    url(r'^nwu_bks_get_choose_data/?$', nwu_bks_get_choose_data_view),

    url(r'^nwu_yjs_get_course_data/?$', nwu_yjs_get_course_data_view),
    url(r'^nwu_yjs_get_choose_data/?$', nwu_yjs_get_choose_data_view),

]
