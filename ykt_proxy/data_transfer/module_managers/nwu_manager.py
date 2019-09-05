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
        conn = MySQLTransferHandler(host="111.114.174.30",
                                    port=3306,
                                    user="ykt_new",
                                    password="Ykt2019",
                                    database="ykt")
        return func(conn)

    return wrapper


# ---------------------------------------------------------------------------------
# 本科生基本数据
# ---------------------------------------------------------------------------------

@get_client
def nwu_bks_get_department_data(db):
    statement = "select code, department_name  from bks_departmentz_info"
    data_list = db.get_raw_data_by_statement(statement=statement, var_tuple=None)
    keys_list = ["department_code", "department_name"]
    user_info_data = query_data_to_dict_list(data_list, keys_list)

    return user_info_data


@get_client
def nwu_bks_get_tra_classroom_data(db):
    statement = "select yxdm, bh, bjmc from bks_class_info"
    data_list = db.get_raw_data_by_statement(statement=statement, var_tuple=None)
    keys_list = ["department_code", "bh", 'name']

    final_info_list = query_data_to_dict_list(data_list, keys_list)

    return final_info_list


@get_client
def nwu_bks_get_student_data(db):
    statement = "select xh, xm, yx, bh from bks_student_info"
    data_list = db.get_raw_data_by_statement(statement=statement, var_tuple=None)
    keys_list = ["number", "name", 'department_code', 'tradition_class_id']

    final_info_list = query_data_to_dict_list(data_list, keys_list)

    return final_info_list


@get_client
def nwu_bks_get_teacher_data(db):
    statement = "select gh, xm, dwmc, id, kcmc, xn, xq from bks_teacher_course_info"
    data_list = db.get_raw_data_by_statement(statement=statement, var_tuple=None)
    keys_list = ["number", "name", "department", 'course_code', 'course_name', 'year', 'term']
    user_info_data = query_data_to_dict_list(data_list, keys_list)

    return user_info_data


@get_client
def nwu_bks_get_choose_data(db):
    statement = "select id, kcbh, gh,xh from bks_choose_course"

    data_list = db.get_raw_data_by_statement(statement=statement, var_tuple=None)
    keys_list = ['course_code', 'kcbh', "teacher_number", "student_number"]
    final_info_list = query_data_to_dict_list(data_list, keys_list)

    return final_info_list


# ---------------------------------------------------------------------------------
# 研究生基本数据
# ---------------------------------------------------------------------------------
@get_client
def nwu_yjs_get_department_data(db):
    statement = "select id, BH, MC from yjs_department"
    data_list = db.get_raw_data_by_statement(statement=statement, var_tuple=None)
    keys_list = ["department_id", "department_code", "department_name"]
    user_info_data = query_data_to_dict_list(data_list, keys_list)

    return user_info_data


@get_client
def nwu_yjs_get_student_data(db):
    statement = "select department, code, name, type, year, team from yjs_student_info"
    data_list = db.get_raw_data_by_statement(statement=statement, var_tuple=None)
    keys_list = ["department_code", "number", "name", "type", "year", "term"]

    final_info_list = query_data_to_dict_list(data_list, keys_list)

    return final_info_list


@get_client
def nwu_yjs_get_course_data(db):
    statement = "select gh, xm, dwmc, id, kcmc, xn, xq from yjs_teacher_course_info"
    data_list = db.get_raw_data_by_statement(statement=statement, var_tuple=None)
    keys_list = ["number", "name", "department", 'course_code', 'course_name', 'year', 'term']

    final_info_list = query_data_to_dict_list(data_list, keys_list)

    return final_info_list


@get_client
def nwu_yjs_get_choose_data(db):
    statement = "select id, xh, kcbh, gh from yjs_choose_course"
    data_list = db.get_raw_data_by_statement(statement=statement, var_tuple=None)
    keys_list = ["course_code", "student_number", "kcbh", 'teacher_number']

    final_info_list = query_data_to_dict_list(data_list, keys_list)

    return final_info_list
