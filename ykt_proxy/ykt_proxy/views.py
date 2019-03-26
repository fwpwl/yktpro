# coding:utf-8

from django.http import HttpResponse


def test_server(request):
    return HttpResponse("connection success! hello,")
