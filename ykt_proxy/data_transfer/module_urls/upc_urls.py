# coding: utf-8
from django.conf.urls import url

from data_transfer.module_views.upc_views import upc_get_student_data_view, upc_get_teacher_data_view, \
    upc_get_department_data_view, upc_get_course_data_view, upc_get_choose_data_view, \
    upc_get_tradition_classroom_data_view, upc_verify_user_view

urlpatterns = [
    url(r'^verify_user/?$', upc_verify_user_view),
    url(r'^get_department_data/?$', upc_get_department_data_view),
    url(r'^get_tradition_classroom_data/?$', upc_get_tradition_classroom_data_view),
    url(r'^get_student_data/?$', upc_get_student_data_view),
    url(r'^get_teacher_data/?$', upc_get_teacher_data_view),
    url(r'^get_course_data/?$', upc_get_course_data_view),
    url(r'^get_choose_data/?$', upc_get_choose_data_view),

]
