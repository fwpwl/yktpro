# -*- coding:utf-8 -*-
from data_transfer.data_proxy_utils import MySQLTransferHandler
from data_transfer.utils.common_tools import cal_md5
from data_transfer.utils.datetime_utils import get_now_datetime_str, FORMAT_DATE_WITHOUT_SEPARATOR

CONN_CLI = MySQLTransferHandler(host="113.55.14.21",
                                port=3306,
                                user="ykt",
                                password="Ykt2019",
                                database="ykt")


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

def ynu_bks_get_department_data():
    statement = "select YXDM, YXMC from BKS_YXDW"
    data_list = CONN_CLI.get_raw_data_by_statement(statement=statement, var_tuple=None)
    keys_list = ["department_code", "department_name"]
    user_info_data = query_data_to_dict_list(data_list, keys_list)

    return user_info_data


def ynu_bks_get_tra_classroom_data():
    statement = "select BJDM, YXDM, NJ, BJMC, ZYDM from BKS_BJ"
    data_list = CONN_CLI.get_raw_data_by_statement(statement=statement, var_tuple=None)
    keys_list = ["tra_classroom_code", "department_code", "year", "tra_classroom_name", "major_code"]
    user_info_data = query_data_to_dict_list(data_list, keys_list)

    return user_info_data


# ---------------------------------------------------------------------------------
# Course
# ---------------------------------------------------------------------------------

def ynu_bks_get_course_basic_data():
    statement = "select KCH, KCM, KKDWDM from BKS_KCB"
    data_list = CONN_CLI.get_raw_data_by_statement(statement=statement, var_tuple=None)
    keys_list = ["course_code", "course_name", "department_code"]
    user_info_data = query_data_to_dict_list(data_list, keys_list)

    return user_info_data


def ynu_bks_get_course_year_data():
    statement = "select XNXQDM, KCH from BKS_KKJHB"
    data_list = CONN_CLI.get_raw_data_by_statement(statement=statement, var_tuple=None)
    keys_list = ["year_str", "course_code"]
    user_info_data = query_data_to_dict_list(data_list, keys_list)

    return user_info_data


def ynu_bks_get_course_belong_data(year='2018-2019-2'):
    statement = "select XNXQDM, JSH, KCH, JXBID from BKS_SJJSB where XNXQDM={}".format(year)
    data_list = CONN_CLI.get_raw_data_by_statement(statement=statement, var_tuple=None)
    keys_list = ["year", "teacher_number", "course_code", "final_classroom_code"]
    user_info_data = query_data_to_dict_list(data_list, keys_list)

    return user_info_data


# ---------------------------------------------------------------------------------
# User
# ---------------------------------------------------------------------------------

def ynu_bks_get_student_data():
    statement = "select XH, XM, YXDM, XZNJ, ZYDM from BKS_JBXX"
    data_list = CONN_CLI.get_raw_data_by_statement(statement=statement, var_tuple=None)
    keys_list = ["number", "name", 'department_code', 'year', 'major_code']

    final_info_list = query_data_to_dict_list(data_list, keys_list)

    return final_info_list


def ynu_bks_get_teacher_data():
    statement = "select ZGH, XM, SZDWDM from BKS_JZGJBXX"
    data_list = CONN_CLI.get_raw_data_by_statement(statement=statement, var_tuple=None)
    keys_list = ["number", "name", "department_code"]

    final_info_list = query_data_to_dict_list(data_list, keys_list)

    return final_info_list


# ---------------------------------------------------------------------------------
# Choose
# ---------------------------------------------------------------------------------


# -----------------------  选课 数据 -----------------------


def ynu_bks_get_choose_data(year='2018-2019-2'):
    statement = "select XNXQDM, XH, KCH, JXBID from BKS_XKJG where XNXQDM={}".format(year)

    data_list = CONN_CLI.get_raw_data_by_statement(statement=statement, var_tuple=None)
    keys_list = ['year', 'student_number', "classroom_code", "final_classroom_code"]
    final_info_list = query_data_to_dict_list(data_list, keys_list)

    return final_info_list


# ---------------------------------------------------------------------------------
# 研究生基本数据
# ---------------------------------------------------------------------------------



def ynu_yjs_get_department_data():
    statement = "select YXDM, YXMC from YJS_YXDM"
    data_list = CONN_CLI.get_raw_data_by_statement(statement=statement, var_tuple=None)
    keys_list = ["department_code", "department_name"]
    user_info_data = query_data_to_dict_list(data_list, keys_list)

    return user_info_data


# ---------------------------------------------------------------------------------
# User
# ---------------------------------------------------------------------------------

def ynu_yjs_get_student_data():
    statement = "select XH, XM, YXDM, XZNJ from YJS_JBXX"
    data_list = CONN_CLI.get_raw_data_by_statement(statement=statement, var_tuple=None)
    keys_list = ["number", "name", 'department_code', 'year']

    final_info_list = query_data_to_dict_list(data_list, keys_list)

    return final_info_list


def ynu_yjs_get_teacher_data():
    statement = "select ZGH, XM, SZDWDM from YJS_JZGJBXX"
    data_list = CONN_CLI.get_raw_data_by_statement(statement=statement, var_tuple=None)
    keys_list = ["number", "name", "department_code"]

    final_info_list = query_data_to_dict_list(data_list, keys_list)

    return final_info_list


def ynu_yjs_get_course_basic_data():
    statement = "select KCDM, KCMC, KKDW from YJS_KCB"
    data_list = CONN_CLI.get_raw_data_by_statement(statement=statement, var_tuple=None)
    keys_list = ["course_code", "course_name", "department_code"]
    user_info_data = query_data_to_dict_list(data_list, keys_list)

    return user_info_data


def ynu_yjs_get_course_data(year='20191'):
    statement = "select XNXQDM, KCDM, KCMC, BJDM, RKJSZGHXM from YJS_QXKB where XNXQDM={}".format(year)
    data_list = CONN_CLI.get_raw_data_by_statement(statement=statement, var_tuple=None)
    keys_list = ["year", "course_code", "course_name", "final_classroom_code", "teacher_info"]
    user_info_data = query_data_to_dict_list(data_list, keys_list)

    return user_info_data


def ynu_yjs_get_choose_data(year='20191'):
    statement = "select XNXQDM, XH, BJDM from YJS_XKJG where XNXQDM={}".format(year)
    data_list = CONN_CLI.get_raw_data_by_statement(statement=statement, var_tuple=None)
    keys_list = ["year", "student_number", "final_classroom_code"]
    user_info_data = query_data_to_dict_list(data_list, keys_list)

    return user_info_data