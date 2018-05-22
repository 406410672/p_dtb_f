#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/21 11:24
# @Author  : HT
# @Site    : 
# @File    : TaskManager.py
# @Software: PyCharm Community Edition
# @Describe: Desc
# @Issues  : Issues


from Crawler.Task.TaskDownloader import TaskDownloader
from Crawler.Task.TaskUploader import TaskUploader
from Socket.SocketProtocol import *

class TaskManager(TaskDownloader, TaskUploader):
    def __init__(self):
        TaskDownloader.__init__(self)
        TaskUploader.__init__(self)

    def processing_task(self, task_info):
        task_id = task_info['task_id']
        data = None
        if task_id is None:
            return None
        if task_id == '1':
            data = self._download_task_1(task_info)
        elif task_id == '2':
            data = self._download_task_2(task_info)
        elif task_id == '3':
            data = self._download_task_3(task_info)
        return data

    def upload_data(self, data, task_info, crawler):
        task_id = task_info['task_id']
        if task_id == '1':
            response = self._upload_task_1(data, task_info, crawler)
            return response
        elif task_id == '2':
            response = self._upload_task_2(data, task_info, crawler)
            return response
        elif task_id == '3':
            response = self._upload_task_3(data, task_info, crawler)
            return response

def TaobaoItemdetail_pressure():
    from Master.Task.TaskManager import TaskManager as tk
    m_tm = tk()
    import datetime
    d_t = lambda : datetime.datetime.now()
    while True:
        tasks = m_tm.get_task({'': ''})
        print('task_lens:{}'.format(len(tasks)))

        tm =TaskManager()
        import time
        now = lambda :time.time()
        start = now()
        datas = tm.processing_task(tasks)

        for data in datas:
            data['insert_time'] = d_t()

        taobao = m_tm.mongodb.taobao6
        taobao_item_detail = taobao.taobao_item_detail
        try:
            taobao_item_detail.insert_many(datas, ordered=False)
        except Exception as error:
            print('插入出错{}'.format(error))
        print('insert_date:{}'.format(len(datas)))
        print('cost, ',now() - start)

