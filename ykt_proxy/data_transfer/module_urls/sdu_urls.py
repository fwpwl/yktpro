# coding: utf-8
from django.conf.urls import url

from data_transfer.module_views.sdu_views import sdu_get_bks_data_view, sdu_get_yjs_data_view, \
    sdu_get_teacher_data_view, sdu_get_department_data_view, sdu_get_bks_classroom_data_view, \
    sdu_get_yjs_classroom_data_view, sdu_get_tradition_class_data_view, sdu_get_bks_choose_classroom_data_view, \
    sdu_get_teacher_choose_classroom_data_view, sdu_get_yjs_choose_classroom_data_view

urlpatterns = [

    url(r'^get_bks_data/?$', sdu_get_bks_data_view),
    url(r'^get_yjs_data/?$', sdu_get_yjs_data_view),
    url(r'^get_teacher_data/?$', sdu_get_teacher_data_view),
    url(r'^get_department_data/?$', sdu_get_department_data_view),

    url(r'^get_bks_major_data/?$', sdu_get_bks_classroom_data_view),
    url(r'^get_yjs_major_data/?$', sdu_get_yjs_classroom_data_view),
    url(r'^get_tradition_class_data/?$', sdu_get_tradition_class_data_view),
    url(r'^get_bks_choose_classroom_data/?$', sdu_get_bks_choose_classroom_data_view),
    url(r'^get_teacher_choose_classroom_data/?$', sdu_get_teacher_choose_classroom_data_view),
    url(r'^get_yjs_choose_classroom_data/?$', sdu_get_yjs_choose_classroom_data_view),
    
]
