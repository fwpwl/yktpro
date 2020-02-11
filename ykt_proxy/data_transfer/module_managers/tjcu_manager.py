# -*- coding:utf-8 -*-
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


def get_client(func):
    """
    """

    def wrapper():
        conn = MySQLTransferHandler(host="127.0.0.1",
                                    port=3306,
                                    user="root",
                                    password="Ykt2020$",
                                    database="ykt")
        return func(conn)

    return wrapper


# ---------------------------------------------------------------------------------
# 本科生基本数据
# ---------------------------------------------------------------------------------

@get_client
def tjcu_get_department_data(db):
    statement = "select XYDM, XYMC  from xyxxb"
    data_list = db.get_raw_data_by_statement(statement=statement, var_tuple=None)
    keys_list = ["department_code", "department_name"]
    user_info_data = query_data_to_dict_list(data_list, keys_list)

    return user_info_data


@get_client
def tjcu_get_tra_classroom_data(db):
    statement = "select ssxy, zy, bjmc, rxxn from xzbjb"
    data_list = db.get_raw_data_by_statement(statement=statement, var_tuple=None)
    keys_list = ["department_name", "major", 'tra_classroom_name', "year"]

    final_info_list = query_data_to_dict_list(data_list, keys_list)

    return final_info_list


@get_client
def tjcu_get_user_data(db):
    statement = "select ssxy, xzbjmc, xm, xh, sf, rxxn from qtcyb"
    data_list = db.get_raw_data_by_statement(statement=statement, var_tuple=None)
    keys_list = ["department_name", "tra_classroom_name", 'name', 'number', 'user_type', 'year']

    final_info_list = query_data_to_dict_list(data_list, keys_list)

    return final_info_list


@get_client
def tjcu_get_course_data(db):
    statement = "select ssxy, kch, xkh, jsgh, jsxm, kcmc, kcbjmc, kkxn, kkxq from bxqkkxxb"
    data_list = db.get_raw_data_by_statement(statement=statement, var_tuple=None)
    keys_list = ["department_name", "course_code", "classroom_code", 'teacher_number', 'teacher_name', 'course_name',
                 'classroom_name', "year", 'term']
    user_info_data = query_data_to_dict_list(data_list, keys_list)

    return user_info_data


@get_client
def tjcu_get_choose_data(db):
    statement = "select xkh, xh from bxqxkxxb"
    data_list = db.get_raw_data_by_statement(statement=statement, var_tuple=None)

    keys_list = ['classroom_code', 'teacher_number']
    final_info_list = query_data_to_dict_list(data_list, keys_list)

    return final_info_list
