# coding:utf-8
from data_transfer.module_managers.nwu_manager import is_valid_request, nwu_bks_get_student_data, \
    nwu_bks_get_choose_data, nwu_yjs_get_course_data, nwu_yjs_get_choose_data, nwu_bks_get_course_data

from data_transfer.utils.network import success_response, get_para_from_request_safe, error_response


# ---------------------------------------------------------------------------------
# 本科生基本数据
# ---------------------------------------------------------------------------------
def nwu_bks_get_student_data_view(request):
    """
    URL[GET]:/data/nwu/nwu_bks_get_student_data/
    """
    key = get_para_from_request_safe(request, 'key')
    if not is_valid_request(key):
        return error_response('无效的请求!')

    ret_data = nwu_bks_get_student_data()
    return success_response(ret_data)


def nwu_bks_get_course_data_view(request):
    """
    URL[GET]:/data/nwu/nwu_bks_get_course_data/
    """
    key = get_para_from_request_safe(request, 'key')
    if not is_valid_request(key):
        return error_response('无效的请求!')

    year = get_para_from_request_safe(request, 'year')
    term = get_para_from_request_safe(request, 'term')

    ret_data = nwu_bks_get_course_data(year, term)
    return success_response(ret_data)


def nwu_bks_get_choose_data_view(request):
    """
    URL[GET]:/data/nwu/nwu_bks_get_choose_data/
    """
    key = get_para_from_request_safe(request, 'key')
    if not is_valid_request(key):
        return error_response('无效的请求!')

    ret_data = nwu_bks_get_choose_data()
    return success_response(ret_data)


# ---------------------------------------------------------------------------------
# 研究生数据
# ---------------------------------------------------------------------------------
def nwu_yjs_get_course_data_view(request):
    """
    URL[GET]:/data/nwu/nwu_yjs_get_course_data/
    """
    key = get_para_from_request_safe(request, 'key')
    if not is_valid_request(key):
        return error_response('无效的请求!')

    year = get_para_from_request_safe(request, 'year')
    term = get_para_from_request_safe(request, 'term')

    ret_data = nwu_yjs_get_course_data(year, term)
    return success_response(ret_data)


def nwu_yjs_get_choose_data_view(request):
    """
    URL[GET]:/data/nwu/nwu_yjs_get_choose_data/
    """
    key = get_para_from_request_safe(request, 'key')
    if not is_valid_request(key):
        return error_response('无效的请求!')

    ret_data = nwu_yjs_get_choose_data()
    return success_response(ret_data)
