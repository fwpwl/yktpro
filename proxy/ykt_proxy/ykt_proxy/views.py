# coding:utf-8

from django.http import HttpResponse


def test_server(request):
    """
    URL[GET]:/test_server/
    """
    return HttpResponse("connection success! hello,")
