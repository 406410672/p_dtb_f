#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/12 17:36
# @Author  : HT
# @Site    : 
# @File    : JsonDecoder.py
# @Software: PyCharm Community Edition
# @Describe: Desc
# @Issues  : Issues
import json
import datetime
from datetime import *
from bson.objectid import ObjectId

class HTJsonEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(obj, date):
            return obj.strftime('%Y-%m-%d')
        elif isinstance(obj, ObjectId):
            # print(obj)
            return str(obj)
        else:
            return json.JSONEncoder.default(self, obj)
