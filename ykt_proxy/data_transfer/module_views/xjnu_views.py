# coding:utf-8
from data_transfer.module_managers.xjnu_manager import xjnu_get_user_data, is_valid_request, \
    xjnu_get_department_data, \
    xjnu_get_tra_classroom_data, xjnu_get_course_data, xjnu_get_choose_data
from data_transfer.utils.network import success_response, get_para_from_request_safe, error_response


# ---------------------------------------------------------------------------------
# 本科生基本数据
# ---------------------------------------------------------------------------------

def xjnu_get_department_data_view(request):
    """
    URL[GET]:/data/xjnu/xjnu_get_department_data/
    """
    # key = get_para_from_request_safe(request, 'key')
    # if not is_valid_request(key):
    #     return error_response('无效的请求!')

    ret_data = xjnu_get_department_data()
    return success_response(ret_data)


def xjnu_get_tra_classroom_data_view(request):
    """
    URL[GET]:/data/xjnu/xjnu_get_tra_classroom_data/
    """
    # key = get_para_from_request_safe(request, 'key')
    # if not is_valid_request(key):
    #     return error_response('无效的请求!')

    ret_data = xjnu_get_tra_classroom_data()
    return success_response(ret_data)


def xjnu_get_user_data_view(request):
    """
    URL[GET]:/data/xjnu/xjnu_get_user_data/
    """
    # key = get_para_from_request_safe(request, 'key')
    # if not is_valid_request(key):
    #     return error_response('无效的请求!')

    ret_data = xjnu_get_user_data()
    return success_response(ret_data)


def xjnu_get_course_data_view(request):
    """
    URL[GET]:/data/xjnu/xjnu_get_course_data/
    """
    # key = get_para_from_request_safe(request, 'key')
    # if not is_valid_request(key):
    #     return error_response('无效的请求!')

    ret_data = xjnu_get_course_data()
    return success_response(ret_data)


def xjnu_get_choose_data_view(request):
    """
    URL[GET]:/data/xjnu/xjnu_get_choose_data/
    """
    # key = get_para_from_request_safe(request, 'key')
    # if not is_valid_request(key):
    #     return error_response('无效的请求!')

    ret_data = xjnu_get_choose_data()
    return success_response(ret_data)
