# coding:utf-8
""""
西安科技大学
"""

from data_transfer.module_managers import xust_manager
from data_transfer.utils.safe import check_signature
from data_transfer.utils.network import success_response, error_response


# ---------------------------------------------------------------------------------
# 本科生基本数据
# ---------------------------------------------------------------------------------

def get_department_data_view(request):
    """
    URL[GET]:/data/xust/get_department_data/
    """
    params = {k: v for k, v in request.GET.items()}
    if not check_signature(**params):
        return error_response('无效的请求!')

    ret_data = xust_manager.get_department_data()
    return success_response(ret_data)


def get_tra_classroom_data_view(request):
    params = {k: v for k, v in request.GET.items()}
    if not check_signature(**params):
        return error_response('无效的请求!')

    page = int(request.GET.get("page", 0))
    page_size = int(request.GET.get("page_size", 2000))
    ret_data = xust_manager.get_tra_classroom_data(page=page, page_size=page_size)
    return success_response(ret_data)


def get_user_data_view(request):
    params = {k: v for k, v in request.GET.items()}
    if not check_signature(**params):
        return error_response('无效的请求!')

    page = int(request.GET.get("page", 0))
    page_size = int(request.GET.get("page_size", 2000))
    year = request.GET.get("year", "2019")
    ret_data = xust_manager.get_user_data(year=year, page=page, page_size=page_size)
    return success_response(ret_data)


def get_course_data_view(request):
    params = {k: v for k, v in request.GET.items()}
    if not check_signature(**params):
        return error_response('无效的请求!')

    page = int(request.GET.get("page", 0))
    page_size = int(request.GET.get("page_size", 2000))
    year = request.GET.get("year", "2019")
    term = request.GET.get("term", "3")
    ret_data = xust_manager.get_course_data(year=year, term=term, page=page, page_size=page_size)
    return success_response(ret_data)


def get_choose_data_view(request):
    params = {k: v for k, v in request.GET.items()}
    if not check_signature(**params):
        return error_response('无效的请求!')
    
    page = int(request.GET.get("page", 0))
    page_size = int(request.GET.get("page_size", 2000))
    year = request.GET.get("year", "2019")
    term = request.GET.get("term", "3")
    ret_data = xust_manager.get_choose_data(year=year, term=term, page=page, page_size=page_size)
    return success_response(ret_data)
