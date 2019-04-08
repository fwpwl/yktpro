# -*- encoding:utf-8 -*-
"""
导入省份城市信息, 最开始建库的时候用,后期不再用
"""
import psycopg2
from django.core.management import BaseCommand

from data_transfer.data_proxy_utils import OracleTransferHandler


class Command(BaseCommand):
    def __init__(self):
        super(Command, self).__init__()

    def handle(self, *args, **optionds):
        """
        python manage.py exec test_by_cp
        """
        a = [1, 2, 3]
        b = [11, 22, 33]
        c = dict(zip(a, b))


        conn = psycopg2.connect(database="datacenter", user="readonly", password="readonly", host="10.155.10.180", port="5432")
        cursor = conn.cursor()
        cursor.execute("select xymc from data_jw.jx_xy")

        cursor.execute("select * from data_out.v_ids")

        rows = cursor.fetchall()
        print rows



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
