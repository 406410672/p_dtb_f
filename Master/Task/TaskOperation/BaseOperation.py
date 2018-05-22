#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/20 18:06
# @Author  : HT
# @Site    : 
# @File    : BaseOperation.py
# @Software: PyCharm Community Edition
# @Describe: Desc
# @Issues  : Issues

import random
import datetime
from pymongo import MongoClient
from pymongo import ASCENDING,DESCENDING
from BaseModule.Configloader import Configloader

import json
from Master.Task import Const as C
from Socket import SocketProtocol as pc
from Master.Task.TaskOperation import task_setting as ts
from BaseModule.DateProcessing import *
from BaseModule.HTLogger import HTLogger
try:
    # Python 3.x
    from urllib.parse import quote_plus
except ImportError:
    # Python 2.x
    from urllib import quote_plus

class BaseOperation(HTLogger):
    def __init__(self):
        HTLogger.__init__(self, 'master_task_operation.log')
        self.configloader = Configloader()
        uri = "mongodb://%s:%s@%s" % (
            quote_plus(self.configloader.mongodb_user), quote_plus(self.configloader.mongodb_password),
            self.configloader.mongodb_host)
        self.mongodb = MongoClient(uri)
        # self.logger = HTLogger('master_task_operation.log')

if __name__ == '__main__':
    op = BaseOperation()
    op.logger.error('tets')