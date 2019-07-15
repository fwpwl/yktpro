# coding:utf-8

from data_transfer.module_managers.sdu_manager import sdu_get_teacher_data, \
    sdu_get_department_data, sdu_get_student_data, sdu_get_course_data, sdu_get_choose_data, is_valid_request
from data_transfer.utils.network import success_response, get_para_from_request_safe, error_response


def sdu_get_student_data_view(request):
    """
    URL[GET]:/data/sdu/get_student_data/
    """
    key = get_para_from_request_safe(request, 'key')
    if not is_valid_request(key):
        return error_response('无效的请求!')

    ret_data = sdu_get_student_data()
    return success_response(ret_data)


def sdu_get_teacher_data_view(request):
    """
    URL[GET]:/data/sdu/get_teacher_data/
    """
    key = get_para_from_request_safe(request, 'key')
    if not is_valid_request(key):
        return error_response('无效的请求!')

    ret_data = sdu_get_teacher_data()
    return success_response(ret_data)


def sdu_get_department_data_view(request):
    """
    URL[GET]:/data/sdu/get_department_data/
    """
    key = get_para_from_request_safe(request, 'key')
    if not is_valid_request(key):
        return error_response('无效的请求!')

    ret_data = sdu_get_department_data()
    return success_response(ret_data)


def sdu_get_course_data_view(request):
    """
    URL[GET]:/data/sdu/get_course_data/
    """
    key = get_para_from_request_safe(request, 'key')
    if not is_valid_request(key):
        return error_response('无效的请求!')

    ret_data = sdu_get_course_data()
    return success_response(ret_data)


def sdu_get_choose_data_view(request):
    """
    URL[GET]:/data/sdu/get_choose_data/
    """
    key = get_para_from_request_safe(request, 'key')
    if not is_valid_request(key):
        return error_response('无效的请求!')

    ret_data = sdu_get_choose_data()
    return success_response(ret_data)
