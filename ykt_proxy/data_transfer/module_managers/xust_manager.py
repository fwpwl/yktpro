# -*- coding:utf-8 -*-
""""
西安科技大学
"""
from data_transfer.data_proxy_utils import MySQLTransferHandler


def query_data_to_dict_list(query_data_list_of_tuple, keys_list):
    final_list = []
    for tuple_item in query_data_list_of_tuple:
        tmp_dict = dict(zip(keys_list, tuple_item))
        final_list.append(tmp_dict)
    return final_list


def gen_total_pages(count, page_size=500):
    num_pages = count // page_size
    if count % page_size != 0:
        num_pages += 1

    return num_pages


def get_client(func):
    def wrapper(*args, **kwargs):
        conn = MySQLTransferHandler(
            host="59.74.174.158",
            port=3306,
            user="root",
            password="o5gwc8Dj?yel",
            database="ykt"
        )
        return func(conn, *args, **kwargs)

    return wrapper


# ---------------------------------------------------------------------------------
# 本科生基本数据
# ---------------------------------------------------------------------------------

@get_client
def get_department_data(db, *args, **kwargs):
    """
    学院列表
    """
    statement = "select `Id`, `xymc`  from xyxxb"
    data_list = db.get_raw_data_by_statement(statement=statement, var_tuple=None)
    keys_list = ["department_id", "department_name"]
    department_data = query_data_to_dict_list(data_list, keys_list)

    return department_data


@get_client
def get_tra_classroom_data(db, page=0, page_size=2000, *args, **kwargs):
    """
    行政班级数据
    """
    count_sql = "select count(rxxn) from xzbjb"
    count_data = db.get_row_count_by_statement(count_sql, var_tuple=None)
    count = int(count_data[0])
    if count == 0:
        return dict(page_num=1, data=[])
    page_num = gen_total_pages(count, page_size)
    offset = page * page_size
    statement = "select ssxy, zy, bjmc, rxxn from xzbjb limit %s  offset %s"
    data_list = db.get_raw_data_by_statement(statement=statement, var_tuple=(page_size, offset))
    keys_list = ["department_name", "major", 'tra_classroom_name', "year"]

    info_list = query_data_to_dict_list(data_list, keys_list)

    return dict(page_num=page_num, data=info_list)


@get_client
def get_user_data(db, page=0, page_size=2000, *args, **kwargs):
    """
    全体成员数据，即用户信息
    """
    count_sql = "select count(xh) from qtcyb"
    count_data = db.get_row_count_by_statement(count_sql, var_tuple=None)
    count = int(count_data[0])
    if count == 0:
        return dict(page_num=1, data=[])
    page_num = gen_total_pages(count, page_size)
    offset = page * page_size
    statement = "select ssxy, xzbjmc, xm, xh, sf, rxxn from qtcyb limit %s  offset %s"
    data_list = db.get_raw_data_by_statement(statement=statement, var_tuple=(page_size, offset))
    keys_list = ["department_name", "tra_classroom_name", 'name', 'number', 'user_type', 'year']

    info_list = query_data_to_dict_list(data_list, keys_list)

    return dict(page_num=page_num, data=info_list)


@get_client
def get_course_data(db, year="2019", term=3, page=0, page_size=2000, *args, **kwargs):
    """
    课程数据
    """
    count_sql = "select count(kkxn) from bxqkkxb where kkxn=%s and kkxq=%s"
    count_data = db.get_row_count_by_statement(count_sql, var_tuple=(year, term))
    count = int(count_data[0])
    if count == 0:
        return dict(page_num=1, data=[])
    page_num = gen_total_pages(count, page_size)
    offset = page * page_size
    statement = """
          select ssxy, kcmc, kch, kcbjmc, xkh, jsgh, jsxm, kkxn, kkxq 
          from bxqkkxb where kkxn=%s and kkxq=%s limit %s offset %s
    """
    data_list = db.get_raw_data_by_statement(statement=statement, var_tuple=(year, term, page_size, offset))
    keys_list = (
        "department_name",
        'course_name',
        "course_code",
        'classroom_name',
        "classroom_code",
        'teacher_number',
        'teacher_name',
        "year", 'term'
    )

    info_list = query_data_to_dict_list(data_list, keys_list)

    return dict(page_num=page_num, data=info_list)


@get_client
def get_choose_data(db, year="2019", term=3, page=0, page_size=2000, *args, **kwargs):
    """
    选课数据
    """
    count_sql = "select count(kkxn) from bxqxkxxb where kkxn=%s and kkxq=%s"
    count_data = db.get_row_count_by_statement(count_sql, var_tuple=(year, term))
    count = int(count_data[0])
    if count == 0:
        return dict(page_num=1, data=[])
    page_num = gen_total_pages(count, page_size)
    offset = page * page_size
    statement = "select xkh, xh, kkxn, kkxq from bxqxkxxb where kkxn=%s and kkxq=%s limit %s  offset %s"
    data_list = db.get_raw_data_by_statement(statement=statement, var_tuple=(year, term, page_size, offset))

    keys_list = ['classroom_code', 'teacher_number', "year", 'term']
    info_list = query_data_to_dict_list(data_list, keys_list)

    return dict(page_num=page_num, data=info_list)
