#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/19 14:13
# @Author  : HT
# @Site    : 
# @File    : DateProcessing.py
# @Software: PyCharm Community Edition
# @Describe: Desc
# @Issues  : Issues
try:
    import platform
    if platform.python_version()[0] == 2:
        import sys
        sys.setdefaultencoding('utf8')
except Exception as error:
    print('setdefaultencoding error:{}'.format(error))

import time
import datetime


def time_stamp_to_time(timestamp, format="%Y-%m-%d %H:%M:%S"):
    '''
    将[str]或者[int]的时间戳，转换为对应[format]的时间字符串
    :param timestamp:
    :param format:
    :return:
    '''
    if timestamp is None:
        return '0'
    time_local = time.localtime(int(timestamp))
    dt = time.strftime(format, time_local)
    return dt


def get_current_datestr():
    return get_datestr(delta=0)


def get_datestr(delta=0):
    '''
    根据变量[delta]字符串形式的当前时间
    :param delta:
    :return:
    '''
    c_date = datetime.datetime.now()
    d_date = datetime.timedelta(days=delta)
    date_str = str(c_date + d_date)
    date_str = date_str[:-7]
    return date_str


def datetime_to_timestamp(datestr, format="%Y-%m-%d %H:%M:%S"):
    '''
    根据format格式转换时间、日期字符串为时间戳
    :param datestr:
    :param format:
    :return: type of [int]
    '''
    assert isinstance(datestr, str), 'datetime must date str'
    timearray = time.strptime(datestr, format)

    timestamp = int(time.mktime(timearray))
    return timestamp