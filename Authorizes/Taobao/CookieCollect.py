#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/17 11:04
# @Author  : HT
# @Site    : 
# @File    : CookieCollect.py
# @Software: PyCharm Community Edition
# @Describe: Desc
# @Issues  : Issues

import redis
import time
import re

from BaseModule.WebDriverManager import WebDriverManager


ISG_SET = 'isg_set'

class CookieCollect():
    driverManger = WebDriverManager()
    redis_client = redis.StrictRedis(host='192.168.6.38', db=15)

    def collect_isg(self, num=100):
        url = 'https://item.taobao.com/item.htm?id=560707511941'
        driver = self.driverManger.getFreeDriver()
        js_filer = open('Anti-js.js', encoding='utf-8')
        js_content = js_filer.read()
        driver.get(url)
        isg_list = []
        count = 0
        while True:
            try:
                isg = driver.execute_script(js_content)
                driver.delete_all_cookies()
                isg_list.append(isg)
                time.sleep(0)
                count += 1
                if count >= num:
                    break
            except Exception as error:
                print('error:{}'.format(error))
                driver.close()
                break
        try:
            driver.close()
        except Exception as error:
            print('close fail:{}'.format(error))
        return isg_list

    def get_isg(self):
        isg_cookie = self.redis_client.spop(ISG_SET)
        isg_cookie = isg_cookie.decode('utf-8')
        isg_value = re.match(u'^isg=(\S*);', isg_cookie).groups()[0]
        # isg_value = re.match(u'^isg=(.*?);', isg_cookie).groups()[0]
        return isg_value

if __name__ == '__main__':
    col = CookieCollect()
    #收集isg
    # isg_list = collect_isg(1000)
    # redis_client.sadd(ISG_SET, *isg_list)

    #取出isg
    isg = col.get_isg()
    print(isg)
