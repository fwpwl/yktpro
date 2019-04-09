# coding: utf-8
from django.conf.urls import url

from data_transfer.module_views.zufe_views import zufe_get_bks_data_view, zufe_get_yjs_data_view, \
    zufe_get_teacher_data_view, zufe_get_department_data_view, zufe_get_bks_classroom_data_view, \
    zufe_get_yjs_classroom_data_view, zufe_get_tradition_class_data_view, zufe_get_bks_choose_classroom_data_view, \
    zufe_get_teacher_choose_classroom_data_view, zufe_get_yjs_choose_classroom_data_view

urlpatterns = [

    url(r'^get_bks_data/?$', zufe_get_bks_data_view),
    url(r'^get_yjs_data/?$', zufe_get_yjs_data_view),
    url(r'^get_teacher_data/?$', zufe_get_teacher_data_view),
    url(r'^get_department_data/?$', zufe_get_department_data_view),

    url(r'^get_bks_major_data/?$', zufe_get_bks_classroom_data_view),
    url(r'^get_yjs_major_data/?$', zufe_get_yjs_classroom_data_view),
    url(r'^get_tradition_class_data/?$', zufe_get_tradition_class_data_view),
    url(r'^get_bks_choose_classroom_data/?$', zufe_get_bks_choose_classroom_data_view),
    url(r'^get_teacher_choose_classroom_data/?$', zufe_get_teacher_choose_classroom_data_view),
    url(r'^get_yjs_choose_classroom_data/?$', zufe_get_yjs_choose_classroom_data_view),
    
]
