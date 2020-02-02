# coding:utf-8
""""
西安科技大学
"""

from data_transfer.module_managers import xust_manager
from data_transfer.utils.network import success_response, get_para_from_request_safe, error_response


# ---------------------------------------------------------------------------------
# 本科生基本数据
# ---------------------------------------------------------------------------------

def get_department_data_view(request):
    """
    URL[GET]:/data/xust/get_department_data/
    """
    # key = get_para_from_request_safe(request, 'key')
    # if not is_valid_request(key):
    #     return error_response('无效的请求!')

    ret_data = xust_manager.get_department_data()
    return success_response(ret_data)


def get_tra_classroom_data_view(request):
    """
    URL[GET]:/data/ynufe/ynufe_get_tra_classroom_data/
    """
    # key = get_para_from_request_safe(request, 'key')
    # if not is_valid_request(key):
    #     return error_response('无效的请求!')
    page = int(request.GET.get("page", 0))
    page_size = int(request.GET.get("page_size", 2000))
    ret_data = xust_manager.get_tra_classroom_data(page=page, page_size=page_size)
    return success_response(ret_data)


def get_user_data_view(request):
    """
    URL[GET]:/data/ynufe/ynufe_get_user_data/
    """
    # key = get_para_from_request_safe(request, 'key')
    # if not is_valid_request(key):
    #     return error_response('无效的请求!')
    page = int(request.GET.get("page", 0))
    page_size = int(request.GET.get("page_size", 2000))
    year = request.GET.get("year", "2019")
    ret_data = xust_manager.get_user_data(year=year, page=page, page_size=page_size)
    return success_response(ret_data)


def get_course_data_view(request):
    """
    URL[GET]:/data/ynufe/ynufe_get_course_data/
    """
    # key = get_para_from_request_safe(request, 'key')
    # if not is_valid_request(key):
    #     return error_response('无效的请求!')
    #
    page = int(request.GET.get("page", 0))
    page_size = int(request.GET.get("page_size", 2000))
    year = request.GET.get("year", "2019")
    term = request.GET.get("term", "3")
    ret_data = xust_manager.get_course_data(year=year, term=term, page=page, page_size=page_size)
    return success_response(ret_data)


def get_choose_data_view(request):
    """
    URL[GET]:/data/ynufe/ynufe_get_choose_data/
    """
    # key = get_para_from_request_safe(request, 'key')
    # if not is_valid_request(key):
    #     return error_response('无效的请求!')
    page = int(request.GET.get("page", 0))
    page_size = int(request.GET.get("page_size", 2000))
    year = request.GET.get("year", "2019")
    term = request.GET.get("term", "3")
    ret_data = xust_manager.get_choose_data(year=year, term=term, page=page, page_size=page_size)
    return success_response(ret_data)
