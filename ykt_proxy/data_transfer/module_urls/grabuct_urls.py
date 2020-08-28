# coding: utf-8
from django.conf.urls import url

from data_transfer.module_views.grabuct_views import grabuct_get_choose_data_view, grabuct_get_department_data_view, \
    grabuct_get_tra_classroom_data_view, grabuct_get_user_data_view, grabuct_get_course_data_view

urlpatterns = [
    url(r'^get_department_data/?$', grabuct_get_department_data_view),
    url(r'^get_tra_classroom_data/?$', grabuct_get_tra_classroom_data_view),
    url(r'^get_user_data/?$', grabuct_get_user_data_view),
    url(r'^get_course_data/?$', grabuct_get_course_data_view),
    url(r'^get_choose_data/?$', grabuct_get_choose_data_view),

]
