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
from Socket import SocketProtocol as pc
import json
from Socket.SocketProtocol import *

class TaskUploader(object):
    def __init__(self):
        pass

    def _upload_task_1(self, data, task_info, crawler):
        client_id = crawler.clientId
        task_name = task_info['task_name']
        url = task_info['items'][0]['url']
        time = datetime_to_timestamp(get_datestr())

        parm =  {
            pc.MSG_TYPE : pc.UPLOAD_TASKS,
            'task_name' : task_name,
            'items' : [{'url':url,'data':data}],
            'task_id' : 1,
            'request_time' : time,
            pc.CLIENT_ID : client_id
        }
        response = crawler.socketClient.send(json.dumps(parm))
        return response

    def _upload_task_2(self, data, task_info, crawler):
        client_id = crawler.clientId
        task_name = task_info['task_name']

        time = datetime_to_timestamp(get_datestr())

        parm =  {
            pc.MSG_TYPE : pc.UPLOAD_TASKS,
            'task_name' : task_name,
            'items' : data,
            'task_id' : '2',
            'request_time' : time,
            pc.CLIENT_ID : client_id
        }
        print('上传的数据{}'.format(json.dumps(parm)))
        response = crawler.socketClient.send(json.dumps(parm))
        return response

    def _upload_task_3(self, data, task_info, crawler):
        client_id = crawler.clientId
        task_name = task_info['task_name']

        time = datetime_to_timestamp(get_datestr())

        parm = {
            pc.MSG_TYPE: pc.UPLOAD_TASKS,
            'task_name': task_name,
            'items': data,
            'task_id': '3',
            'request_time': time,
            pc.CLIENT_ID: client_id
        }
        print('上传的数据{}'.format(json.dumps(parm)))
        response = crawler.socketClient.send(json.dumps(parm))
        return response