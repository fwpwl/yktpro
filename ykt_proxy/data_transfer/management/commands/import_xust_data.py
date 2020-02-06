# -*- encoding:utf-8 -*-
"""
西安科技大学 导入数据
"""
import os
import sys
import datetime
import itertools
import requests
from django.core.management import BaseCommand
from django.utils.crypto import get_random_string
from django.utils.encoding import force_text

from data_transfer.utils.safe import make_signature

reload(sys)
sys.setdefaultencoding('utf8')


# 学校的学期及对应开放时间
SCHOOL_TERM_MAP = {
    3: ("0801", "0131"),  # 第1学期
    12: ("0201", "0731")   # 第2学期
}


XUST_SERVER = "http://127.0.0.1:8080/data/xust"
XUST_UNI_INFO_DICT = {
    "university_name": "西安科技大学",
    "university_province": "陕西省",
    "university_city": "西安市",
    "university_address": "西安市雁塔路58号",
    "university_url": "https://xust.yuketang.cn/",
    "current_term": "201901",
    "university_prefix": "xust"
}


def ensure_dir_exist_and_clean(dir_path):
    """

    """
    if os.path.exists(dir_path):
        os.system('rm -rf {}'.format(dir_path))
    os.system('mkdir -p {}'.format(dir_path))


def remove_list_repeat(some_list):
    """
    最高效率的去重函数
    PARA:
    some_list: 比如:
    [[1, 2], [2, 3], [1, 2]]   ------> [[2, 3], [1, 2]]

    """
    some_list.sort()
    some_list = list(k for k, _ in itertools.groupby(some_list))
    return some_list


def ensure_unicode(str1):
    if str1 is None:
        return u''
    if isinstance(str1, unicode):
        return str1
    elif isinstance(str1, (int, float)):
        return str1
    elif isinstance(str1, datetime.datetime):
        return str1.strftime("%Y")
    else:
        return str1.decode('utf-8')


def delete_special_char_from_excel_str(some_str, replace_dot=True):
    """

    """
    some_str = force_text(some_str).encode("utf8")
    if replace_dot:
        special_char_list = [' ', '\n', '\x0b', ' ', '.0', '.00', "   ", "  ", " ", '\n', '\r']
    else:
        special_char_list = [' ', '\n', '\x0b', ' ', "   ", "  ", " ", '\n', '\r']
    for special_char in special_char_list:
        some_str = some_str.replace(special_char, '')

    # 有些课程里面的老师这一列会有中文逗号,所以替换
    some_str = some_str.replace('，', ',')
    return some_str


def excel_data_cleaner(data_list_of_list, ignore_index=[], replace_dot=True):
    """
    去掉每个字段中的特殊字符, 并且替换字符串型数字中的0/00等格式
    """
    new_info_list_of_list = []
    for info_list in data_list_of_list:
        tmp_list = []
        for index, value in enumerate(info_list):
            if value is None or value == 'None':
                value = ''
            if index in ignore_index:
                value = value.strip()
                tmp_list.append(value)
            else:
                value = ensure_unicode(delete_special_char_from_excel_str(force_text(value).encode("utf8"), replace_dot=replace_dot))
                tmp_list.append(value)
        new_info_list_of_list.append(tmp_list)
    return new_info_list_of_list


def write_file_as_csv(file_name, list_of_list):
    """

    """
    import csv

    with open(file_name, mode='wb') as employee_file:
        employee_writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        for some_list in list_of_list:
            employee_writer.writerow(some_list)


def write_result_info_dict_into_tmp_csv(tmp_csv_file_path, result_info_dict, replace_dot=True):
    """

    """
    ensure_dir_exist_and_clean(tmp_csv_file_path)

    department_info_list_of_list = remove_list_repeat(excel_data_cleaner(result_info_dict.get("department"),
                                                                         replace_dot=replace_dot))
    tradition_class_info_list_of_list = remove_list_repeat(excel_data_cleaner(result_info_dict.get("tra_classroom"),
                                                                              replace_dot=replace_dot))
    user_info_list_of_list = remove_list_repeat(excel_data_cleaner(result_info_dict.get("user_info"),
                                                                   replace_dot=replace_dot))
    course_info_list_of_list = remove_list_repeat(excel_data_cleaner(result_info_dict.get("course"),
                                                                     replace_dot=replace_dot))
    choose_info_list_of_list = remove_list_repeat(excel_data_cleaner(result_info_dict.get("choose"),
                                                                     replace_dot=replace_dot))

    write_file_as_csv('{}/department.csv'.format(tmp_csv_file_path), department_info_list_of_list)
    write_file_as_csv('{}/tradition_class.csv'.format(tmp_csv_file_path), tradition_class_info_list_of_list)
    write_file_as_csv('{}/user.csv'.format(tmp_csv_file_path), user_info_list_of_list)
    write_file_as_csv('{}/course.csv'.format(tmp_csv_file_path), course_info_list_of_list)
    write_file_as_csv('{}/choose.csv'.format(tmp_csv_file_path), choose_info_list_of_list)


def send_request(url, method="get", **kwargs):
    if "timeout" not in kwargs:
        kwargs["timeout"] = 800

    r = requests.request(
        method=method,
        url=url,
        **kwargs
    )
    if r.status_code != 200:
        return []

    response = r.json()
    return response.get("data", [])


class Command(BaseCommand):
    def __init__(self):
        super(Command, self).__init__()

    def add_arguments(self, parser):
        parser.add_argument("-t", "--type", nargs='*',
                            help="其他参数列表")

    # @script_standard_output
    def handle(self, *args, **optionds):
        """
        python manage.py exec import_ynufe_data -t generate/import
        """
        # ---------------------------------------------------------------------------------
        # 以下这段每个脚本都一样,直接copy即可
        # ---------------------------------------------------------------------------------
        generate_data()


