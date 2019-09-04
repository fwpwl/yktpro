# -*- coding:utf-8 -*-
import hashlib
import math
import os
import random
import re
import string
import time

from django.conf import settings

ALPHABET = '23456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnpqrstuvwxyz'


def time_since(millisecond=True):
    """millisecond since xxx
    import time; time.mktime(datetime.datetime.strptime('2013-10-01',
        '%Y-%m-%d').timetuple())
    """
    if millisecond:
        return int(time.time() * 1000) - 1380556800000
    else:
        return int(time.time()) - 1380556800


def basex_encode(num, alphabet=ALPHABET):
    """Encode a number in Base X

    `num`: The number to encode
    `alphabet`: The alphabet to use for encoding
    """
    assert (num >= 0)
    if num == 0:
        return alphabet[0]
    arr = []
    base = len(alphabet)
    while num:
        rem = num % base
        num = num // base
        arr.append(alphabet[rem])
    arr.reverse()
    return ''.join(arr)


def id64():
    return basex_encode(
        (time_since() << 23) + random.SystemRandom().getrandbits(23))


def generate_random_fake_number(random_lenth=10, alphabet=ALPHABET):
    assert (random_lenth > 0)
    if random_lenth == 0:
        return ""
    else:
        base = len(alphabet)
        arr = []
        rand = random.Random()
        for i in range(0, random_lenth):
            rem = rand.randint(0, base - 1)
            arr.append(alphabet[rem])
        return ''.join(arr)


def get_start_end_num_by_page(page=1, per_page_num=20):
    """
    根据page数量返回开始和结束 页码
    """
    page = int(page)
    per_page_num = int(per_page_num)

    if page < 0:
        return 0, 0

    if page == 0:
        page = 1

    start_num = (page - 1) * per_page_num
    end_num = start_num + per_page_num
    return start_num, end_num


def is_for_testcase():
    """
    判断是否是在跑testcase
    """
    try:
        return settings.IS_FOR_TESTCASE
    except:
        return False


def division_ceil(divisor, dividend):
    """
    除法向上取整
    PARA: divisor: 除数
          dividend: 被除数
    RET: int
    eg: division_ceil(20, 130) = 7
    """
    return int(math.ceil(dividend / float(divisor)))


def cal_md5(value, num=None):
    """
    计算MD5
    """
    try:
        value = str(value)
        sha1 = hashlib.md5()
        sha1.update(value.encode("utf8"))
        result = sha1.hexdigest()
        if num:
            num = int(num)
            return result[0:num]
        return result
    except Exception as e:
        print(str(e))
        return ''


def get_file_md5(file_path):
    """

    """
    if not os.path.exists(file_path):
        return ''
    with open(file_path, 'rb') as file:
        md5 = hashlib.md5()
        while True:
            str_read = file.read(8096)
            if not str_read:
                break
            md5.update(str_read)
        str_md5 = md5.hexdigest()
    return str_md5


def is_cellphone_num(cellphone_num):
    """
    判断是否手机号码
    """
    if not isinstance(cellphone_num, str):
        cellphone_num = str(cellphone_num)

    if not cellphone_num:
        return False
    return bool(re.compile('^1\d{10}$').match(cellphone_num))


def cal_percent_tool(some_status_num, all_num):
    """
    计算百分率
    RET: 20.3%
    """
    try:
        temp_num_str = '%.2f' % (float(some_status_num) / float(all_num) * 100)
        return temp_num_str + "%"
    except:
        return ''


def cal_percent_normal(some_status_num, all_num):
    """
    计算百分率
    RET: 0.22 float
    """
    try:
        temp_num_str = '%.3f' % (float(some_status_num) / float(all_num))
        return float(temp_num_str)
    except:
        return 0


def create_models_for_testcase(model_root_path):
    """

    """
    new_file_str = ''
    models_path = model_root_path + 'models.py'
    with open(models_path, 'r') as f:
        for line in f:
            if _should_this_line_added(line):
                new_file_str += line

    models_for_testcase_path = model_root_path + 'models_for_testcase.py'
    with open(models_for_testcase_path, 'w') as f:
        f.write(new_file_str)
    return models_for_testcase_path


def _should_this_line_added(line):
    """

    """
    forbid_keyword_list = ['managed = False',
                           'app_label',
                           'db_table',
                           'class Meta:']
    should_add = True
    for forbid_keyword in forbid_keyword_list:
        if forbid_keyword in line:
            should_add = False
    return should_add


def convert_value_list_str_to_list(value_list_str, split_char='-'):
    """
    convert '12-13-35' to [12, 13, 35]
    """
    try:
        value_list = value_list_str.split(split_char)
        value_list = [value for value in value_list if value]
        return value_list
    except:
        return []


class Switch(object):
    """
    @brief: A Simple Imitation of Switch-Case Structure to Avoid Complex Nestification of 'if-else'
    """

    def __init__(self, value):
        self.value = value

    def match(self, *args):
        for i in range(len(self.value)):
            if self.value[i] != args[i]:
                return False
        return True


def get_page_from_request(request):
    """

    """
    try:
        page = request.REQUEST.get("page")
        if not page:
            page = '1'
        return int(page)
    except:
        return 1


def convert_str_to_int(str_):
    try:
        return int(str_)
    except:
        return None


def get_file_absolute_path_by_relative_path(relative_path):
    """

    """
    project_directory = os.path.dirname(os.path.dirname(__file__))
    return os.path.join(project_directory, relative_path)


def is_str_all_num(some_str):
    """

    """
    try:
        int(some_str)
        return True
    except:
        return False


