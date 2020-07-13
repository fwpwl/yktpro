# coding: utf-8
from django.conf.urls import url

from data_transfer.module_views.cqyu_views import cqyu_get_choose_data_view, cqyu_get_department_data_view, \
    cqyu_get_tra_classroom_data_view, cqyu_get_user_data_view, cqyu_get_course_data_view

urlpatterns = [
    url(r'^get_department_data/?$', cqyu_get_department_data_view),
    url(r'^get_tra_classroom_data/?$', cqyu_get_tra_classroom_data_view),
    url(r'^get_user_data/?$', cqyu_get_user_data_view),
    url(r'^get_course_data/?$', cqyu_get_course_data_view),
    url(r'^get_choose_data/?$', cqyu_get_choose_data_view),

]
