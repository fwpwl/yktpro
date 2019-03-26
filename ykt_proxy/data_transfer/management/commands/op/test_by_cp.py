# -*- encoding:utf-8 -*-
"""
导入省份城市信息, 最开始建库的时候用,后期不再用
"""

from django.core.management import BaseCommand

from data_transfer.data_proxy_utils import OracleTransferHandler


class Command(BaseCommand):
    def __init__(self):
        super(Command, self).__init__()

    def handle(self, *args, **optionds):
        """
        python manage.py exec test_by_cp
        """
        # conn = psycopg2.connect(database="testdb", user="postgres", password="pass123", host="127.0.0.1", port="5432")
        db = OracleTransferHandler(connect_str="user_yuketang/user_yuketang@172.16.8.70:1521/icdc")

        db = OracleTransferHandler(connect_str="usr_yuketang/Cidp#2019@10.159.241.3:1521/KFPTDB")


        statement = "select XH,  XM,  YXSH,  ZYM,  SZBH,  SZNJ,  RXNY,  XZ,  XSDQZTM from icdc_gx.V_XSJBXX_BKS"
        ret_list = []
        data_list = db.get_raw_data_by_statement(statement=statement, var_tuple=None)
        for data in data_list:
            keys_list = ["number", "name", 'department_code', 'major_code', 'tra_class_code', 'term',
                         'come_in_year', 'xuezhi', 'current_status_code']
            ret_list.append(query_data_to_dict(data, keys=keys_list))

        print ret_list


def query_data_to_dict(query_data, keys):
    result_dict = {}
    for i, item in enumerate(query_data):
        item = "" if not item else item
        result_dict.update({keys[i]: item})
    return result_dict
