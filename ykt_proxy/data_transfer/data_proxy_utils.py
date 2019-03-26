# coding:utf-8

import cx_Oracle
import os

os.environ['NLS_LANG'] = 'AMERICAN_AMERICA.AL32UTF8'


class DataProxyBase(object):
    def get_all_data(self, *args, **kwargs):
        return {
            "university": self.get_university_data(*args, **kwargs),
            "department": self.get_department_data(*args, **kwargs),
            "tradition_class": self.get_tradition_class_data(*args, **kwargs),
            "user_map": self.get_user_map_data(*args, **kwargs),
            "course_class": self.get_course_class_data(*args, **kwargs),
            "choose_course": self.get_choose_course_data(*args, **kwargs),
        }

    def get_university_data(self, *args, **kwargs):
        raise NotImplementedError

    def get_department_data(self, *args, **kwargs):
        raise NotImplementedError

    def get_tradition_class_data(self, *args, **kwargs):
        raise NotImplementedError

    def get_user_map_data(self, *args, **kwargs):
        raise NotImplementedError

    def get_course_class_data(self, *args, **kwargs):
        raise NotImplementedError

    def get_choose_course_data(self, *args, **kwargs):
        raise NotImplementedError


class OracleTransferHandler(object):
    def __init__(self, connect_str):
        self.connect_str = connect_str
        print "connecting to oracle server [{}]".format(self.connect_str)
        self.db = cx_Oracle.connect(self.connect_str)
        print "connect success! now get cursor"
        self.cursor = self.db.cursor()
        print "generate DataTransfer Object success!"

    def get_raw_data_by_statement(self, statement, var_tuple):
        if var_tuple:
            self.cursor.execute(statement, var_tuple)
        else:
            self.cursor.execute(statement)
        data_list = self.cursor.fetchall()
        return data_list

    def write_data_to_database(self, statement, var_tuple):
        try:
            self.cursor.prepare(statement)
            self.cursor.execute(None, var_tuple)
            self.db.commit()
            return True, ""
        except Exception as ex:
            return False, ex.message
