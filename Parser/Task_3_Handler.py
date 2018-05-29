#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/9 15:15
# @Author  : HT
# @Site    : 
# @File    : Task_3_Handler.py
# @Software: PyCharm Community Edition
# @Describe: Desc
# @Issues  : Issues

import functools
import re
from BaseModule.HTMLParser import HTMLParser as hp
from BaseModule.HTTPRequest import user_agent
import asyncio

def config_call_back(config_list, task_info, nid, url, fn):
    result = fn.result()
    result = result.decode(encoding='gb18030')

    parser_data = hp.parser(content=result, task_info=task_info)
    data = {
        'data': parser_data,
        'nid': nid,
        '_id': nid,
        'url': url
    }
    config_list.append(data)



def get_other_info_task(config, session):
    def call_back(key, fn):
        result = fn.result()
        result = result.decode(encoding='gb18030')
        config['data'][key] = result

    descUrl = config.get('data').get('descUrl')
    sibUrl = config.get('data').get('sibUrl')
    counterApi = config.get('data').get('counterApi')
    rateCounterApi = config.get('data').get('rateCounterApi')




    nid = config.get('nid')
    headers = {
        'cache-control': "no-cache",
        # 'Cookie': "enc=LbDhv2gVz58iGzjeNvtg0fU9IybnoGvjQHE2B/19d9Qy0xExqp8kQIc0glRxRLs9O+Dcm4D41l0T/azCrIu0iQ==",
        'Referer': "https://item.taobao.com/",
        'User-Agent': user_agent(),
    }
    c_headers = {
        'cache-control': "no-cache",
        'Cookie': "enc=LbDhv2gVz58iGzjeNvtg0fU9IybnoGvjQHE2B/19d9Qy0xExqp8kQIc0glRxRLs9O+Dcm4D41l0T/azCrIu0iQ==",
        'Referer': "https://item.taobao.com/",
        'User-Agent': user_agent(),
    }
    task_list = list()

    if descUrl == '':
        pass
    else:
        try:
            descUrl = re.findall(u"(//.*)'\s", descUrl)[0]
            descUrl = 'http:' + descUrl

            task = asyncio.ensure_future(session.get_url(url=descUrl, headers=headers))
            task.add_done_callback(functools.partial(call_back, 'desc_content'))
            task_list.append(task)
        except Exception as error:
            print('getdescUrl error:{}'.format(error))

    if sibUrl == '':
        pass
    else:
        # print(sibUrl)
        sibUrl = 'https:' + sibUrl +  '&callback=onSibRequestSuccess'
        task = asyncio.ensure_future(session.get_url(url=sibUrl, headers=headers))
        task.add_done_callback(functools.partial(call_back, 'sib_content'))
        task_list.append(task)

    if counterApi == '':
        pass
    else:
        # print(counterApi)

        counterApi = 'https:' + counterApi + '&callback=jsonp144'
        task = asyncio.ensure_future(session.get_url(url=counterApi, headers=headers))
        task.add_done_callback(functools.partial(call_back, 'counter_content'))
        task_list.append(task)

    if rateCounterApi == '':
        pass
    else:
        # print(rateCounterApi)
        rateCounterApi = 'https:' + rateCounterApi
        task = asyncio.ensure_future(session.get_url(url=rateCounterApi, headers=headers))
        task.add_done_callback(functools.partial(call_back, 'rate_content'))
        task_list.append(task)

    return task_list
    # loop.run_until_complete(asyncio.wait(task_list))

if __name__ == '__main__':
    info = "location.protocol==='http:' ? '//dsc.taobaocdn.com/i7/560/301/560308936365/TB1Sb.fXFkoBKNjSZFE8qvrEVla.desc%7Cvar%5Edesc%3Bsign%5E2c641960957aac7c3ef991ea5b774075%3Blang%5Egbk%3Bt%5E1519732615' : '//desc.alicdn.com/i7/560/301/560308936365/TB1Sb.fXFkoBKNjSZFE8qvrEVla.desc%7Cvar%5Edesc%3Bsign%5E2c641960957aac7c3ef991ea5b774075%3Blang%5Egbk%3Bt%5E1519732615"
    print(re.findall(u"(//.*)'\s", info))
    r = {'r':'r'}
    print(id(r))
    d = r
    print(id(d))
    print(id(r.copy()))