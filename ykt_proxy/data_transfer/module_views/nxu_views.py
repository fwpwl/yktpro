# coding:utf-8
from data_transfer.module_managers.nxu_manager import is_valid_request, nxu_get_student_data, \
    nxu_get_choose_data, nxu_get_course_data, nxu_get_teacher_data

from data_transfer.utils.network import success_response, get_para_from_request_safe, error_response


# ---------------------------------------------------------------------------------
# 本科生基本数据
# ---------------------------------------------------------------------------------
def nxu_get_student_data_view(request):
    """
    URL[GET]:/data/nxu/nxu_get_student_data/
    """
    key = get_para_from_request_safe(request, 'key')
    if not is_valid_request(key):
        return error_response('无效的请求!')

    ret_data = nxu_get_student_data()
    return success_response(ret_data)


def nxu_get_teacher_data_view(request):
    """
    URL[GET]:/data/nxu/nxu_get_teacher_data/
    """
    key = get_para_from_request_safe(request, 'key')
    if not is_valid_request(key):
        return error_response('无效的请求!')

    ret_data = nxu_get_teacher_data()
    return success_response(ret_data)


def nxu_get_course_data_view(request):
    """
    URL[GET]:/data/nxu/nxu_get_course_data/

    PARA:
    term
    """
    key = get_para_from_request_safe(request, 'key')
    if not is_valid_request(key):
        return error_response('无效的请求!')

    term = get_para_from_request_safe(request, 'term')

    ret_data = nxu_get_course_data(term)
    return success_response(ret_data)


def nxu_get_choose_data_view(request):
    """
    URL[GET]:/data/nxu/nxu_get_choose_data/

    PARA:
    term
    """
    key = get_para_from_request_safe(request, 'key')
    if not is_valid_request(key):
        return error_response('无效的请求!')

    term = get_para_from_request_safe(request, 'term')
    ret_data = nxu_get_choose_data(term)
    return success_response(ret_data)
