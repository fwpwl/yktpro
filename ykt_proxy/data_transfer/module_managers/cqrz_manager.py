# coding: utf-8
import psycopg2


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
        conn = psycopg2.connect(database="datacenter",
                                user="readonly",
                                password="readonly",
                                host="10.155.10.180",
                                port="5432")
        cursor = conn.cursor()
        func(cursor)
        conn.close()

    return wrapper



@get_client
def cqrz_get_user_info_data(cursor):
    cursor.execute("select dwmc, bjmc, xgh, xm, nj, lx1  from data_out.v_ids")
    rows = cursor.fetchall()
    user_info_data = query_data_to_dict_list(rows, ["department_name", "tradition_classroom_name", "number",
                                                    "name", "year", "user_type"])
    return user_info_data


@get_client
def cqrz_get_course_data(cursor):
    sql = "select xnxq, gh, kcmc, kcdm, xkkh from data_jw.jx_js_kcb"
    cursor.execute(sql)
    rows = cursor.fetchall()
    course_data = query_data_to_dict_list(rows,["year_term", "teacher_number", "course_name", "course_code", "classroom_code"])
    print course_data
    return course_data



@get_client
def cqrz_get_choose_course_data(cursor):

    pass
