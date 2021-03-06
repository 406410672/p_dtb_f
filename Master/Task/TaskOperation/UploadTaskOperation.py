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

now = lambda: time.time()
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
        # return
        return response

    def _upload_task_3(self, request_obj):
        '''
        淘宝商品详情
        :param request_obj:
        :return:
        '''
        task_id = str(request_obj[C.TASK_ID])
        response = dict()
        items = request_obj[C.ITEMS]
        taobao = self.mongodb.taobao6
        taobao_item_detail_new = taobao.taobao_item_detail_new
        if taobao_item_detail_new.count() == 0:
            taobao_item_detail_new.create_index([(C.INSERT_TIME,DESCENDING)])
        # insert_list = list()
        try:
            for item_dict in items:
                # insert_data = dict()
                # nid = item_dict['nid']
                # data = insert_data['data']
                # insert_data['_id'] = item_dict['nid']
                item_dict['insert_time'] = now()

                # insert_data.update(data)
                # insert_list.append(insert_data)
            taobao_item_detail_new.insert_many(items, ordered=False)
        except Exception as error:
            self.logger.error('insert set 3 error:{}'.format(error))

            response[pc.ERROR] = pc.ERR_UPLOAD_TASK
            response[pc.ERROR_INFO] = str(error)

        return response
    # def _upload_task_4(self, request_obj):
    #     '''
    #     淘宝商品详情子数据商品分类及销售信息获取
    #     :param request_obj:
    #     :return:
    #     '''
    #     task_id = str(request_obj[C.TASK_ID])
    #     response = dict()
    #     items = request_obj[C.ITEMS]
    #     taobao = self.mongodb.taobao6
    #     taobao_item_detail = taobao.taobao_item_detail
    #     if taobao_item_detail.count() == 0:
    #         taobao_item_detail.create_index([(C.INSERT_TIME,DESCENDING)])
    #     insert_list = list()
    #     for item_dict in items:
    #         insert_data = dict()
    #         nid = item_dict['nid']
    #         data = insert_data['data']
    #         insert_data['_id'] = item_dict['nid']
    #         insert_data['insert_time'] = time.time()
    #         insert_data.update(data)
    #         insert_list.append(insert_data)
    #     taobao_item_detail.insert_many(insert_list, ordered=False)


if __name__ == '__main__':
    r = {1:2}
    print(r)
    print(r[1])
