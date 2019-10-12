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
    conn = MySQLTransferHandler(host="111.114.174.30",
                                port=3306,
                                user="ykt_new",
                                password="Ykt2019",
                                database="ykt")
    return conn


# ---------------------------------------------------------------------------------
# 本科生基本数据
# ---------------------------------------------------------------------------------
def nwu_bks_get_student_data():
    statement = "select XGH, XM, YX, BJMC, RXRQ, SFLB from T_RYXX"
    data_list = get_client().get_raw_data_by_statement(statement=statement, var_tuple=None)
    keys_list = ["number", "name", 'department', 'tradition_class', 'year', 'user_type']

    final_info_list = query_data_to_dict_list(data_list, keys_list)

    return final_info_list


def nwu_bks_get_course_data():
    statement = "select JSGH, JSXM, YX, KCH, KCMC, XN, XQ, XKH, BJMC from T_BKS_KCXX where XN={} and XQ={}"
    data_list = get_client().get_raw_data_by_statement(statement=statement, var_tuple=None)
    keys_list = ["number", "name", "department", 'course_code', 'course_name', 'year', 'term', 'classroom_code',
                 'classroom_name']
    user_info_data = query_data_to_dict_list(data_list, keys_list)

    return user_info_data


def nwu_bks_get_choose_data():
    statement = "select KXH, XH from T_BKS_XK"

    data_list = get_client().get_raw_data_by_statement(statement=statement, var_tuple=None)
    keys_list = ['classroom_code', "student_number"]
    final_info_list = query_data_to_dict_list(data_list, keys_list)

    return final_info_list


# ---------------------------------------------------------------------------------
# 研究生基本数据
# ---------------------------------------------------------------------------------
def nwu_yjs_get_course_data():
    statement = "select JSGH, JSXM, YX, KCH, KCMC,XN, XQ, BJMC, XKH from T_YJS_KCXX"
    data_list = get_client().get_raw_data_by_statement(statement=statement, var_tuple=None)
    keys_list = ["number", "name", "department", 'course_code', 'course_name', 'year', 'term', 'classroom_name',
                 'classroom_code']

    final_info_list = query_data_to_dict_list(data_list, keys_list)

    return final_info_list


def nwu_yjs_get_choose_data():
    statement = "select WID, XH from T_YJS_XKB"
    data_list = get_client().get_raw_data_by_statement(statement=statement, var_tuple=None)
    keys_list = ["classroom_code", 'student_number']

    final_info_list = query_data_to_dict_list(data_list, keys_list)

    return final_info_list
