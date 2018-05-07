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

from gevent import monkey; monkey.patch_socket()
import gevent
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
        crawl_obj = list()
        data_list = list()
        #遍历处理每个任务
        #并对每个任务进行封装然后返回 预备上传
        for item in items:
            url = item['detail_url']
            category_name = item['nid']
            compate_url = 'https:' + url
            gevent.spawn(http.get(compate_url))
            # item_response = http.get(url='https:' + url)

            parser_data = hp.parser(content=item_response.content, task_info=task_info)
            data = [{'data': parser_data,
                     'category_name': category_name,
                     'url': url}]

            data_list.append(data)
        return data_list



if __name__ == '__main__':
    td = TaskDownloader()
    parm = {'task_id':'2',
            'items':[{'url':'https://s.taobao.com/list?spm=a21bo.7723600.8557.3.6ad85ec9YilCta&app=vproduct&vlist=1&q=iphone&cat=1512&from_type=3c',
            'category_name':'Iphone'}]}
    dl = td._download_task_2(parm)
    import json
    print(json.dumps(dl))