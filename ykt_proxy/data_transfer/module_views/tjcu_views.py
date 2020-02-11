# coding:utf-8
from data_transfer.module_managers.tjcu_manager import tjcu_get_user_data, is_valid_request, \
    tjcu_get_department_data, \
    tjcu_get_tra_classroom_data, tjcu_get_course_data, tjcu_get_choose_data
from data_transfer.utils.network import success_response, get_para_from_request_safe, error_response


# ---------------------------------------------------------------------------------
# 本科生基本数据
# ---------------------------------------------------------------------------------

def tjcu_get_department_data_view(request):
    """
    URL[GET]:/data/tjcu/tjcu_get_department_data/
    """
    key = get_para_from_request_safe(request, 'key')
    if not is_valid_request(key):
        return error_response('无效的请求!')

    ret_data = tjcu_get_department_data()
    return success_response(ret_data)


def tjcu_get_tra_classroom_data_view(request):
    """
    URL[GET]:/data/tjcu/tjcu_get_tra_classroom_data/
    """
    key = get_para_from_request_safe(request, 'key')
    if not is_valid_request(key):
        return error_response('无效的请求!')

    ret_data = tjcu_get_tra_classroom_data()
    return success_response(ret_data)


def tjcu_get_user_data_view(request):
    """
    URL[GET]:/data/tjcu/tjcu_get_user_data/
    """
    key = get_para_from_request_safe(request, 'key')
    if not is_valid_request(key):
        return error_response('无效的请求!')

    ret_data = tjcu_get_user_data()
    return success_response(ret_data)


def tjcu_get_course_data_view(request):
    """
    URL[GET]:/data/tjcu/tjcu_get_course_data/
    """
    key = get_para_from_request_safe(request, 'key')
    if not is_valid_request(key):
        return error_response('无效的请求!')

    ret_data = tjcu_get_course_data()
    return success_response(ret_data)


def tjcu_get_choose_data_view(request):
    """
    URL[GET]:/data/tjcu/tjcu_get_choose_data/
    """
    key = get_para_from_request_safe(request, 'key')
    if not is_valid_request(key):
        return error_response('无效的请求!')

    ret_data = tjcu_get_choose_data()
    return success_response(ret_data)