def convert_large_list_to_list_of_list(large_list, gap_num=50000):
    """

    """
    result_list_of_list = []
    start_num = 0
    all_num = len(large_list)
    while start_num < all_num:
        result_list_of_list.append(large_list[start_num: start_num + gap_num])
        start_num += gap_num
    return result_list_of_list


def get_list_of_list_all_num(list_of_list):
    """

    """
    num_list = [len(single_list) for single_list in list_of_list]
    all_num = 0
    for num in num_list:
        all_num += num
    return all_num


def convert_num_str_to_num(num_str):
    """

    """
    if not num_str:
        return 0
    if '.' in num_str:
        return float(num_str)
    else:
        return int(num_str)


def custom_join_path_by_path_list(path_list, path_split_char='/'):
    """

    """
    # path_list 长度必须>=1, 并且不能有空的item
    if len(path_list) < 1:
        return ''
    for item in path_list:
        if not item:
            return ''

    whole_path = path_list[0]
    for index, path in enumerate(path_list[1:]):

        if whole_path[-1] == path_split_char and path[0] == path_split_char:
            whole_path += path[1:]
        elif (whole_path[-1] == path_split_char and path[0] != path_split_char) or (
                        whole_path[-1] != path_split_char and path[0] == path_split_char):
            whole_path += path
        elif whole_path[-1] != path_split_char and path[0] != path_split_char:
            whole_path += (path_split_char + path)
    return whole_path


def ensure_millisecond(some_timestamp):
    """
    确保是毫秒级别的
    """
    some_timestamp = int(some_timestamp)
    if len(str(some_timestamp)) > 11:
        return some_timestamp
    else:
        return some_timestamp * 1000


def change_file_name_to_random(file_name):
    """

    """
    file_name_list = file_name.split('.')
    return id64() + '.' + file_name_list[-1]


def add_some_suffix_to_file_name(file_name, some_suffix=''):
    """

    """
    file_name_list = file_name.split('.')
    return file_name_list[0] + some_suffix + '.' + file_name_list[-1]


def convert_byte_to_mb(file_size):
    """
    RET: float
    """
    return float('%.2f' % (file_size / 1024.0 / 1024.0))


def get_key_by_value_in_dict(dict, search_value):
    """

    """
    for key, value in dict.items():
        if value == search_value:
            return key
    return ''


def get_price(price):
    """
    将价格的分转化为元
    """
    if price % 100 == 0:
        price = str(price // 100)
    elif price % 10 == 0:
        price = '{0[0]}.{0[1]:0>1}'.format(divmod(price // 10, 10))
    else:
        price = '{0[0]}.{0[1]:0>2}'.format(divmod(price, 100))
    return '{0}'.format(price)


def get_right_resource_url(some_url, is_https=True):
    """
    http和https转换
    """
    import re
    if not is_https and 'https:' in some_url:
        some_url = re.sub(r"\bhttps\b", 'http', some_url)
    if is_https and 'http:' in some_url:
        some_url = re.sub(r"\bhttp\b", 'https', some_url)
    return some_url


def convert_second_to_format_time(seconds):
    """

    """
    import time
    now_time_stamp = int(time.time())
    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(float(now_time_stamp + seconds)))


def random_str(randomlength=6):
    a = list(string.ascii_letters)
    random.shuffle(a)
    some = ''.join(a[:randomlength])
    return some.upper()


def get_random_num_list(count, limit_max_count):
    if count >= limit_max_count:
        return [i for i in range(0, limit_max_count)]
    else:
        final = []
        while (len(final) < count):
            i = random.randint(0, limit_max_count - 1)
            if i not in final:
                final.append(i)

        return final


def convert_to_bool(s, default=False):
    if not s:
        return False
    if s in ('', u''):
        return False
    s = s.lower()
    if s in (u'on', u'true', u'1', 'on', 'true', '1'):
        return True
    if s in (u'off', u'false', u'0', 'off', 'false', '0'):
        return False
    return default


def get_year_month_range_by_term(year_term):
    """
    解析学期字段的学期覆盖
    :param year_term:
    :return:
    """
    year = year_term[0:4]
    int_year = int(year)
    term = year_term[4:]
    if term == "01":
        return {
            str(int_year): [str(item) for item in range(8, 13)],
            str(int_year + 1): ["1"]
        }
    else:
        return {
            str(int_year + 1): [str(item) for item in range(2, 8)]
        }


def convert_number_to_percent_str(number):
    """

    """
    return "{0:.0%}".format(number)


def delete_special_char_from_str(some_str):
    """
    存储路径中去掉特殊字符,如空格,换行,其他字符等等
    """
    special_char_list = [' ', '-', '\n', '\x0b', ' ']
    for special_char in special_char_list:
        some_str = some_str.replace(special_char, '')
    return some_str


def url_join(*args):
    """
    URL 或者 路径 组装
    PARA: 'www.baidu.com', 'hello', 'good', ...
    """
    return "/".join(map(lambda x: str(x).rstrip('/'), args))


def check_contain_chinese(check_str):
    """
    判断字符串中是否包含中文
    """
    chinese_mark_list = ['。', '？', '！', '，', '、', '；', '：', '「', '」', '『', '』',
                         '‘', '’', '“', '”', '（', '）', '〔', '〕', '【', '】',
                         '—', '…', '–', '．', '《', '》', '〈', '〉']
    for char in chinese_mark_list:
        if char in check_str:
            return True

    for char in check_str.decode('utf-8'):
        if u'\u4e00' <= char <= u'\u9fff':
            return True

    return False
