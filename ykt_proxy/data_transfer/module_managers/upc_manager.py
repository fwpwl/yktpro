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
        conn = MySQLTransferHandler(host="202.204.193.168",
                                    port=3306,
                                    user="ykt_new",
                                    password="Yktnew2019",
                                    database="ykt")
        return func(conn)

    return wrapper


@get_client
def upc_get_department_data(db):
    statement = "select XYMC, XYDM from T_BZKS_XY"
    data_list = db.get_raw_data_by_statement(statement=statement, var_tuple=None)
    keys_list = ["department_code", "department_name"]
    user_info_data = query_data_to_dict_list(data_list, keys_list)

    return user_info_data


@get_client
def upc_get_tradition_classroom_data(db):
    statement = "select BJMC, SSXY, RXXN from XZBJB"
    data_list = db.get_raw_data_by_statement(statement=statement, var_tuple=None)
    keys_list = ["tra_class_name", "department_name", "year"]
    user_info_data = query_data_to_dict_list(data_list, keys_list)

    return user_info_data


@get_client
def upc_get_student_data(db):
    statement = "select XH, RXXN, SSXY, XZBJMC, SF, XM from XSXXB"
    data_list = db.get_raw_data_by_statement(statement=statement, var_tuple=None)
    keys_list = ["number", "year", 'department_name', 'tra_class_name', 'user_type', 'name']

    final_info_list = query_data_to_dict_list(data_list, keys_list)

    return final_info_list


@get_client
def upc_get_teacher_data(db):
    statement = "select ZGH, XM, SSXY, SF from JSXXB"
    data_list = db.get_raw_data_by_statement(statement=statement, var_tuple=None)
    keys_list = ["number", "name", "department", "user_type"]

    final_info_list = query_data_to_dict_list(data_list, keys_list)

    return final_info_list


# -----------------------  选课 数据 -----------------------
@get_client
def upc_get_course_data(db):
    statement = "select KCMC, KCH, KCBJMC, KXH, JSGH, SSXY, KKXN, KKXQ from BXQKKXXB"
    data_list = db.get_raw_data_by_statement(statement=statement, var_tuple=None)
    keys_list = ["number", "name", 'department_name', 'user_type', 'year', 'term',
                 'tra_class_name']

    final_info_list = query_data_to_dict_list(data_list, keys_list)

    return final_info_list


@get_client
def upc_get_choose_data(db):
    statement = "select XH, KXH from BXQXKSJB"

    data_list = db.get_raw_data_by_statement(statement=statement, var_tuple=None)
    keys_list = ['student_number', "classroom_code"]
    final_info_list = query_data_to_dict_list(data_list, keys_list)

    return final_info_list
