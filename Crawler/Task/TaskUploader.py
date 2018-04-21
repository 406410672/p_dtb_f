#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/21 14:15
# @Author  : HT
# @Site    : 
# @File    : TaskUploader.py
# @Software: PyCharm Community Edition
# @Describe: Desc
# @Issues  : Issues

from BaseModule.DateProcessing import *
from BaseModule import HTTPRequest as http
from BaseModule.HTMLParser import HTMLParser as hp
from Master.Task import Const as C
from Socket.SocketProtocol import *

class TaskUploader(object):
    def __init__(self):
        pass


    def _upload_task_1(self, data, task_info, crawler):
        client_id = crawler.clientId
        domain = task_info['domain']
        parse_rule = task_info[PARSE_RULE]
        storage_rule = task_info[STORAGE_RULE]

