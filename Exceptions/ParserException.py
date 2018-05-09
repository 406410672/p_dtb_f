#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/7 15:45
# @Author  : HT
# @Site    :
# @File    : ParserException.py
# @Software: PyCharm Community Edition
# @Describe: Desc
# @Issues  : Issues

class TaoBaoItemParserException(Exception):
    def __init__(self, error):
        Exception.__init__(self, '淘宝item解析出错，或者没有结果。')