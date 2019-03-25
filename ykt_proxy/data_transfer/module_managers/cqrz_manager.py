# -*- coding:utf-8 -*-
import psycopg2

from data_transfer.data_proxy_utils import DataProxyBase
from data_transfer.data_proxy_utils import OracleTransferHandler


class CqrzDataProxy(DataProxyBase):
    """

    """

    def __init__(self):
        self.db = OracleTransferHandler(connect_str="user_yuketang/user_yuketang@172.16.8.70:1521/icdc")

    def query_data_to_dict(self, query_data, keys):
        result_dict = {}
        for i, item in enumerate(query_data):
            item = "" if not item else item
            result_dict.update({keys[i]: item})
        return result_dict

    # -----------------------  用户信息 -----------------------
    def get_bks_data(self, *args, **kwargs):
        statement = "select XH,  XM,  YXSH,  ZYM,  SZBH,  SZNJ,  RXNY,  XZ,  XSDQZTM from icdc_gx.V_XSJBXX_BKS"
        ret_list = []
        data_list = self.db.get_raw_data_by_statement(statement=statement, var_tuple=None)
        for data in data_list:
            keys_list = ["number", "name", 'department_code', 'major_code', 'tra_class_code', 'term',
                         'come_in_year', 'xuezhi', 'current_status_code']
            ret_list.append(self.query_data_to_dict(data, keys=keys_list))
        return ret_list

    def get_yjs_data(self, *args, **kwargs):
        statement = "select XH,  XM,  YXSH,  ZYM,  SZBH,  SZNJ,  RXNY,  XZ,  XSDQZTM from icdc_gx.V_XSJBXX_YJS"
        ret_list = []
        data_list = self.db.get_raw_data_by_statement(statement=statement, var_tuple=None)
        for data in data_list:
            keys_list = ["number", "name", 'department_code', 'major_code', 'tra_class_code', 'term',
                         'come_in_year', 'xuezhi', 'current_status_code']
            ret_list.append(self.query_data_to_dict(data, keys=keys_list))
        return ret_list

    def get_teacher_data(self, *args, **kwargs):
        statement = "select GH,  XM,  from icdc_gx.V_JZGJBXX"
        ret_list = []
        data_list = self.db.get_raw_data_by_statement(statement=statement, var_tuple=None)
        for data in data_list:
            keys_list = ["number", "name"]
            ret_list.append(self.query_data_to_dict(data, keys=keys_list))
        return ret_list

    # -----------------------  学院.专业.班级 数据 -----------------------
    def get_department_data(self, *args, **kwargs):
        statement = "select UNIT_ID, UNIT_NAME from icdc_gx.V_ZZJGXX"
        ret_list = []
        data_list = self.db.get_raw_data_by_statement(statement=statement, var_tuple=None)
        for data in data_list:
            keys_list = ["department_id", "department_name"]
            ret_list.append(self.query_data_to_dict(data, keys=keys_list))
        return ret_list

    def get_bks_major_data(self, *args, **kwargs):
        statement = "select ZYH,  ZYMC,  ZYJC  from icdc_gx.V_ZYXX_BKS"
        ret_list = []
        data_list = self.db.get_raw_data_by_statement(statement=statement, var_tuple=None)
        for data in data_list:
            keys_list = ["major_code", "major_name", 'major_short_name']
            ret_list.append(self.query_data_to_dict(data, keys=keys_list))
        return ret_list

    def get_yjs_major_data(self, *args, **kwargs):
        statement = "select ZYH,  ZYMC,  ZYJC  from icdc_gx.V_ZYXX_YJS"
        ret_list = []
        data_list = self.db.get_raw_data_by_statement(statement=statement, var_tuple=None)
        for data in data_list:
            keys_list = ["major_code", "major_name", 'major_short_name']
            ret_list.append(self.query_data_to_dict(data, keys=keys_list))
        return ret_list

    def get_tradition_class_data(self, *args, **kwargs):
        statement = "select DWH, BH,  BJ,  SSNJ, SSZY  from icdc_gx.V_BJXX_BKS"
        ret_list = []
        data_list = self.db.get_raw_data_by_statement(statement=statement, var_tuple=None)
        for data in data_list:
            keys_list = ["department_code", "classroom_code", "classroom_name", 'term', 'major_code']
            ret_list.append(self.query_data_to_dict(data, keys=keys_list))
        return ret_list

    # -----------------------  选课 数据 -----------------------
    def get_bks_choose_classroom_data(self, *args, **kwargs):
        statement = "select  XH,   XKKH,  KCB from icdc_gx.V_PKXX_BKS"
        ret_list = []
        data_list = self.db.get_raw_data_by_statement(statement=statement, var_tuple=None)
        for data in data_list:
            keys_list = ["student_number", "classroom_code", 'classroom_table']
            ret_list.append(self.query_data_to_dict(data, keys=keys_list))
        return ret_list

    def get_teacher_choose_classroom_data(self, *args, **kwargs):
        statement = "select  XKKCH,   KCH,  SJKCMC,  XKKH, XKXQ, KKYX, JSGH, JSXM from icdc_gx.V_PKXX_JZ"
        ret_list = []
        data_list = self.db.get_raw_data_by_statement(statement=statement, var_tuple=None)
        for data in data_list:
            keys_list = ["course_code", "classroom_code", 'course_name', 'xueke_kehao', 'xueke_term',
                         'department_code', 'teacher_number', 'teacher_name']
            ret_list.append(self.query_data_to_dict(data, keys=keys_list))
        return ret_list

    def get_yjs_choose_classroom_data(self, *args, **kwargs):
        statement = "select  XH,   XN,  XQ,  RKJSGH, KCDM, KCMC,SKBJ, XKH from icdc_gx.V_PKXX_YJS"
        ret_list = []
        data_list = self.db.get_raw_data_by_statement(statement=statement, var_tuple=None)
        for data in data_list:
            keys_list = ["student_number", "year", 'term',
                         'teacher_number', 'course_code', 'course_name', 'tra_classroom', 'classroom_code']
            ret_list.append(self.query_data_to_dict(data, keys=keys_list))
        return ret_list


kmust_proxy = ZufeDataProxy()
