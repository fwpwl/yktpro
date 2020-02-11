# -*- coding: utf-8 -*-

import os


def load_env_variable(var_name, default=None):
    var_value = os.getenv(var_name)
    if not var_value:
        if default:
            return default
        raise Exception('Cannot find env variable: ' + var_name)
    return var_value
