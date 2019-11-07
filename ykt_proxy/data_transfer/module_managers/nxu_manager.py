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


def get_client():
    """
    """
    conn = MySQLTransferHandler(host="127.0.0.1",
                                port=52100,
                                user="ykt",
                                password="yuketang@NXU$0951",
                                database="yuketang")
    return conn


# ---------------------------------------------------------------------------------
# 本科生基本数据
# ---------------------------------------------------------------------------------
def nxu_get_student_data():
    statement = "select dept, klass, name, sno, user_type, term from student"
    data_list = get_client().get_raw_data_by_statement(statement=statement, var_tuple=None)
    keys_list = ['department', 'tradition_class', "name", "number", 'user_type', 'year', ]

    final_info_list = query_data_to_dict_list(data_list, keys_list)

    return final_info_list


def nxu_get_teacher_data():
    statement = "select dept, name, zgh, user_type, from teacher"
    data_list = get_client().get_raw_data_by_statement(statement=statement, var_tuple=None)
    keys_list = ['department', "name", "number", 'user_type', ]

    final_info_list = query_data_to_dict_list(data_list, keys_list)

    return final_info_list


def nxu_get_course_data(term):
    statement = "select department_name, course_code, course_name, classroom_name,classroom_code, teacher_number, teacher_name , term from course where term='{}'".format(term)
    data_list = get_client().get_raw_data_by_statement(statement=statement, var_tuple=None)
    keys_list = ["department_name", "course_code", "course_name",
                 'classroom_name', 'classroom_code', 'teacher_number', 'teacher_name', 'term']
    user_info_data = query_data_to_dict_list(data_list, keys_list)

    return user_info_data


def nxu_get_choose_data(term):
    statement = "select classroom_code, student_number, term from choose where term='{}'".format(term)

    data_list = get_client().get_raw_data_by_statement(statement=statement, var_tuple=None)
    keys_list = ['classroom_code', "student_number", 'term']
    final_info_list = query_data_to_dict_list(data_list, keys_list)

    return final_info_list
