# -*- coding:utf-8 -*-
from data_transfer.data_proxy_utils import MySQLTransferHandler
from data_transfer.utils.common_tools import cal_md5
from data_transfer.utils.datetime_utils import get_now_datetime_str, FORMAT_DATE_WITHOUT_SEPARATOR
import pymssql
import datetime

db = pymssql.connect(host='121.195.154.168',user='sjgx',password='bjhg2019!@',database='pubs')
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

def grabuct_get_department_data():
    statement = "select xsmc from xyxxb"
    cursor.execute(statement)
    data_list = cursor.fetchall()
    keys_list = ["department_name"]
    final_info_list = query_data_to_dict_list(data_list, keys_list)
    return final_info_list


def grabuct_get_tra_classroom_data():
    year = datetime.datetime.now().year
    return ["北京化工大学研究生院", "研究生"]


def grabuct_get_user_data():
    statement = "select ssxy, xm, xh, sf, rxxn from qtcyb"
    cursor.execute(statement)
    data_list = cursor.fetchall()
    keys_list = ["department_name", 'name', 'number', 'user_type', 'year']
    final_info_list = query_data_to_dict_list(data_list, keys_list)
    return final_info_list


def grabuct_get_course_data(year, term):
    statement = "select ssxy, xkh, jsgh, jsxm, kcmc, kcbjmc from bxqkkxxb where kkxn='{}' and kkxq='{}'".format(year, term)
    cursor.execute(statement)
    data_list = cursor.fetchall()
    keys_list = ["department_name", "classroom_code", 'teacher_number', 'teacher_name', 'course_name', 'classroom_name']
    user_info_data = query_data_to_dict_list(data_list, keys_list)
    return user_info_data


def grabuct_get_choose_data(year, term):
    statement = "select bjid, xh from bxqxkxxb where kkxn='{}' and kkxq='{}'".format(year, term)
    cursor.execute(statement)
    data_list = cursor.fetchall()
    keys_list = ['classroom_code', 'student_number']
    final_info_list = query_data_to_dict_list(data_list, keys_list)
    return final_info_list
