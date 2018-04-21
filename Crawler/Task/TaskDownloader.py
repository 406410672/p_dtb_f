#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/21 11:24
# @Author  : HT
# @Site    : 
# @File    : TaskDownloader.py
# @Software: PyCharm Community Edition
# @Describe: Desc
# @Issues  : Issues

from BaseModule.DateProcessing import *
from BaseModule import HTTPRequest as http
from BaseModule.HTMLParser import HTMLParser as hp
from Master.Task import Const as C
from Socket.SocketProtocol import *

class TaskDownloader(object):
    def __init__(self):
        pass


    def _download_task_1(self, task_info):
        parse_rule = task_info[PARSE_RULE]
        storage_rule = task_info[STORAGE_RULE]
        items = task_info['items']
        task_id = task_info['task_id']
        domain = task_info['domain']

        crawl_obj = list()
        for item in items:
            url = item['url']
            item_response = http.get(url=url)
            crawl_obj.append(item_response.content)

        for content in crawl_obj:
            data = hp.parser(content=content, task_info=task_info)
            return data