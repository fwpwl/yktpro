# coding: utf-8
from data_transfer.data_proxy_utils import DataProxyBase, OracleTransferHandler


class FzxyDataProxy(DataProxyBase):
    """

    """

    def __init__(self):
        self.db = OracleTransferHandler(connect_str="kgykt/Kg_ykt2018@222.197.198.189:1521/orcl")

    def query_data_to_dict(self, query_data, keys):
        result_dict = {}
        for i, item in enumerate(query_data):
            item = "" if not item else item
            result_dict.update({keys[i]: item})
        return result_dict

    def get_department_data(self, *args, **kwargs):
        statement = "select XXMC, XYMC from KG_VIEW_OUT_YKT_DWXX"
        ret_list = []
        data_list = self.db.get_raw_data_by_statement(statement=statement, var_tuple=None)
        for data in data_list:
            ret_list.append(self.query_data_to_dict(data, keys=["university_name", "department_name"]))
        return ret_list

    def get_tradition_class_data(self, *args, **kwargs):
        statement = "select XXMC, YXMC, ZYMC, BJMC, BZRGH, JS, XW, RXNF from KG_VIEW_OUT_YKT_BJXX"
        ret_list = []
        data_list = self.db.get_raw_data_by_statement(statement=statement, var_tuple=None)
        for data in data_list:
            ret_list.append(self.query_data_to_dict(data, keys=["university_name", "department_name", "major",
                                                                "tradition_classroom_name", "teacher_number", "role",
                                                                "grade", "join_year"]))
        return ret_list

    def get_user_map_data(self, *args, **kwargs):
        statement = "select XXMC, YXMC, BJMC, XM, XGH, RXXN, RXXQ, JS from KG_VIEW_OUT_YKT_XSJSXX"
        ret_list = []
        data_list = self.db.get_raw_data_by_statement(statement=statement, var_tuple=None)
        for data in data_list:
            ret_list.append(self.query_data_to_dict(data, keys=["university_name", "department_name",
                                                                "tradition_classroom_name", "name", "number",
                                                                "join_year", "join_term", "user_type"]))
        return ret_list

    def get_course_class_data(self, *args, **kwargs):
        year = kwargs.get("year", "2018-2019")
        term = kwargs.get("term", 1)
        statement = "select XXMC,YXMC, KCH, KMC, KXH, KKLSGH, KKXN, KKXQ from KG_VIEW_OUT_YKT_KKXXB where KKXN=\'{}\' and KKXQ={}".format(
            year, term)
        ret_list = []
        data_list = self.db.get_raw_data_by_statement(statement=statement, var_tuple=None)
        for data in data_list:
            ret_list.append(self.query_data_to_dict(data, keys=["university_name", "department_name", "course_code",
                                                                "course_name", "classroom_code", "teacher_number",
                                                                "year", "term"]))

        return ret_list

    def get_choose_course_data(self, *args, **kwargs):
        year = kwargs.get("year", "2018-2019")
        term = kwargs.get("term", 1)
        statement = "select KXH, XH, JS from KG_VIEW_OUT_YKT_XKXXB where SKXN=\'{}\' and SKXQ={}".format(
            year, term)
        data_list = self.db.get_raw_data_by_statement(statement=statement, var_tuple=None)
        ret_list = []
        for data in data_list:
            ret_list.append(self.query_data_to_dict(data,
                                                    keys=["classroom_code", "number", "role"]))
        return ret_list

fzxy_proxy = FzxyDataProxy()
