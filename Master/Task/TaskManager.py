#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/20 11:11
# @Author  : HT
# @Site    : 
# @File    : TaskManager.py
# @Software: PyCharm Community Edition
# @Describe: Desc
# @Issues  : Issues

from Master.Task.TaskOperation.GetTaskOperation import GetTaskOperation
from Master.Task.TaskOperation.UploadTaskOperation import UploadTaskOperation
from Master.Task import Const as C

class TaskManager(UploadTaskOperation, GetTaskOperation):
    def __init__(self):
        UploadTaskOperation.__init__(self)
        GetTaskOperation.__init__(self)

    def get_task(self, request_obj):
        response = self._get_task_operation(request_obj)
        return response

    def upload_task(self, request_obj):
        if request_obj[C.TASK_ID] == '1':
            #淘宝分类获取
            response = self._upload_task_1(request_obj)
        elif request_obj[C.TASK_ID] == '2':
            #淘宝分类获取
            response = self._upload_task_2(request_obj)
        elif request_obj[C.TASK_ID] == '3':
            #淘宝商品详情获取
            response = self._upload_task_3(request_obj)
        elif request_obj[C.TASK_ID] == '4':
            #淘宝商品详情Sib获取
            response = self._upload_task_4(request_obj)

        return response


if __name__ == '__main__':
    tm = TaskManager()
    # print(
    import json
    print(json.dumps(tm.get_task({'':''})))