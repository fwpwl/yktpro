# -*- coding:utf-8 -*-
"""
网络相关小工具
"""
import json

import os
from django.contrib.auth.models import AnonymousUser
from django.http import HttpResponse
from django.test import Client
from django.test.client import MULTIPART_CONTENT


def get_user_from_request(request):
    """
    从request中获取user,获取user调用这个函数
    """
    return request.user if not isinstance(request.user, AnonymousUser) else None


def get_para_dict_from_request(request):
    """

    """
    try:
        return json.loads(request.body)
    except:
        return {}


def json_http_response(content):
    """

    """
    return HttpResponse(json.dumps(content), content_type="application/json;encoding=utf-8")


def file_http_response(file_path):
    """
    文件返回HttpResponse
    """
    from rexec import FileWrapper
    wrapper = FileWrapper(file(file_path))
    response = HttpResponse(wrapper, content_type='text/plain')
    response['Content-Disposition'] = 'attachment; filename=%s' % os.path.basename(file_path)
    response['Content-Length'] = os.path.getsize(file_path)
    return response


def query_dict_to_dict(query_dict):
    """
    将QueryDict转化成dict，request.GET, request.POST转化成dict
    """
    result = {}
    for k, v in query_dict.items():
        if len(v) > 0:
            result[k] = v
    return result


class CustomClient(Client):
    """
    自定义的json格式模拟testcase客户端
    """

    def __init__(self):
        super(CustomClient, self).__init__()

    def json_post(self, path, data={}, content_type=MULTIPART_CONTENT, follow=False, **extra):
        response = self.post(path, data, content_type, follow, **extra)
        return json.loads(response.content)

    def json_get(self, path, data={}, follow=False, **extra):
        response = self.get(path, data, follow, **extra)
        return json.loads(response.content)


def get_para_from_request(request, para, default_value=''):
    """

    """
    value = default_value
    if request.method == 'POST':
        value = request.POST.get(para)
    elif request.method == 'GET':
        value = request.GET.get(para)
    if not value:
        return default_value
    return value


def get_para_from_request_safe(request, para, default_value=''):
    """
    我们的老流程是:
    1.如果是POST， 则将参数放在Body里面;
    2.如果是GET, 则正常放在URL后面;
    """
    value = default_value

    if request.method == 'POST':
        value = request.POST.get(para)
        if not value:
            para_dict = get_para_dict_from_request(request)
            value = para_dict.get(para)
    elif request.method == 'GET':
        value = request.GET.get(para)

    if not value:
        return default_value

    return value


def parse_json_response(json_response):
    """

    """
    return json.loads(json_response.text)


def get_request_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')

    return ip
