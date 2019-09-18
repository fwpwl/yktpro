# coding:utf-8

from django.views.decorators.csrf import csrf_exempt

from data_transfer.module_managers.upc_manager import is_user_valid, is_valid_request, upc_bks_get_department_data, \
    upc_bks_get_course_data, upc_bks_get_teacher_data, upc_bks_get_choose_data, upc_bks_get_student_data, \
    upc_bks_get_tradition_classroom_data, upc_yjs_get_course_data, upc_yjs_get_choose_data, \
    upc_yjs_get_student_data, upc_yjs_get_department_data
from data_transfer.utils.network import success_response, get_para_from_request_safe, error_response


@csrf_exempt
def upc_verify_user_view(request):
    """
    URL[POST]:/data/upc/verify_user/
    """
    user_name = get_para_from_request_safe(request, 'user_name')
    password = get_para_from_request_safe(request, 'password')

    is_valid = is_user_valid(user_name, password)
    if is_valid:
        return success_response({})
    else:
        return error_response(u'用户名密码错误!')


# ---------------------------------------------------------------------------------
# 本科生数据
# ---------------------------------------------------------------------------------
def upc_bks_get_department_data_view(request):
    """
    URL[GET]:/data/upc/upc_bks_get_department_data/
    """
    key = get_para_from_request_safe(request, 'key')
    if not is_valid_request(key):
        return error_response('无效的请求!')

    ret_data = upc_bks_get_department_data()
    return success_response(ret_data)


def upc_bks_get_tradition_classroom_data_view(request):
    """
    URL[GET]:/data/upc/upc_bks_get_tradition_classroom_data/
    """
    key = get_para_from_request_safe(request, 'key')
    if not is_valid_request(key):
        return error_response('无效的请求!')

    ret_data = upc_bks_get_tradition_classroom_data()
    return success_response(ret_data)


def upc_bks_get_student_data_view(request):
    """
    URL[GET]:/data/upc/upc_bks_get_student_data/
    """
    key = get_para_from_request_safe(request, 'key')
    if not is_valid_request(key):
        return error_response('无效的请求!')

    ret_data = upc_bks_get_student_data()
    return success_response(ret_data)


def upc_bks_get_teacher_data_view(request):
    """
    URL[GET]:/data/upc/upc_bks_get_teacher_data/
    """
    key = get_para_from_request_safe(request, 'key')
    if not is_valid_request(key):
        return error_response('无效的请求!')

    ret_data = upc_bks_get_teacher_data()
    return success_response(ret_data)


def upc_bks_get_course_data_view(request):
    """
    URL[GET]:/data/upc/upc_bks_get_course_data/
    """
    key = get_para_from_request_safe(request, 'key')
    if not is_valid_request(key):
        return error_response('无效的请求!')

    ret_data = upc_bks_get_course_data()
    return success_response(ret_data)


def upc_bks_get_choose_data_view(request):
    """
    URL[GET]:/data/upc/upc_bks_get_choose_data/
    """
    key = get_para_from_request_safe(request, 'key')
    if not is_valid_request(key):
        return error_response('无效的请求!')

    ret_data = upc_bks_get_choose_data()
    return success_response(ret_data)


# ---------------------------------------------------------------------------------
# 研究生数据
# ---------------------------------------------------------------------------------
def upc_yjs_get_department_data_view(request):
    """
    URL[GET]:/data/upc/upc_yjs_get_department_data/
    """
    key = get_para_from_request_safe(request, 'key')
    if not is_valid_request(key):
        return error_response('无效的请求!')

    ret_data = upc_yjs_get_department_data()
    return success_response(ret_data)


def upc_yjs_get_student_data_view(request):
    """
    URL[GET]:/data/upc/upc_yjs_get_student_data/
    """
    key = get_para_from_request_safe(request, 'key')
    if not is_valid_request(key):
        return error_response('无效的请求!')

    ret_data = upc_yjs_get_student_data()
    return success_response(ret_data)


def upc_yjs_get_course_data_view(request):
    """
    URL[GET]:/data/upc/upc_yjs_get_course_data/
    """
    key = get_para_from_request_safe(request, 'key')
    if not is_valid_request(key):
        return error_response('无效的请求!')

    ret_data = upc_yjs_get_course_data()
    return success_response(ret_data)


def upc_yjs_get_choose_data_view(request):
    """
    URL[GET]:/data/upc/upc_yjs_get_choose_data/
    """
    key = get_para_from_request_safe(request, 'key')
    if not is_valid_request(key):
        return error_response('无效的请求!')

    ret_data = upc_yjs_get_choose_data()
    return success_response(ret_data)
