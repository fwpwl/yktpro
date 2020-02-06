# -*- coding: utf-8 -*-
import hashlib
import hmac
from base64 import encodestring
from django.conf import settings

from django.utils.crypto import constant_time_compare
from django.utils import six
from django.utils.encoding import force_bytes

if six.PY3:
    from urllib.request import urlencode, pathname2url
else:
    from urllib import urlencode, pathname2url


def _standard_url(url_query):
    return url_query.replace('+', '%20').replace('*', '%2A').replace('%7E', '~')


def check_signature(**params):
    if 'signature' not in params:
        return False
    new_signature = make_signature(**params)
    return constant_time_compare(force_bytes(params["signature"]), force_bytes(new_signature))


def make_signature(**params):
    sign_data = [(k, v) for k, v in params.items() if k != 'signature' or k.startswith("__")]
    sorted_parameters = sorted(sign_data, key=lambda kv: kv[0])
    sorted_query_string = _standard_url(urlencode(sorted_parameters))
    string_to_sign = _standard_url(pathname2url(sorted_query_string))
    h = hmac.new(settings.YKT_ACCESS_KEY, string_to_sign, hashlib.sha1)
    signature = encodestring(h.digest()).strip()
    return signature

