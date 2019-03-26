# coding:utf-8

import json
import traceback

from django.http import HttpResponse, HttpResponseForbidden

from data_transfer.module_managers.fzxy_manager import fzxy_proxy


def get_all_data_view(request):
    try:
        post_vars = json.loads(request.body)
        if not post_vars:
            return HttpResponseForbidden()

        ret_data = fzxy_proxy.get_all_data(**post_vars)
        result_dict = {
            "success": True,
            "msg": "",
            "data": {
                ret_data
            }
        }
    except:
        result_dict = {
            "success": False,
            "msg": traceback.format_exc(),
            "data": {}
        }
    return HttpResponse(json.dumps(result_dict), content_type="application/json;encoding=utf-8")


def get_university_data_view(request):
    try:
        post_vars = json.loads(request.body)
        if not post_vars:
            return HttpResponseForbidden()

        ret_data = fzxy_proxy.get_university_data(**post_vars)
        result_dict = {
            "success": True,
            "msg": "",
            "data": {
                "university": ret_data
            }
        }
    except:
        result_dict = {
            "success": False,
            "msg": traceback.format_exc(),
            "data": {}
        }
    return HttpResponse(json.dumps(result_dict), content_type="application/json;encoding=utf-8")


def get_department_data_view(request):
    try:
        post_vars = json.loads(request.body)
        if not post_vars:
            return HttpResponseForbidden()

        ret_data = fzxy_proxy.get_department_data(**post_vars)
        result_dict = {
            "success": True,
            "msg": "",
            "data": {
                "department": ret_data
            }
        }
    except:
        result_dict = {
            "success": False,
            "msg": traceback.format_exc(),
            "data": {}
        }
    return HttpResponse(json.dumps(result_dict), content_type="application/json;encoding=utf-8")


def get_tradition_class_data_view(request):
    try:
        post_vars = json.loads(request.body)
        if not post_vars:
            return HttpResponseForbidden()

        ret_data = fzxy_proxy.get_tradition_class_data(**post_vars)
        result_dict = {
            "success": True,
            "msg": "",
            "data": {
                "tradition_class": ret_data
            }
        }
    except:
        result_dict = {
            "success": False,
            "msg": traceback.format_exc(),
            "data": {}
        }
    return HttpResponse(json.dumps(result_dict), content_type="application/json;encoding=utf-8")


def get_user_map_data_view(request):
    try:
        post_vars = json.loads(request.body)
        if not post_vars:
            return HttpResponseForbidden()
        ret_data = fzxy_proxy.get_user_map_data(**post_vars)
        result_dict = {
            "success": True,
            "msg": "",
            "data": {
                "user_map": ret_data
            }
        }
    except:
        result_dict = {
            "success": False,
            "msg": traceback.format_exc(),
            "data": {}
        }
    return HttpResponse(json.dumps(result_dict), content_type="application/json;encoding=utf-8")


def get_course_class_data_view(request):
    try:
        post_vars = json.loads(request.body)
        if not post_vars:
            return HttpResponseForbidden()
        ret_data = fzxy_proxy.get_course_class_data(**post_vars)
        result_dict = {
            "success": True,
            "msg": "",
            "data": {
                "course_class": ret_data
            }
        }
    except:
        result_dict = {
            "success": False,
            "msg": traceback.format_exc(),
            "data": {}
        }
    return HttpResponse(json.dumps(result_dict), content_type="application/json;encoding=utf-8")


def get_choose_course_data_view(request):
    try:
        post_vars = json.loads(request.body)
        if not post_vars:
            return HttpResponseForbidden()
        ret_data = fzxy_proxy.get_choose_course_data(**post_vars)
        result_dict = {
            "success": True,
            "msg": "",
            "data": {
                "choose_course": ret_data
            }
        }
    except:
        result_dict = {
            "success": False,
            "msg": traceback.format_exc(),
            "data": {}
        }
    return HttpResponse(json.dumps(result_dict), content_type="application/json;encoding=utf-8")
