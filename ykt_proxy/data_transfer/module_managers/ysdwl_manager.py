# -*- coding:utf-8 -*-
from data_transfer.data_proxy_utils import MySQLTransferHandler
from data_transfer.utils.common_tools import cal_md5
from data_transfer.utils.datetime_utils import get_now_datetime_str, FORMAT_DATE_WITHOUT_SEPARATOR
import pymysql

db = pymysql.connect(host="127.0.0.1", port=3306, user="wlykt", passwd="ykt#2020", db="test")
cursor = db.cursor()

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

# ---------------------------------------------------------------------------------
# 本科生基本数据
# ---------------------------------------------------------------------------------

def ysdwl_get_department_data():
    statement = "select XYMC from xyxxb"
    cursor.execute(statement)
    data_list = cursor.fetchall()
    keys_list = ["department_name"]
    final_info_list = query_data_to_dict_list(data_list, keys_list)
    return final_info_list


def ysdwl_get_tra_classroom_data():
    statement = "select xymc, bjmc, nj from xzbjb"
    cursor.execute(statement)
    data_list = cursor.fetchall()
    keys_list = ["department_name", 'tra_classroom_name', "year"]
    final_info_list = query_data_to_dict_list(data_list, keys_list)

    return final_info_list


def ysdwl_get_user_data():
    statement = "select xy1, xzb1, xm1, xh1, js, dqszj1 from qtcyb"
    cursor.execute(statement)
    data_list = cursor.fetchall()
    keys_list = ["department_name", "tra_class_name", 'name', 'number', 'user_type', 'year']
    final_info_list = query_data_to_dict_list(data_list, keys_list)

    return final_info_list


def ysdwl_get_course_data(year, term):
    statement = "select kkxy, kch, xkkh, jszgh, jsxm, kcmc, bjmc, xn, xq from bxtkkxxb XN='{}' and XQ='{}'".format(year, term)
    print(statement)
    cursor.execute(statement)
    data_list = cursor.fetchall()
    keys_list = ["department_name", "course_code", "classroom_code", 'teacher_number', 'teacher_name', 'course_name', 'classroom_name', "year", 'term']
    user_info_data = query_data_to_dict_list(data_list, keys_list)
    return user_info_data


def ysdwl_get_choose_data(year, term):
    statement = "select xkkh, xh from xsxkb xn={} and xq={}".format(year, term)
    print(statement)
    cursor.execute(statement)
    data_list = cursor.fetchall()
    keys_list = ['classroom_code', 'student_number']
    final_info_list = query_data_to_dict_list(data_list, keys_list)
    return final_info_list
