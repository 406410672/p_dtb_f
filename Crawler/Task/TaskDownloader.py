#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/21 11:24
# @Author  : HT
# @Site    : 
# @File    : TaskDownloader.py
# @Software: PyCharm Community Edition
# @Describe: Desc
# @Issues  : Issues

from BaseModule.DateProcessing import *
from BaseModule import HTTPRequest as http
from BaseModule.HTMLParser import HTMLParser as hp
from BaseModule.HTLogger import HTLogger
from Master.Task import Const as C
from Socket.SocketProtocol import *
from Coroutine.AHTTP import SessionManager

from Parser import Task_3_Handler
import asyncio
import functools

class TaskDownloader(HTLogger):
    def __init__(self):
        HTLogger.__init__(self, 'crawler_task_downloader.log')
        # self.logger = HTLogger('crawler_task_downloader.log')

    def _download_task_1(self, task_info):
        self.logger.debug('task1 downloading ')
        items = task_info['items']
        task_id = task_info['task_id']
        crawl_obj = list()
        url = items[0]['url']
        item_response = http.get(url=url)
        parser_data = hp.parser(content=item_response.text, task_info=task_info)
        data = [{'data':parser_data,
                'url':url}]
        data = parser_data
        return data

    def _download_task_2(self, task_info):
        '''
        将task_info里面的任务下载处理完 然后进行返回 上传需要的items
        :param task_info:
        :return:
        '''
        self.logger.debug('task2 downloading ')
        items = task_info['items']
        task_id = task_info['task_id']
        crawl_obj = list()
        data_list = list()
        #遍历处理每个任务
        #并对每个任务进行封装然后返回 预备上传
        for item in items:
            url = item['url']
            category_name = item['category_name']
            item_response = http.get(url='https:'+url)

            parser_data = hp.parser(content=item_response.content, task_info=task_info)
            data = [{'data': parser_data,
                     'category_name': category_name,
                     'url': url}]

            data_list.append(data)
        return data_list

    def _download_task_3(self, task_info):
        '''
        淘宝详情下载
        :param task_info:
        :return:
        '''
        items = task_info['items']
        task_id = task_info['task_id']
        # crawl_obj = list()
        config_list = list()

        #遍历处理每个任务
        #并对每个任务进行封装然后返回 预备上传

        loop = asyncio.get_event_loop()
        config_tasks = list()
        s = SessionManager()
        for item in items:
            url = item['url']
            nid = item['nid']
            compate_url = 'https:' + url
            # item_response = http.get(url='https:' + url)
            cor = s.get_url(url=compate_url)
            task = asyncio.ensure_future(cor)
            task.add_done_callback(functools.partial(Task_3_Handler.config_call_back,
                                                     config_list,
                                                     task_info,
                                                     nid,
                                                     url))
            config_tasks.append(task)
        loop.run_until_complete(asyncio.wait(config_tasks))

        get_other_tasks = list()
        #继续根据config下载
        for config in config_list:
            print(config)
            # Task_3_Handler.get_other_info(config, session=s)
            # task = asyncio.ensure_future(Task_3_Handler.get_other_info(config, session=s,loop=loop))
            # get_other_tasks.append(task)
            tasks = Task_3_Handler.get_other_info_task(config, s)
            get_other_tasks.extend(tasks)
        loop.run_until_complete(asyncio.wait(get_other_tasks))
        loop.stop()
        s.session.close()
        return config_list



