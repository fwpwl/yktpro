# -*- coding:utf-8 -*-
from data_transfer.data_proxy_utils import OracleTransferHandler


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
        conn = OracleTransferHandler(connect_str="user_yuketang/user_yuketang@172.16.8.70:1521/icdc")
        return func(conn)

    return wrapper


@get_client
def zufe_get_bks_data(db):
    statement = "select XH,  XM,  YXSH,  ZYM,  SZBH,  SZNJ,  RXNY,  XZ,  XSDQZTM from icdc_gx.V_XSJBXX_BKS"
    data_list = db.get_raw_data_by_statement(statement=statement, var_tuple=None)
    keys_list = ["number", "name", 'department_code', 'major_code', 'tra_class_code', 'term',
                 'come_in_year', 'xuezhi', 'current_status_code']
    user_info_data = query_data_to_dict_list(data_list, keys_list)
    print user_info_data

    return user_info_data


@get_client
def zufe_get_yjs_data(db):
    statement = "select XH,  XM,  YXSH,  ZYM,  SZBH,  SZNJ,  RXNY,  XZ,  XSDQZTM from icdc_gx.V_XSJBXX_YJS"
    data_list = db.get_raw_data_by_statement(statement=statement, var_tuple=None)
    keys_list = ["number", "name", 'department_code', 'major_code', 'tra_class_code', 'term',
                 'come_in_year', 'xuezhi', 'current_status_code']

    final_info_list = query_data_to_dict_list(data_list, keys_list)

    return final_info_list


@get_client
def zufe_get_teacher_data(db):
    statement = "select GH,  XM,  DQZTM from icdc_gx.V_JZGJBXX"
    data_list = db.get_raw_data_by_statement(statement=statement, var_tuple=None)
    keys_list = ["number", "name", "status"]

    final_info_list = query_data_to_dict_list(data_list, keys_list)

    return final_info_list


# -----------------------  学院.专业.班级 数据 -----------------------
@get_client
def zufe_get_department_data(db):
    statement = "select UNIT_ID, UNIT_NAME from icdc_gx.V_ZZJGXX"
    data_list = db.get_raw_data_by_statement(statement=statement, var_tuple=None)
    keys_list = ["department_id", "department_name"]

    final_info_list = query_data_to_dict_list(data_list, keys_list)

    return final_info_list


@get_client
def zufe_get_bks_major_data(db):
    statement = "select ZYH,  ZYMC,  ZYJC  from icdc_gx.V_ZYXX_BKS"
    data_list = db.get_raw_data_by_statement(statement=statement, var_tuple=None)
    keys_list = ["major_code", "major_name", 'major_short_name']

    final_info_list = query_data_to_dict_list(data_list, keys_list)

    return final_info_list


@get_client
def zufe_get_yjs_major_data(db):
    statement = "select ZYH,  ZYMC,  ZYJC  from icdc_gx.V_ZYXX_YJS"

    data_list = db.get_raw_data_by_statement(statement=statement, var_tuple=None)
    keys_list = ["major_code", "major_name", 'major_short_name']

    final_info_list = query_data_to_dict_list(data_list, keys_list)

    return final_info_list


@get_client
def zufe_get_tradition_class_data(db):
    statement = "select DWH, BH,  BJ,  SSNJ, SSZY  from icdc_gx.V_BJXX_BKS"

    data_list = db.get_raw_data_by_statement(statement=statement, var_tuple=None)
    keys_list = ["department_code", "classroom_code", "classroom_name", 'term', 'major_code']

    final_info_list = query_data_to_dict_list(data_list, keys_list)

    return final_info_list


# -----------------------  选课 数据 -----------------------
@get_client
def zufe_get_bks_choose_classroom_data(db):
    statement = "select  XH,   XKKH,  KCB from icdc_gx.V_PKXX_BKS"

    data_list = db.get_raw_data_by_statement(statement=statement, var_tuple=None)
    keys_list = ["student_number", "classroom_code", 'classroom_table']

    final_info_list = query_data_to_dict_list(data_list, keys_list)

    return final_info_list


@get_client
def zufe_get_teacher_choose_classroom_data(db):
    statement = "select  XKKCH,   KCH,  SJKCMC,  KKYX, JSGH, JSXM from icdc_gx.V_PKXX_JZ"

    data_list = db.get_raw_data_by_statement(statement=statement, var_tuple=None)
    keys_list = ["course_code", "classroom_code", 'course_name',
                 'department_code', 'teacher_number', 'teacher_name']
    final_info_list = query_data_to_dict_list(data_list, keys_list)

    return final_info_list


@get_client
def zufe_get_yjs_choose_classroom_data(db):
    statement = "select  XH,   XN,  XQ,  RKJSGH, KCDM, KCMC,SKBJ, XKH from icdc_gx.V_PKXX_YJS"

    data_list = db.get_raw_data_by_statement(statement=statement, var_tuple=None)
    keys_list = ["student_number", "year", 'term',
                 'teacher_number', 'course_code', 'course_name', 'tra_classroom', 'classroom_code']
    final_info_list = query_data_to_dict_list(data_list, keys_list)

    return final_info_list