#     10:30
if __name__ == '__main__':
    TaobaoItemdetail_pressure()
    # tm =TaskManager()
    # import time
    # now = lambda :time.time()
    # start = now()
    # data = tm.processing_task({'task_name': '淘宝商品详情爬取', 'task_id': '3', 'items': [{'url': '//item.taobao.com/item.htm?id=566019208402&ns=1&abbucket=0#detail', 'nid': '566019208402'}, {'url': '//item.taobao.com/item.htm?id=568782374247&ns=1&abbucket=0#detail', 'nid': '568782374247'}, {'url': '//item.taobao.com/item.htm?id=567217064636&ns=1&abbucket=0#detail', 'nid': '567217064636'}, {'url': '//item.taobao.com/item.htm?id=566671867399&ns=1&abbucket=0#detail', 'nid': '566671867399'}, {'url': '//item.taobao.com/item.htm?id=567325175248&ns=1&abbucket=0#detail', 'nid': '567325175248'}, {'url': '//item.taobao.com/item.htm?id=561554453282&ns=1&abbucket=0#detail', 'nid': '561554453282'}, {'url': '//item.taobao.com/item.htm?id=567031408478&ns=1&abbucket=0#detail', 'nid': '567031408478'}, {'url': '//item.taobao.com/item.htm?id=562662340912&ns=1&abbucket=0#detail', 'nid': '562662340912'}, {'url': '//item.taobao.com/item.htm?id=562437301433&ns=1&abbucket=0#detail', 'nid': '562437301433'}, {'url': '//item.taobao.com/item.htm?id=534775097458&ns=1&abbucket=0#detail', 'nid': '534775097458'}, {'url': '//item.taobao.com/item.htm?id=538680637071&ns=1&abbucket=0#detail', 'nid': '538680637071'}, {'url': '//item.taobao.com/item.htm?id=562617371768&ns=1&abbucket=0#detail', 'nid': '562617371768'}, {'url': '//item.taobao.com/item.htm?id=559604412085&ns=1&abbucket=0#detail', 'nid': '559604412085'}, {'url': '//item.taobao.com/item.htm?id=557655146482&ns=1&abbucket=0#detail', 'nid': '557655146482'}, {'url': '//item.taobao.com/item.htm?id=557313976301&ns=1&abbucket=0#detail', 'nid': '557313976301'}, {'url': '//item.taobao.com/item.htm?id=535798856261&ns=1&abbucket=0#detail', 'nid': '535798856261'}, {'url': '//item.taobao.com/item.htm?id=564542533055&ns=1&abbucket=0#detail', 'nid': '564542533055'}, {'url': '//item.taobao.com/item.htm?id=560490077821&ns=1&abbucket=0#detail', 'nid': '560490077821'}, {'url': '//item.taobao.com/item.htm?id=545729379236&ns=1&abbucket=0#detail', 'nid': '545729379236'}, {'url': '//item.taobao.com/item.htm?id=539017029659&ns=1&abbucket=0#detail', 'nid': '539017029659'}, {'url': '//item.taobao.com/item.htm?id=548979287053&ns=1&abbucket=0#detail', 'nid': '548979287053'}, {'url': '//item.taobao.com/item.htm?id=547306123063&ns=1&abbucket=0#detail', 'nid': '547306123063'}, {'url': '//item.taobao.com/item.htm?id=560401081811&ns=1&abbucket=0#detail', 'nid': '560401081811'}, {'url': '//item.taobao.com/item.htm?id=559238826160&ns=1&abbucket=0#detail', 'nid': '559238826160'}, {'url': '//item.taobao.com/item.htm?id=548005655930&ns=1&abbucket=0#detail', 'nid': '548005655930'}, {'url': '//item.taobao.com/item.htm?id=566283789517&ns=1&abbucket=0#detail', 'nid': '566283789517'}, {'url': '//item.taobao.com/item.htm?id=44099699478&ns=1&abbucket=0#detail', 'nid': '44099699478'}, {'url': '//item.taobao.com/item.htm?id=544161171595&ns=1&abbucket=0#detail', 'nid': '544161171595'}, {'url': '//item.taobao.com/item.htm?id=559188661190&ns=1&abbucket=0#detail', 'nid': '559188661190'}, {'url': '//item.taobao.com/item.htm?id=542147668751&ns=1&abbucket=0#detail', 'nid': '542147668751'}, {'url': '//item.taobao.com/item.htm?id=550783952943&ns=1&abbucket=0#detail', 'nid': '550783952943'}, {'url': '//item.taobao.com/item.htm?id=546783312007&ns=1&abbucket=0#detail', 'nid': '546783312007'}, {'url': '//item.taobao.com/item.htm?id=561765387837&ns=1&abbucket=0#detail', 'nid': '561765387837'}, {'url': '//item.taobao.com/item.htm?id=561697998655&ns=1&abbucket=0#detail', 'nid': '561697998655'}, {'url': '//item.taobao.com/item.htm?id=521546061835&ns=1&abbucket=0#detail', 'nid': '521546061835'}, {'url': '//item.taobao.com/item.htm?id=40034000797&ns=1&abbucket=0#detail', 'nid': '40034000797'}, {'url': '//item.taobao.com/item.htm?id=553114728523&ns=1&abbucket=0#detail', 'nid': '553114728523'}, {'url': '//item.taobao.com/item.htm?id=531170306861&ns=1&abbucket=0#detail', 'nid': '531170306861'}, {'url': '//item.taobao.com/item.htm?id=556219226249&ns=1&abbucket=0#detail', 'nid': '556219226249'}, {'url': '//item.taobao.com/item.htm?id=556097568745&ns=1&abbucket=0#detail', 'nid': '556097568745'}, {'url': '//item.taobao.com/item.htm?id=554090593383&ns=1&abbucket=0#detail', 'nid': '554090593383'}, {'url': '//item.taobao.com/item.htm?id=524998694417&ns=1&abbucket=0#detail', 'nid': '524998694417'}, {'url': '//item.taobao.com/item.htm?id=550479251026&ns=1&abbucket=0#detail', 'nid': '550479251026'}, {'url': '//item.taobao.com/item.htm?id=520037295396&ns=1&abbucket=0#detail', 'nid': '520037295396'}, {'url': '//item.taobao.com/item.htm?id=562492282176&ns=1&abbucket=0#detail', 'nid': '562492282176'}, {'url': '//item.taobao.com/item.htm?id=555550246645&ns=1&abbucket=0#detail', 'nid': '555550246645'}, {'url': '//item.taobao.com/item.htm?id=530285355786&ns=1&abbucket=0#detail', 'nid': '530285355786'}, {'url': '//item.taobao.com/item.htm?id=563105179293&ns=1&abbucket=0#detail', 'nid': '563105179293'}, {'url': '//item.taobao.com/item.htm?id=564244828958&ns=1&abbucket=0#detail', 'nid': '564244828958'}, {'url': '//item.taobao.com/item.htm?id=523779327955&ns=1&abbucket=0#detail', 'nid': '523779327955'}], 'task_nums': '50'})
    # print(data)
    # print('cost, ',now() - start)
    # testTaobaoItemdetail_pressure()

    # from Master.Task.TaskManager import TaskManager as tk
    # m_tm = tk()
    # tasks = m_tm.get_task({'': ''})
    # print(tasks)