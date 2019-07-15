# coding:utf-8

from data_transfer.module_managers.sdu_manager import sdu_get_teacher_data, \
    sdu_get_department_data, sdu_get_student_data, sdu_get_course_data, sdu_get_choose_data
from data_transfer.utils.network import json_http_response


def sdu_get_student_data_view(request):
    """
    URL[GET]:/data/sdu/get_student_data/
    """
    ret_data = sdu_get_student_data()
    result_dict = {
        "success": True,
        "msg": "",
        "data": ret_data
    }
    return json_http_response(result_dict)


def sdu_get_teacher_data_view(request):
    """
    URL[GET]:/data/sdu/get_teacher_data/
    """
    ret_data = sdu_get_teacher_data()
    result_dict = {
        "success": True,
        "msg": "",
        "data": ret_data
    }
    return json_http_response(result_dict)


def sdu_get_department_data_view(request):
    """
    URL[GET]:/data/sdu/get_department_data/
    """
    ret_data = sdu_get_department_data()
    result_dict = {
        "success": True,
        "msg": "",
        "data": ret_data
    }
    return json_http_response(result_dict)


def sdu_get_course_data_view(request):
    """
    URL[GET]:/data/sdu/get_course_data/
    """
    ret_data = sdu_get_course_data()
    result_dict = {
        "success": True,
        "msg": "",
        "data": ret_data
    }
    return json_http_response(result_dict)


def sdu_get_choose_data_view(request):
    """
    URL[GET]:/data/sdu/get_choose_data/
    """
    ret_data = sdu_get_choose_data()
    result_dict = {
        "success": True,
        "msg": "",
        "data": ret_data
    }
    return json_http_response(result_dict)