def send_page_request(url, method="get", page=0, page_size=2000, params=None):
    """
    分页拉取所有数据
    """
    if params is None:
        params = {}

    params["page"] = page
    params["page_size"] = page_size
    new_params = {k: v for k, v in params.items() if k != "signature"}
    signature = make_signature(**new_params)
    new_params["signature"] = signature

    response = send_request(url, method=method, params=new_params)
    if not response:
        return response

    page_num = response.get("page_num", 1)
    if page_num <= 1:
        return response.get("data", [])

    data_list = []
    data_list.extend(response.get("data", []))
    for page in range(1, page_num):
        new_params = {k: v for k, v in params.items() if k != "signature"}
        new_params["page"] = page
        signature = make_signature(**new_params)
        new_params["signature"] = signature
        response = send_request(url, method=method, params=new_params)
        if not response:
            break
        data_list.extend(response.get("data", []))

    return data_list


def gen_term_info():
    today = datetime.datetime.today()
    today -= datetime.timedelta(days=30)
    current_year = str(today.year)
    today_str = today.strftime("%Y%m%d")
    last_year = today.year - 1
    current_school_term = 3
    current_term = "%s01" % last_year

    for term, term_times in SCHOOL_TERM_MAP.iteritems():
        if term == 3:
            term_start = "%s%s" % (last_year, term_times[0])
            term_end = "%s%s" % (current_year, term_times[1])
        else:
            term_start = "%s%s" % (current_year, term_times[0])
            term_end = "%s%s" % (current_year, term_times[1])
        if term_start <= today_str <= term_end:
            current_school_term = term
            break
    current_year = str(last_year)
    if current_school_term == 12:
        current_term = "%s02" % last_year
        current_year = str(last_year)

    return dict(
        current_term=current_term,
        current_year=current_year,
        current_school_term=current_school_term
    )


def generate_data():
    term_info = gen_term_info()
    current_term = term_info["current_term"]
    current_year = term_info["current_year"]
    current_school_term = term_info["current_school_term"]
    params = {"year": current_year, "term": current_school_term, "salt": get_random_string(10)}
    signature = make_signature(**params)
    params["signature"] = signature
    print '获取{}学期数据中......'.format(current_term)

    # 产生对照关系表
    print 'department_data......'
    department_data = send_request(
        url='{}/get_department_data'.format(XUST_SERVER), params=params
    )

    print 'tra_classroom_data......'
    tra_classroom_data = send_page_request(
        url='{}/get_tra_classroom_data'.format(XUST_SERVER),
        page_size=5000, params=params
    )

    print 'user_data......'
    user_data = send_page_request(
        url='{}/get_user_data'.format(XUST_SERVER),
        page_size=5000, params=params
    )

    print 'course_data......'
    course_data = send_page_request(
        url='{}/get_course_data'.format(XUST_SERVER),
        page_size=5000, params=params
    )

    print 'choose_data......'
    choose_data = send_page_request(
        url='{}/get_choose_data'.format(XUST_SERVER),
        page_size=5000, params=params
    )

    department_name_list = [[d["department_name"]] for d in department_data]
    tradition_class_info_list = []
    user_info_list = []
    course_info_list = []
    choose_info_list = []

    for info_dict in tra_classroom_data:
        tra_classroom_name = info_dict.get('tra_classroom_name')
        department_name = info_dict.get('department_name')
        major = info_dict.get('major')
        year = info_dict.get('year')

        tradition_class_info_list.append([
            department_name,
            major,
            tra_classroom_name,
            year
        ])

    for info_dict in user_data:
        number = info_dict.get('number')
        department_name = info_dict.get('department_name')
        tra_classroom_name = info_dict.get('tra_classroom_name')
        user_type = info_dict.get('user_type')
        name = info_dict.get('name')
        year = info_dict.get('year')

        user_info_list.append([
            department_name,
            tra_classroom_name,
            name,
            number,
            user_type,
            year if year else 0
        ])

    for info_dict in course_data:
        department_name = info_dict.get('department_name')
        course_code = info_dict.get('course_code')
        course_name = info_dict.get('course_name')
        classroom_code = info_dict.get('classroom_code')
        classroom_name = info_dict.get('classroom_name')
        teacher_number = info_dict.get('teacher_number')
        teacher_name = info_dict.get('teacher_name')
        final_classroom_code = '{}-{}'.format(current_term, classroom_code)

        course_info_list.append([
            department_name,
            course_code,
            course_name,
            teacher_number,
            teacher_name,
            final_classroom_code,
            classroom_name,
        ])

    for info_dict in choose_data:
        student_number = info_dict.get("teacher_number")
        classroom_code = info_dict.get("classroom_code")

        final_classroom_code = '{}-{}'.format(current_term, classroom_code)
        if not (student_number and classroom_code):
            continue

        choose_info_list.append([
            student_number,
            final_classroom_code
        ])

    # ---------------------------------------------------------------------------------
    # 每个学校,以下代码都一致(根据个人需求改变tmp路径即可)
    # ---------------------------------------------------------------------------------
    tmp_csv_file_path = '/opt/ykt/university_data/{}'.format(
        XUST_UNI_INFO_DICT.get('university_name')
    )
    result_info_dict = {
        "department": department_name_list,
        "tra_classroom": tradition_class_info_list,
        "user_info": user_info_list,
        "course": course_info_list,
        "choose": choose_info_list,

    }
    write_result_info_dict_into_tmp_csv(tmp_csv_file_path, result_info_dict=result_info_dict)
    return result_info_dict
