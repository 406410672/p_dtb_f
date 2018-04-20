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


class TaskManager(UploadTaskOperation, GetTaskOperation):
    def __init__(self):
        UploadTaskOperation.__init__(self)
        GetTaskOperation.__init__(self)

    def get_task(self, request_obj):
        response = self._get_task_operation(request_obj)
        return response

    def upload_task(self, request_obj):
        pass


if __name__ == '__main__':
    tm = TaskManager()
    print(tm.get_task({'',''}))