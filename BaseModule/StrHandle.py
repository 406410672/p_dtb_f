#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/9 14:05
# @Author  : HT
# @Site    : 
# @File    : StrHandle.py
# @Software: PyCharm Community Edition
# @Describe: Desc
# @Issues  : Issues

def convert_unicodestr2str(str):
    try:
        result_str = str.encode('latin-1').decode('unicode_escape')
        return result_str
    except UnicodeEncodeError as error:
        print('encode error:{}'.format(error))
        return str
