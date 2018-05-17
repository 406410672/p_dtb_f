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
        '''
        依据get_task顺序获取数据
        :param request_obj:
        :return:
        '''
        for fun in ts.get_task:
            attr = getattr(self, fun, None)
            response = attr(request_obj)
            if int(response['task_nums']) != 0:
                return response
        return response

    # def _get_task_1(self, request_obj):
    #     taobao = self.mongodb.taobao
    #     taobao_seed = taobao.taobao_seed
    #     if taobao_seed.count() == 0:
    #         taobao_seed.create_index([(C.INSERT_TIME,DESCENDING)])
    #     response = dict()
    #     #获取任务id == 1
    #     update_data = {C.CRAWL_STATUS: C.CRAWL_DOWNING, C.CRAWL_TIME:datetime_to_timestamp(get_datestr())}
    #     record = taobao_seed.find_one_and_update(
    #         {'$and': [{'$or': [{C.CRAWL_STATUS: C.CRAWL_NEW}, {C.CRAWL_STATUS: None}, {C.CRAWL_STATUS: {'$exists': False}}]},
    #                  {C.TASK_ID : '1'}]},
    #         {'$set': update_data},
    #         upsert=False,
    #         sort=[(C.INSERT_TIME, DESCENDING)],  # 2018-01-31修改，根据接待时间的倒序去下载（最新的客户）
    #         returnNewDocument=False
    #     )
    #     if record:
    #         response['task_nums'] = '1'
    #         response['items'] = [{'url':record['url']}]
    #         response['task_name'] = record['task_name']
    #         response['task_id'] = record['task_id']
    #         return response
    #     else:
    #         response['task_nums'] = '0'
    #         response['items'] = []
    #         response['task_name'] = ''
    #         response['task_id'] = ''
    #         return response
    #
    # def _get_task_2(self, request_obj):
    #     taobao = self.mongodb.taobao
    #     taobao_seed = taobao.taobao_seed
    #     if taobao_seed.count() == 0:
    #         taobao_seed.create_index([(C.INSERT_TIME, DESCENDING)])
    #     # response = dict()
    #     # 获取任务id == 1
    #     # update_data = {C.CRAWL_STATUS: C.CRAWL_DOWNING, C.CRAWL_TIME: datetime_to_timestamp(get_datestr())}
    #     records = taobao_seed.find(
    #         {'$and': [
    #             {'$or': [{C.CRAWL_STATUS: C.CRAWL_NEW}, {C.CRAWL_STATUS: None}, {C.CRAWL_STATUS: {'$exists': False}}]},
    #             {C.TASK_ID: '2'}
    #         ]},
    #         sort=[(C.INSERT_TIME, DESCENDING)],
    #         limit=10
    #     )
    #     num_task = 0
    #     urls = []
    #     items = []
    #     response = dict()
    #     for record in records:
    #         num_task += 1
    #         url = record['url']
    #         category_name = record['category_name']
    #         urls.append({'url':url})
    #         item = {'url':url,'category_name':category_name}
    #         items.append(item)
    #     if len(items) > 0:
    #         response = {
    #             'task_name': '淘宝商品二级分类或者商品信息获取_数码家电',
    #             'task_id': '2',
    #             'items': items,
    #             'task_nums': str(num_task),
    #         }
    #         taobao_seed.update_many({'$or': urls}, {'$set': {C.CRAWL_STATUS: C.CRAWL_DOWNING}})
    #
    #         return response
    #     else:
    #         response['task_nums'] = 0
    #         response['items'] = []
    #         response['task_name'] = ''
    #         response['task_id'] = ''
    #         return response

    def _get_task_3(self, request_obj):
        '''
        淘宝商品详情爬取
        :param request_obj:
        :return:
        '''
        taobao = self.mongodb.taobao6
        taobao_item = taobao.taobao_item

        records = taobao_item.find(
            {'$and': [
                {'$or': [{C.CRAWL_STATUS: C.CRAWL_NEW}, {C.CRAWL_STATUS: None}, {C.CRAWL_STATUS: {'$exists': False}}]},
                {'detail_url': {'$regex': 'taobao.com'}}
            ]},
            sort=[('comment_count', DESCENDING)],
            limit=50
        )
        num_task = 0
        _ids = []
        items = []
        response = dict()
        print(records)
        for record in records:
            num_task += 1
            url = record['detail_url']
            _id = record['_id']
            nid = record['nid']
            _ids.append({'_id': _id})
            item = {'url': url, 'nid': nid}
            items.append(item)
        if len(items) > 0:
            response = {
                'task_name': '淘宝商品详情爬取',
                'task_id': '3',
                'items': items,
                'task_nums': str(num_task),
            }
            taobao_item.update_many({'$or': _ids}, {'$set': {C.CRAWL_STATUS: C.CRAWL_DOWNING}})
            return response
        else:
            response['task_nums'] = 0
            response['items'] = []
            response['task_name'] = ''
            response['task_id'] = ''
            return response

    def _get_task_4(self, request_obj):
        '''
        淘宝商品详情爬取
        :param request_obj:
        :return:
        '''
        taobao = self.mongodb.taobao6
        taobao_item = taobao.taobao_item_detail

        records = taobao_item.find(

                {'$or': [{C.CRAWL_STATUS: C.CRAWL_NEW}, {C.CRAWL_STATUS: None}, {C.CRAWL_STATUS: {'$exists': False}}]},

            sort=[('insert_time', DESCENDING)],
            limit=50
        )
        num_task = 0
        _nids = []
        items = []
        response = dict()
        for record in records:
            num_task += 1
            import json
            from BaseModule import JsonDecoder
            # print(record)
            # print(json.dumps(record, cls=JsonDecoder.HTJsonEncoder))
            url = record['url']
            data = record['data']

            sibUrl = data['sibUrl']
            _id = record['nid']
            nid = record['nid']
            _nids.append({'nid': _id})
            item = {'itemurl': url, 'nid': nid, 'sibUrl':sibUrl}
            items.append(item)
        if len(items) > 0:
            response = {
                'task_name': '淘宝商品详情子数据商品分类及销售信息获取',
                'task_id': '4',
                'items': items,
                'task_nums': str(num_task),
            }
            taobao_item.update_many({'$or': _nids}, {'$set': {C.CRAWL_STATUS: C.CRAWL_DOWNING}})
            return response
        else:
            response['task_nums'] = 0
            response['items'] = []
            response['task_name'] = ''
            response['task_id'] = ''
            return response

if __name__ == '__main__':
    to = GetTaskOperation()
    response = to._get_task_4('r')
    print(response)
    # print(json.dumps(response))
