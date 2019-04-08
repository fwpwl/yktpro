# coding:utf-8

from data_transfer.module_managers.cqrz_manager import cqrz_get_user_info_data, cqrz_get_course_data, \
    cqrz_get_choose_course_data
from data_transfer.utils.network import json_http_response


def get_user_map_data_view(request):
    """
    URL[GET]:/data/cqrz/get_user_map_data/
    """
    try:
        ret_data = cqrz_get_user_info_data()
        result_dict = {
            "success": True,
            "msg": "",
            "data": ret_data
        }
    except Exception as e:
        result_dict = {
            "success": False,
            "msg": str(e),
            "data": {}
        }

    return json_http_response(result_dict)


def get_course_class_data_view(request):
    """
    URL[GET]:/data/cqrz/get_course_class_data/
    """
    try:
        ret_data = cqrz_get_course_data()
        result_dict = {
            "success": True,
            "msg": "",
            "data": ret_data
        }
    except Exception as e:
        result_dict = {
            "success": False,
            "msg": str(e),
            "data": {}
        }

    return json_http_response(result_dict)


def get_choose_course_data_view(request):
    """
    URL[GET]:/data/cqrz/get_choose_course_data/
    """
    try:
        ret_data = cqrz_get_choose_course_data()
        result_dict = {
            "success": True,
            "msg": "",
            "data": ret_data
        }
    except Exception as e:
        result_dict = {
            "success": False,
            "msg": str(e),
            "data": {}
        }

    return json_http_response(result_dict)
