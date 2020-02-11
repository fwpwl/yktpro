#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    Copyright 2013-2016 北京慕华信息科技有限公司
    
    Author: Huangsuoyuan
    Created: 16/9/27
    Description:
"""

import time


def red(s):
    return "%s[31;31m%s%s[0m" % (chr(27), str(s), chr(27))


def green(s):
    return "%s[31;32m%s%s[0m" % (chr(27), str(s), chr(27))


def yellow(s):
    return"%s[31;33m%s%s[0m" % (chr(27), str(s), chr(27))


def blue(s):
    return"%s[31;34m%s%s[0m" % (chr(27), str(s), chr(27))


def eval_with_retry(func, tip_msg, first_interact=True, interact=True,
                    retry_strategy=None, retry_interval=0, max_retry=100):

    def wrapper(*args):
        print tip_msg
        if first_interact:
            if wait_for_input(['Continue', 'Skip']) == 's':
                return 's'

        retry_times = 0
        while True:
            try:
                if func:
                    return func(*args)
                return
            except Exception, e:
                retry_times += 1
                if retry_times > max_retry:
                    raise

                if retry_strategy and not retry_strategy(e):
                    raise

                if interact:
                    print red(e)
                    print tip_msg
                    retry_or_abort = wait_for_input(['Retry', 'Abort'])

                    if retry_or_abort != 'r':
                        raise e

                time.sleep(retry_interval)
    return wrapper


def wait_for_input(options, message=''):
    options_dict = {}
    options_message_list = []
    for option in options:
        if len(option) <= 1:
            raise Exception('option size must large than 1')
        c = option[0].lower()
        if c in options_dict:
            raise Exception('duplicated option')
        options_dict[c] = option
        options_message_list.append('(%s)%s' % (c, option))

    message = '%s[%s]: ' % (message, ' / '.join(options_message_list))

    while True:
        c = raw_input(message).strip()
        if c in options_dict:
            return c

        if c == '':
            continue
        else:
            print "Unrecognized input %s " % c
