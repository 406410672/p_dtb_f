#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/20 14:33
# @Author  : HT
# @Site    : 
# @File    : UploadTaskOperation.py
# @Software: PyCharm Community Edition
# @Describe: Desc
# @Issues  : Issues



from Master.Task.TaskOperation.BaseOperation import *



class UploadTaskOperation(BaseOperation):
    def __init__(self):
        BaseOperation.__init__(self)


    def _upload_taobao_task(self, request_obj):
        task_id = request_obj[C.TASK_ID]
        response = dict()
        if int(task_id) == 1:
            try:
                items = request_obj[C.ITEMS]
                next_id = 2
                task_name = '淘宝商品二级分类或者商品信息获取_数码家电'
                last_url = request_obj['url']

                storage_rule = ts.task_storage_rule[task_id]
                db = storage_rule[C.STORAGE_DB]
                table = storage_rule[C.STORAGE_TABLE]
                target = storage_rule[C.STORAGE_TARGET]

                if target == 'mongodb':
                    db = self.mongodb[db]
                    collection = db[table]
                    if collection.count() == 0:
                        collection.create_index([("insert_time", DESCENDING)])
                    for item in items:
                        item[C.INSERT_TIME] = datetime_to_timestamp(get_current_datestr())
                        collection.insert(item)
            except Exception as error:
                response[pc.ERROR] = pc.ERR_UPLOAD_TASK
                response[pc.ERROR_INFO] = error
                return response
        return response


if __name__ == '__main__':
    r = {1:2}
    print(r)
    print(r[1])
