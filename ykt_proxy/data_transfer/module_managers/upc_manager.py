# -*- coding:utf-8 -*-
import json

import requests

from data_transfer.data_proxy_utils import MySQLTransferHandler
from data_transfer.utils.common_tools import cal_md5
from data_transfer.utils.datetime_utils import get_now_datetime_str, FORMAT_DATE_WITHOUT_SEPARATOR


def is_valid_request(key):
    """

    """
    if not key or key != cal_md5(get_now_datetime_str(FORMAT_DATE_WITHOUT_SEPARATOR)):
        return False
    return True


def query_data_to_dict_list(query_data_list_of_tuple, keys_list):
    final_list = []
    for tuple_item in query_data_list_of_tuple:
        tmp_dict = dict(zip(keys_list, tuple_item))
        final_list.append(tmp_dict)
    return final_list


def get_client():
    """
    """
    conn = MySQLTransferHandler(host="202.204.193.168",
                                port=3306,
                                user="ykt_new",
                                password="Yktnew2019",
                                database="ykt")
    return conn


def is_user_valid(user_name, password):
    """
    PARA:
    user_name='1582'
    password='pf170910'
    """
    verify_url = 'http://202.204.193.169/login.php'
    client = requests.Session()
    login_data = {"username": user_name,
                  "password": password}
    response = client.post(verify_url, data=login_data, timeout=10)
    result_dict = json.loads(response.text)
    if result_dict.get('message') == u'登陆成功' and int(result_dict.get('error_code')) == 0:
        return True
    return False


# ---------------------------------------------------------------------------------
# 本科生数据
# ---------------------------------------------------------------------------------
def upc_bks_get_department_data():
    statement = "select XYMC, XYDM from T_DW"
    data_list = get_client().get_raw_data_by_statement(statement=statement, var_tuple=None)
    keys_list = ["department_name", "department_code"]
    user_info_data = query_data_to_dict_list(data_list, keys_list)

    return user_info_data


def upc_bks_get_tradition_classroom_data():
    statement = "select BJMC, SSXY, RXXN from T_BZKS_BJ"
    data_list = get_client().get_raw_data_by_statement(statement=statement, var_tuple=None)
    keys_list = ["tra_class_name", "department_name", "year"]
    user_info_data = query_data_to_dict_list(data_list, keys_list)

    return user_info_data


def upc_bks_get_student_data():
    statement = "select XH, RXXN, SSXY, XZBJMC, SF, XM from T_BZKS"
    data_list = get_client().get_raw_data_by_statement(statement=statement, var_tuple=None)
    keys_list = ["number", "year", 'department_name', 'tra_class_name', 'user_type', 'name']

    final_info_list = query_data_to_dict_list(data_list, keys_list)

    return final_info_list


def upc_bks_get_teacher_data():
    statement = "select ZGH, XM, SSXY, SF from T_JZG"
    data_list = get_client().get_raw_data_by_statement(statement=statement, var_tuple=None)
    keys_list = ["number", "name", "department", "user_type"]

    final_info_list = query_data_to_dict_list(data_list, keys_list)

    return final_info_list


# -----------------------  选课 数据 -----------------------
def upc_bks_get_course_data():
    statement = "select KCMC, KCH, KCBJMC, KXH, JSGH, SSXY, KKXN, KKXQ from T_BZKS_KKXX"
    data_list = get_client().get_raw_data_by_statement(statement=statement, var_tuple=None)
    keys_list = ["course_name", "course_code", 'classroom_code', 'classroom_series_code', 'teacher_number',
                 'department_code', 'year', 'term']

    final_info_list = query_data_to_dict_list(data_list, keys_list)

    return final_info_list


def upc_bks_get_choose_data():
    statement = "select XH, KXH from T_BZKS_XK"

    data_list = get_client().get_raw_data_by_statement(statement=statement, var_tuple=None)
    keys_list = ['student_number', "classroom_code"]
    final_info_list = query_data_to_dict_list(data_list, keys_list)

    return final_info_list


# ---------------------------------------------------------------------------------
# 研究生数据
# ---------------------------------------------------------------------------------


def upc_yjs_get_department_data():
    statement = "select XYMC, XYDM from T_DW"
    data_list = get_client().get_raw_data_by_statement(statement=statement, var_tuple=None)
    keys_list = ["department_name", "department_code"]
    user_info_data = query_data_to_dict_list(data_list, keys_list)

    return user_info_data


def upc_yjs_get_student_data():
    statement = "select XH, RXXN, SF, XM, YX  from T_YJS"
    data_list = get_client().get_raw_data_by_statement(statement=statement, var_tuple=None)
    keys_list = ["number", "year", 'user_type', 'name', 'department_code']

    final_info_list = query_data_to_dict_list(data_list, keys_list)

    return final_info_list


def upc_yjs_get_course_data():
    statement = "select KCMC, KCH, KCBJMC, JSGH, SSXY, KKXN, KKXQ from T_YJS_KKXX"
    data_list = get_client().get_raw_data_by_statement(statement=statement, var_tuple=None)
    keys_list = ["course_name", "course_code", 'classroom_code', 'teacher_number',
                 'department_code', 'year', 'term']

    final_info_list = query_data_to_dict_list(data_list, keys_list)

    return final_info_list


def upc_yjs_get_choose_data():
    statement = "select XH, KXH from T_YJS_XK"

    data_list = get_client().get_raw_data_by_statement(statement=statement, var_tuple=None)
    keys_list = ['student_number', "classroom_code"]
    final_info_list = query_data_to_dict_list(data_list, keys_list)

    return final_info_list