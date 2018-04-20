#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/20 14:33
# @Author  : HT
# @Site    : 
# @File    : GetTaskOperation.py
# @Software: PyCharm Community Edition
# @Describe: Desc
# @Issues  : Issues

from Master.Task.TaskOperation.BaseOperation import *

class GetTaskOperation(BaseOperation):
    def __init__(self):
        BaseOperation.__init__(self)

    def _get_task_operation(self, request_obj):
        attr = getattr(self, random.choice(ts.get_task), None)
        response = attr(request_obj)
        return response

    def get_taobao_task(self, request_obj):
        taobao = self.mongodb.taobao
        taobao_seed = taobao.taobao_seed
        if taobao_seed.count() == 0:
            taobao_seed.create_index([(C.INSERT_TIME,DESCENDING)])
        response = dict()
        #获取任务id == 1
        update_data = {C.CRAWL_STATUS: C.CRAWL_DOWNING, C.CRAWL_TIME: datetime.datetime.now()}
        update_data = {'test':'1'}
        record = taobao_seed.find_one_and_update(
            {'$and': [{'$or': [{C.CRAWL_STATUS: C.CRAWL_NEW}, {C.CRAWL_STATUS: None}, {C.CRAWL_STATUS: {'$exists': False}}]},
                     {C.TASK_ID : 1}]},
            {'$set': update_data},
            upsert=False,
            sort=[(C.INSERT_TIME, DESCENDING)],  # 2018-01-31修改，根据接待时间的倒序去下载（最新的客户）
            returnNewDocument=False
        )
        if record:
            response.update(record)
            del response['_id']
            del response[C.INSERT_TIME]
            task_id = str(int(response[C.TASK_ID]))
            response[pc.PARSE_RULE] = ts.task_parse_rule[task_id]
            response[pc.STORAGE_RULE] = ts.task_storage_rule[task_id]
            return response
        else:
            return None

if __name__ == '__main__':
    to = GetTaskOperation()
    response = to.get_taobao_task('r')
    print(json.dumps(response))
