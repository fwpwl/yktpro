# coding:utf-8
from data_transfer.module_managers.grabuct_manager import grabuct_get_user_data, is_valid_request, \
    grabuct_get_department_data, \
    grabuct_get_tra_classroom_data, grabuct_get_course_data, grabuct_get_choose_data
from data_transfer.utils.network import success_response, get_para_from_request_safe, error_response


# ---------------------------------------------------------------------------------
# 本科生基本数据
# ---------------------------------------------------------------------------------

def grabuct_get_department_data_view(request):
    """
    URL[GET]:/data/grabuct/grabuct_get_department_data/
    """
    key = get_para_from_request_safe(request, 'key')
    if not is_valid_request(key):
        return error_response('无效的请求!')

    ret_data = grabuct_get_department_data()
    return success_response(ret_data)


def grabuct_get_tra_classroom_data_view(request):
    """
    URL[GET]:/data/grabuct/grabuct_get_tra_classroom_data/
    """
    key = get_para_from_request_safe(request, 'key')
    if not is_valid_request(key):
        return error_response('无效的请求!')

    ret_data = grabuct_get_tra_classroom_data()
    return success_response(ret_data)


def grabuct_get_user_data_view(request):
    """
    URL[GET]:/data/grabuct/grabuct_get_user_data/
    """
    key = get_para_from_request_safe(request, 'key')
    if not is_valid_request(key):
        return error_response('无效的请求!')

    ret_data = grabuct_get_user_data()
    return success_response(ret_data)


def grabuct_get_course_data_view(request):
    """
    URL[GET]:/data/grabuct/grabuct_get_course_data/
    """
    key = get_para_from_request_safe(request, 'key')
    if not is_valid_request(key):
        return error_response('无效的请求!')
    year = get_para_from_request_safe(request, 'year')
    term = get_para_from_request_safe(request, 'term')

    ret_data = grabuct_get_course_data(year, term)
    return success_response(ret_data)


def grabuct_get_choose_data_view(request):
    """
    URL[GET]:/data/grabuct/grabuct_get_choose_data/
    """
    key = get_para_from_request_safe(request, 'key')
    if not is_valid_request(key):
        return error_response('无效的请求!')
    year = get_para_from_request_safe(request, 'year')
    term = get_para_from_request_safe(request, 'term')
    ret_data = grabuct_get_choose_data(year, term)
    return success_response(ret_data)
