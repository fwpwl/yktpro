# coding: utf-8
from django.conf.urls import url


urlpatterns = [
    url(r'^get_department_data/?$', get_department_data_view),
    url(r'^get_tradition_class_data/?$', get_tradition_class_data_view),
    url(r'^get_user_map_data/?$', get_user_map_data_view),
    url(r'^get_course_class_data/?$', get_course_class_data_view),
    url(r'^get_choose_course_data/?$', get_choose_course_data_view),
]
