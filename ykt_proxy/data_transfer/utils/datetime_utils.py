# -*- coding:utf-8 -*-
"""
时间处理工具
"""
import calendar
import datetime
import time

FORMAT_DATE_WITHOUT_SEPARATOR = '%Y%m%d'
FORMAT_DATETIME_WITHOUT_SEPARATOR = '%Y%m%d%H%M%S'
FORMAT_DATE = '%Y-%m-%d'
SLASH_FORMAT_DATE = '%m/%d/%Y'
FORMAT_MONTH = '%Y-%m'
FORMAT_YEAR = '%Y'

FORMAT_DATETIME = '%Y-%m-%d %H:%M:%S'
NO_SECOND_FORMAT_DATETIME = '%Y-%m-%d %H:%M'
FORMAT_DATETIME_MSEC = '%Y-%m-%d %H:%M:%S.%f'
FORMAT_HOUR_MIN = '%H:%M'

CHINA_FORMAT_DATE = u'%Y年%m月%d日'

CURRENT_TIME_INFO = u'%s %s'
WEEK_LIST = [u'星期一', u'星期二', u'星期三', u'星期四', u'星期五', u'星期六', u'星期日']


def datetime_to_str(date, date_format=FORMAT_DATE):
    """
    convert datetime type into date string ('2011-01-12')
    """
    return date.strftime(date_format)


def timestamp_to_datetime(seconds):
    """
    将POSIX time (Unix timestamp)转换为datetime
    """
    return datetime.datetime.fromtimestamp(seconds)


def datetime_to_timestamp_msec(time_):
    """
    datetime类型转换为unix时间戳
    RET: 毫秒级
    """
    if time_:
        timestamp = time.mktime(time_.timetuple())
        return int(timestamp) * 1000
    else:
        return ""


def datetime_to_timestamp_second(time_):
    """
    datetime类型转换为unix时间戳
    RET: 毫秒级
    """
    if time_:
        timestamp = time.mktime(time_.timetuple())
        return int(timestamp)
    else:
        return ""


def timestamp_to_datetime_str(seconds, date_format=FORMAT_DATETIME):
    """
    时间戳直接转成日期格式('2011-01-12')
    """
    try:
        datetime_format = datetime.datetime.fromtimestamp(seconds)
        return datetime_format.strftime(date_format)
    except:
        return ''


def str_to_timestamp(_str, date_format=SLASH_FORMAT_DATE):
    """
    时间字符转转换成时间戳,常见的几种格式全部包含在里面, convert '06/05/2016' >>> 1565056000
    PARA: '06/05/2016' or '2016-10-20' or '20161020'
    RET: int
    """
    try:
        return datetime_to_timestamp_msec(str_to_datetime(_str, date_format=date_format))
    except:
        datetime_format_list = [FORMAT_DATE, SLASH_FORMAT_DATE, FORMAT_DATE_WITHOUT_SEPARATOR,
                                FORMAT_DATETIME, NO_SECOND_FORMAT_DATETIME]

        for datetime_format in datetime_format_list:
            try:
                return datetime_to_timestamp_second(str_to_datetime(_str, date_format=datetime_format))
            except:
                continue
        return 0


def get_month_range(today=None):
    """
    根据时间计算月份范围，采用前闭后开原则，最后一天则为下个月的第一天
    """
    if not today:
        today = datetime.datetime.today()
    current_time = datetime.datetime(today.year, today.month, today.day)
    current_year = current_time.year
    compute_month = current_time.month
    range_days = calendar.monthrange(current_year, compute_month)[1]
    start_time = current_time.replace(day=1)
    end_time = start_time + datetime.timedelta(days=range_days)
    return start_time, end_time


def str_to_datetime(date_str, date_format=FORMAT_DATE):
    """
    将字符串转换成Datetime
    可转换的类型:'2016-06-30' or '06/30/2016'
    """
    try:
        date = datetime.datetime.strptime(date_str, date_format)
    except:
        try:
            date = datetime.datetime.strptime(date_str, SLASH_FORMAT_DATE)
        except:
            date = datetime.datetime.strptime(date_str, FORMAT_DATE)
    return date


def get_week_start_day(cal_date=None, return_datetime=True):
    """
    RET: 周一的日期(return datetime if return_datetime==True)
    """
    cal_date = cal_date or datetime.date.today()
    cal_datetime = datetime.datetime(cal_date.year, cal_date.month, cal_date.day)

    week_day = cal_datetime.weekday()
    start_datetime = cal_datetime - datetime.timedelta(days=week_day) if week_day else cal_datetime
    return start_datetime if return_datetime else start_datetime.date()


def get_current_week_range(cal_date=None, is_datetime=True):
    """
    RET: 周一的日期， 周日的日期 (return datetime if is_datetime==True)
    """
    start_day = get_week_start_day(cal_date, is_datetime)
    return start_day, start_day + datetime.timedelta(days=6)


def convert_date_range_to_timestamp(date_range_str):
    """
    将时间范围字符串转换成 timestamp
    PARA: '06/21/2016 - 06/22/2016'
    RET: int, int
    """
    datetime_list = date_range_str.split(' - ')
    no_blank_datetime_list = [datetime_.strip() for datetime_ in datetime_list]
    start_timestamp = str_to_timestamp(no_blank_datetime_list[0])
    # 因为筛选的时候得包括后面的这一天
    end_timestamp = str_to_timestamp(no_blank_datetime_list[1]) + 60 * 60 * 24
    return start_timestamp, end_timestamp


def convert_date_range_to_datetime(date_range_str):
    """
    将时间范围字符串转换成datetime
    PARA: '06/21/2016 - 06/22/2016'
    RET: 2016-06-21, 2016-06-22
    """
    start_timestamp, end_timestamp = convert_date_range_to_timestamp(date_range_str)
    return timestamp_to_datetime(start_timestamp), timestamp_to_datetime(end_timestamp)


def convert_datetime_to_point_datetime(datetime_):
    """
    将不是整点的时间转换成整点的
    PARA: datetime_: type(datetime)
    convert:
    2016-09-11 08:30:23
    to:
    2016-09-11
    RET: datetime
    """
    datetime_str = datetime_to_str(datetime_)
    return str_to_datetime(datetime_str)


def get_timestamp_by_day_and_period(day, period):
    """
    更具datetime和一天中的某个片段获取这个时间点的时间戳
    PARA:
    day(type:datetime): eg: 2016-09-10
    period: (type:str)eg:'1'
    RET: timestamp
    """
    datetime_str = datetime_to_str(day)
    whole_datetime_str = '%s %s:0:0' % (datetime_str, FRAGMENT_TYPE.verbose(period))
    whole_datetime = str_to_datetime(whole_datetime_str, FORMAT_DATETIME)
    return datetime_to_timestamp_msec(whole_datetime)


def get_start_time_chinese_str_by_day_and_period(day, period):
    """
    更具datetime和一天中的某个片段获取这个时间点的时间字符串
    PARA:
    day(type:datetime): eg: 2016-09-10
    period: (type:str)eg:'1'
    RET: '2016-06-08 10:38:30':type(str)
    """
    timestamp = get_timestamp_by_day_and_period(day, period)
    return timestamp_to_datetime_str(timestamp)


def get_today_datetime():
    return datetime.datetime.today()


def get_now_datetime_str(date_format=FORMAT_DATETIME_WITHOUT_SEPARATOR):
    """

    """
    return datetime_to_str(datetime.datetime.now(), date_format)


def get_today():
    """

    """
    now = datetime.datetime.now().strftime('%Y-%m-%d')
    return str_to_datetime(now)
