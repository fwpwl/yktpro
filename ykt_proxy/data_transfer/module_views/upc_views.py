# coding:utf-8

from data_transfer.module_managers.upc_manager import upc_get_teacher_data, \
    upc_get_department_data, upc_get_student_data, upc_get_course_data, upc_get_choose_data, is_valid_request
from data_transfer.utils.network import success_response, get_para_from_request_safe, error_response


def upc_get_student_data_view(request):
    """
    URL[GET]:/data/upc/get_student_data/
    """
    key = get_para_from_request_safe(request, 'key')
    if not is_valid_request(key):
        return error_response('无效的请求!')

    ret_data = upc_get_student_data()
    return success_response(ret_data)


def upc_get_teacher_data_view(request):
    """
    URL[GET]:/data/upc/get_teacher_data/
    """
    key = get_para_from_request_safe(request, 'key')
    if not is_valid_request(key):
        return error_response('无效的请求!')

    ret_data = upc_get_teacher_data()
    return success_response(ret_data)


def upc_get_department_data_view(request):
    """
    URL[GET]:/data/upc/get_department_data/
    """
    key = get_para_from_request_safe(request, 'key')
    if not is_valid_request(key):
        return error_response('无效的请求!')

    ret_data = upc_get_department_data()
    return success_response(ret_data)


def upc_get_course_data_view(request):
    """
    URL[GET]:/data/upc/get_course_data/
    """
    key = get_para_from_request_safe(request, 'key')
    if not is_valid_request(key):
        return error_response('无效的请求!')

    ret_data = upc_get_course_data()
    return success_response(ret_data)


def upc_get_choose_data_view(request):
    """
    URL[GET]:/data/upc/get_choose_data/
    """
    key = get_para_from_request_safe(request, 'key')
    if not is_valid_request(key):
        return error_response('无效的请求!')

    ret_data = upc_get_choose_data()
    return success_response(ret_data)