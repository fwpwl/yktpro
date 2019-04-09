# coding:utf-8

from data_transfer.module_managers.zufe_manager import zufe_get_bks_data, zufe_get_yjs_data, zufe_get_teacher_data, \
    zufe_get_department_data, zufe_get_bks_major_data, zufe_get_yjs_major_data, zufe_get_tradition_class_data, \
    zufe_get_bks_choose_classroom_data, zufe_get_teacher_choose_classroom_data, zufe_get_yjs_choose_classroom_data
from data_transfer.utils.network import json_http_response


def zufe_get_bks_data_view(request):
    """
    URL[GET]:/data/zufe/get_bks_data/

    """
    ret_data = zufe_get_bks_data()
    result_dict = {
        "success": True,
        "msg": "",
        "data": ret_data
    }
    return json_http_response(result_dict)


def zufe_get_yjs_data_view(request):
    """
    URL[GET]:/data/zufe/get_yjs_data/
    """
    ret_data = zufe_get_yjs_data()
    result_dict = {
        "success": True,
        "msg": "",
        "data": ret_data
    }
    return json_http_response(result_dict)


def zufe_get_teacher_data_view(request):
    """
    URL[GET]:/data/zufe/get_teacher_data/
    """
    ret_data = zufe_get_teacher_data()
    result_dict = {
        "success": True,
        "msg": "",
        "data": ret_data
    }
    return json_http_response(result_dict)


def zufe_get_department_data_view(request):
    """
    URL[GET]:/data/zufe/get_department_data/
    """
    ret_data = zufe_get_department_data()
    result_dict = {
        "success": True,
        "msg": "",
        "data": ret_data
    }
    return json_http_response(result_dict)


def zufe_get_bks_classroom_data_view(request):
    """
    URL[GET]:/data/zufe/get_bks_major_data/
    """
    ret_data = zufe_get_bks_major_data()
    result_dict = {
        "success": True,
        "msg": "",
        "data": ret_data
    }
    return json_http_response(result_dict)


def zufe_get_yjs_classroom_data_view(request):
    """
    URL[GET]:/data/zufe/get_yjs_major_data/
    """
    ret_data = zufe_get_yjs_major_data()
    result_dict = {
        "success": True,
        "msg": "",
        "data": ret_data
    }
    return json_http_response(result_dict)


def zufe_get_tradition_class_data_view(request):
    """
    URL[GET]:/data/zufe/get_tradition_class_data/
    """
    ret_data = zufe_get_tradition_class_data()
    result_dict = {
        "success": True,
        "msg": "",
        "data": ret_data
    }
    return json_http_response(result_dict)


def zufe_get_bks_choose_classroom_data_view(request):
    """
    URL[GET]:/data/zufe/get_bks_choose_classroom_data/
    """
    ret_data = zufe_get_bks_choose_classroom_data()
    result_dict = {
        "success": True,
        "msg": "",
        "data": ret_data
    }
    return json_http_response(result_dict)


def zufe_get_teacher_choose_classroom_data_view(request):
    """
    URL[GET]:/data/zufe/get_teacher_choose_classroom_data/
    """
    ret_data = zufe_get_teacher_choose_classroom_data()
    result_dict = {
        "success": True,
        "msg": "",
        "data": ret_data
    }
    return json_http_response(result_dict)


def zufe_get_yjs_choose_classroom_data_view(request):
    """
    URL[GET]:/data/zufe/get_yjs_choose_classroom_data/
    """
    ret_data = zufe_get_yjs_choose_classroom_data()
    result_dict = {
        "success": True,
        "msg": "",
        "data": ret_data
    }
    return json_http_response(result_dict)
