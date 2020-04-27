# -*- coding:utf-8 -*-
from data_transfer.data_proxy_utils import MySQLTransferHandler
from data_transfer.utils.common_tools import cal_md5
from data_transfer.utils.datetime_utils import get_now_datetime_str, FORMAT_DATE_WITHOUT_SEPARATOR
import pymysql


db = pymysql.connect(host="192.168.21.13", port=3306, user="root", passwd="Ykt@2020", db="ykt")
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


def get_client(func):
    """
    """

    conn = MySQLTransferHandler(host="192.168.21.13",
                                    port=3306,
                                    user="root",
                                    password="Ykt@2020",
                                    database="ykt")
    print(conn)
    return conn


def query_data_to_dict_list(query_data_list_of_tuple, keys_list):
    final_list = []
    for tuple_item in query_data_list_of_tuple:
        tmp_dict = dict(zip(keys_list, tuple_item))
        final_list.append(tmp_dict)
    return final_list


def hrbeuyjs_get_department_data():
    statement = "select xymc from xyxxb"
    cursor.execute(statement)
    data_list = cursor.fetchall()
    keys_list = ["department_name"]
    final_info_list = query_data_to_dict_list(data_list, keys_list)
    return final_info_list

def hrbeuyjs_get_tra_data():
    statement = "select ssxy, ZY, bjmc, rxxn from xzbjb"
    cursor.execute(statement)
    data_list = cursor.fetchall()
    keys_list = ["department_name", "major", 'tra_classroom_name', "year"]
    final_info_list = query_data_to_dict_list(data_list, keys_list)
    return final_info_list

def hrbeuyjs_get_user_data():
    statement = "select SSXY, xzbjmc, XM, XH, sf, rxxn from qtcyb"
    cursor.execute(statement)
    data_list = cursor.fetchall()
    keys_list = ["department_name", "tra_class_name", 'name', 'number', 'user_type', 'year']
    final_info_list = query_data_to_dict_list(data_list, keys_list)
    return final_info_list

def hrbeuyjs_get_course_data(year, term):
    statement = "select SSXY, kch, kcmc, xkh, kcbjmc, jsgh, jsxm, KKXN, KKXQ from bxqkkxxb where KKXN='{}' and KKXQ='{}'".format(year, term)
    cursor.execute(statement)
    data_list = cursor.fetchall()
    keys_list = ["department_name", "course_code", "course_name", 'classroom_code', "classroom_name", 
        "teacher_number", "teacher_name", "year", "term"]
    final_info_list = query_data_to_dict_list(data_list, keys_list)
    return final_info_list

def hrbeuyjs_get_choose_data(year, term):
    statement = "select XKH, XH from bxqxkxxb where KKXN='{}' and KKXQ='{}'".format(year, term)
    cursor.execute(statement)
    data_list = cursor.fetchall()
    keys_list = ["classroom_code", "student_number"]
    final_info_list = query_data_to_dict_list(data_list, keys_list)
    return final_info_list
