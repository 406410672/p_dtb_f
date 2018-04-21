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


    def _upload_task_1(self, request_obj):
        try:
            task_id = str(request_obj[C.TASK_ID])
            response = dict()
            items = request_obj[C.ITEMS]

            # 淘宝一级分类只有一个
            item = items[0]
            next_id = '2'
            task_name = '淘宝商品二级分类或者商品信息获取_数码家电'
            last_url = item['url']

            storage_rule = ts.task_storage_rule[str(task_id)]
            db = storage_rule[C.STORAGE_DB]
            table = storage_rule[C.STORAGE_TABLE]
            target = storage_rule[C.STORAGE_TARGET]

            if target == 'mongodb':
                db = self.mongodb[db]
                collection = db[table]
                if collection.count() == 0:
                    collection.create_index([("insert_time", DESCENDING)])
                for item in item['data']:
                    item[C.INSERT_TIME] = datetime_to_timestamp(get_current_datestr())
                    item['last_url'] = last_url
                    item['task_id'] = next_id
                    item['task_name'] = task_name
                    collection.insert(item)
        except KeyError as error:
            response[pc.ERROR] = pc.ERR_UPLOAD_TASK
            response[pc.ERROR_INFO] = 'upload key error'
            return response
        except Exception as error:
            response[pc.ERROR] = pc.ERR_UPLOAD_TASK
            response[pc.ERROR_INFO] = 'upload error,other error'
            return response
        return response

    def _upload_task_2(self, request_obj):
        task_id = str(request_obj[C.TASK_ID])
        response = dict()
        items = request_obj[C.ITEMS]

        next_id = '3'
        task_name = '淘宝商品信息_数码家电'

        storage_rule = ts.task_storage_rule[str(task_id)]
        db = storage_rule[C.STORAGE_DB]
        table = storage_rule[C.STORAGE_TABLE]
        target = storage_rule[C.STORAGE_TARGET]

        if target == 'mongodb':
            db = self.mongodb[db]
            collection = db[table]
            if collection.count() == 0:
                collection.create_index([("insert_time", DESCENDING)])

            for item_dict in items:
                last_url = item_dict['url']
                category_name = item_dict['category_name']
                time = datetime_to_timestamp(get_current_datestr())
                datas = item_dict['data']
                for data in datas:
                    insert_obj = dict()
                    insert_obj[C.INSERT_TIME] = datetime_to_timestamp(get_current_datestr())
                    insert_obj['last_url'] = last_url
                    insert_obj['task_id'] = next_id
                    insert_obj['task_name'] = task_name
                    collection.insert(insert_obj)
        return
        try:
            task_id = str(request_obj[C.TASK_ID])
            response = dict()
            items = request_obj[C.ITEMS]

            next_id = '3'
            task_name = '淘宝商品信息_数码家电'

            storage_rule = ts.task_storage_rule[str(task_id)]
            db = storage_rule[C.STORAGE_DB]
            table = storage_rule[C.STORAGE_TABLE]
            target = storage_rule[C.STORAGE_TARGET]

            if target == 'mongodb':
                db = self.mongodb[db]
                collection = db[table]
                if collection.count() == 0:
                    collection.create_index([("insert_time", DESCENDING)])

                for item_dict in items:
                    last_url = item_dict['url']
                    category_name = item_dict['category_name']
                    time =  datetime_to_timestamp(get_current_datestr())
                    datas = item_dict['data']
                    for data in datas:
                        insert_obj = dict()
                        insert_obj[C.INSERT_TIME] = datetime_to_timestamp(get_current_datestr())
                        insert_obj['last_url'] = last_url
                        insert_obj['task_id'] = next_id
                        insert_obj['task_name'] = task_name
                        collection.insert(insert_obj)


        except KeyError as error:
            response[pc.ERROR] = pc.ERR_UPLOAD_TASK
            response[pc.ERROR_INFO] = 'upload key error'
            return response
        except Exception as error:
            response[pc.ERROR] = pc.ERR_UPLOAD_TASK
            response[pc.ERROR_INFO] = 'upload error,other error'
            return response
        return response


if __name__ == '__main__':
    r = {1:2}
    print(r)
    print(r[1])