if __name__ == '__main__':
    now = lambda  : time.time()
    td = TaskDownloader()
    parm = {'task_id': '3',
            'items': [
                      {'detail_url': '//item.taobao.com/item.htm?id=566332885181&ns=1&abbucket=14#detail',
                       'nid': 'Iphone'},
                      {'detail_url': '//item.taobao.com/item.htm?id=566332885181&ns=1&abbucket=14#detail',
                       'nid': 'Iphone'},
                      {'detail_url': '//item.taobao.com/item.htm?id=566332885181&ns=1&abbucket=14#detail',
                       'nid': 'Iphone'},
                      {'detail_url': '//item.taobao.com/item.htm?id=566332885181&ns=1&abbucket=14#detail',
                       'nid': 'Iphone'},
                      {'detail_url': '//item.taobao.com/item.htm?id=566332885181&ns=1&abbucket=14#detail',
                       'nid': 'Iphone'},
                      {'detail_url': '//item.taobao.com/item.htm?id=566332885181&ns=1&abbucket=14#detail',
                       'nid': 'Iphone'},
                      {'detail_url': '//item.taobao.com/item.htm?id=566332885181&ns=1&abbucket=14#detail',
                       'nid': 'Iphone'},
                      {'detail_url': '//item.taobao.com/item.htm?id=566332885181&ns=1&abbucket=14#detail',
                       'nid': 'Iphone'},
                      {'detail_url': '//item.taobao.com/item.htm?id=566332885181&ns=1&abbucket=14#detail',
                       'nid': 'Iphone'},
                      {'detail_url': '//item.taobao.com/item.htm?id=566332885181&ns=1&abbucket=14#detail',
                       'nid': 'Iphone'},
                      {'detail_url': '//item.taobao.com/item.htm?id=566332885181&ns=1&abbucket=14#detail',
                       'nid': 'Iphone'},
                      {'detail_url': '//item.taobao.com/item.htm?id=566332885181&ns=1&abbucket=14#detail',
                       'nid': 'Iphone'},
                      {'detail_url': '//item.taobao.com/item.htm?id=566332885181&ns=1&abbucket=14#detail',
                       'nid': 'Iphone'},
                      {'detail_url': '//item.taobao.com/item.htm?id=566332885181&ns=1&abbucket=14#detail',
                       'nid': 'Iphone'},
                      {'detail_url': '//item.taobao.com/item.htm?id=566332885181&ns=1&abbucket=14#detail',
                       'nid': 'Iphone'},
                      {'detail_url': '//item.taobao.com/item.htm?id=566332885181&ns=1&abbucket=14#detail',
                       'nid': 'Iphone'},
                      {'detail_url': '//item.taobao.com/item.htm?id=566332885181&ns=1&abbucket=14#detail',
                       'nid': 'Iphone'},
                      {'detail_url': '//item.taobao.com/item.htm?id=566332885181&ns=1&abbucket=14#detail',
                       'nid': 'Iphone'},
                      {'detail_url': '//item.taobao.com/item.htm?id=566332885181&ns=1&abbucket=14#detail',
                       'nid': 'Iphone'},
                      {'detail_url': '//item.taobao.com/item.htm?id=566332885181&ns=1&abbucket=14#detail',
                       'nid': 'Iphone'},
                      {'detail_url': '//item.taobao.com/item.htm?id=566332885181&ns=1&abbucket=14#detail',
                       'nid': 'Iphone'},
                      {'detail_url': '//item.taobao.com/item.htm?id=566332885181&ns=1&abbucket=14#detail',
                       'nid': 'Iphone'},
                      {'detail_url': '//item.taobao.com/item.htm?id=566332885181&ns=1&abbucket=14#detail',
                       'nid': 'Iphone'},
                      {'detail_url': '//item.taobao.com/item.htm?id=566332885181&ns=1&abbucket=14#detail',
                       'nid': 'Iphone'},
                      {'detail_url': '//item.taobao.com/item.htm?id=566332885181&ns=1&abbucket=14#detail',
                       'nid': 'Iphone'},
                      {'detail_url': '//item.taobao.com/item.htm?id=566332885181&ns=1&abbucket=14#detail',
                       'nid': 'Iphone'},
                      {'detail_url': '//item.taobao.com/item.htm?id=566332885181&ns=1&abbucket=14#detail',
                       'nid': 'Iphone'},
                      {'detail_url': '//item.taobao.com/item.htm?id=566332885181&ns=1&abbucket=14#detail',
                       'nid': 'Iphone'},
                      {'detail_url': '//item.taobao.com/item.htm?id=566332885181&ns=1&abbucket=14#detail',
                       'nid': 'Iphone'}]}
    parm = {'task_id': '3',
            'items': [
                {'detail_url': '//item.taobao.com/item.htm?id=566332885181&ns=1&abbucket=14#detail',
                 'nid': 'Iphone'}]}
    start = now()
    dl = td._download_task_3(parm)
    print(dl)
    print('task num:{}'.format(parm.get('items').__len__()))
    print(now() - start)
    # import json
    # print(json.dumps(dl))