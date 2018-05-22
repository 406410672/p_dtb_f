#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/21 13:54
# @Author  : HT
# @Site    : 
# @File    : CrawlerManager.py
# @Software: PyCharm Community Edition
# @Describe: Desc
# @Issues  : Issues

import sys
import os
import json
import time

from Crawler.BaseCrawler import *
from threading import Thread
from Crawler.Task.TaskManager import TaskManager as tk
from multiprocessing import Process
from gevent.monkey import patch_socket
import gevent

class CrawlerManager(BaseCrawler):
    def __init__(self):
        BaseCrawler.__init__(self, 'crawler.log')
        # Thread.__init__(self)
        self.task_manager = tk()
        self.threads = list()

    def crawl(self):
        task = self.application_task()
        task_num = task['task_nums']
        items = task['items']
        if int(task_num) == 0 or items is None or len(items) == 0:
            self.logger.debug('没有需要处理的任务')
        else:
            data = self.task_manager.processing_task(task)
            if data is None:
                self.logger.error('get date error for task:{}'.format(task))
            else:
                response = self.task_manager.upload_data(data, task, self)
                self.logger.debug('upload result :{}'.format(response))

    def application_task(self):
        time = datetime_to_timestamp(get_datestr())
        parm = {pc.MSG_TYPE: pc.APPLICATION_TASKS, pc.CLIENT_ID: self.clientId, pc.REQUEST_TIME: time}
        response = self.socketClient.send(json.dumps(parm))
        response_dict = json.loads(response)
        error = response_dict.get(pc.ERROR)
        if error :
            self.logger.error('application task error:%s'%(response_dict))
            return None
        else:
            # self.task_manager.processing_task(response_dict)
            return response_dict

    def process_crawl_scheduler(self):
        # while True:
        #     for thread in self.threads:
        #         if thread.isAlive() is not True:
        #             self.threads.remove(thread)
        #     self.logger.debug('current threads num:%s'%(len(self.threads)))
        #     if len(self.threads) >= 5:
        #         time.sleep(5)
        #         continue
        #     try:
        #         t = Thread(target=self.crawl, name='application tasks')
        #         t.setDaemon(True)
        #         self.threads.append(t)
        #         t.start()
        #         time.sleep(5)
        #     except Exception as error:
        #         self.logger.error('create thread error:{}'.format(error))
        #         time.sleep(5)
        while True:
            self.crawl()
            time.sleep(5)

    def run(self):
        BaseCrawler.actionCrawler(self)
        self.process_crawl_scheduler()


if __name__ == '__main__':
    am = CrawlerManager()
    process = Process(target=am.run)
    process.start()
    process.join()
    # from pickle import Pickler
    # file = {'log_to_stderr': False, 'authkey': b'\x12\xe5\xff4\x1f\n\xc0\x1c\xf1\xb7\xe2\x16\x83\xbd\xb8\x86\xc0ZM\xff\xba\xdaT1)\xf0\xed\x9d\xa1\xb7\x96\xad', 'name': 'Process-1', 'sys_path': ['C:\\Users\\18316\\Desktop\\p_dtb_f\\Crawler', 'C:\\Users\\18316\\Desktop\\p_dtb_f', 'C:\\Users\\18316\\Anaconda3\\python36.zip', 'C:\\Users\\18316\\Anaconda3\\DLLs', 'C:\\Users\\18316\\Anaconda3\\lib', 'C:\\Users\\18316\\Anaconda3', 'C:\\Users\\18316\\Anaconda3\\lib\\site-packages', 'C:\\Users\\18316\\Anaconda3\\lib\\site-packages\\Babel-2.5.0-py3.6.egg', 'C:\\Users\\18316\\Anaconda3\\lib\\site-packages\\win32', 'C:\\Users\\18316\\Anaconda3\\lib\\site-packages\\win32\\lib', 'C:\\Users\\18316\\Anaconda3\\lib\\site-packages\\Pythonwin', 'C:\\Users\\18316\\Desktop\\p_dtb_f\\Crawler\\..'], 'sys_argv': ['C:/Users/18316/Desktop/p_dtb_f/Crawler/CrawlerManager.py'], 'orig_dir': 'C:\\Users\\18316\\Desktop\\p_dtb_f\\Crawler', 'dir': 'C:\\Users\\18316\\Desktop\\p_dtb_f\\Crawler', 'start_method': 'spawn', 'init_main_from_path': 'C:\\Users\\18316\\Desktop\\p_dtb_f\\Crawler\\CrawlerManager.py'}
    # Pickler(file)
    # am.setDaemon(True)
    # am.start()
    # am.join()