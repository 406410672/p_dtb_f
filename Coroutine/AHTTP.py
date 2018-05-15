#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/8 18:24
# @Author  : HT
# @Site    : 
# @File    : AHTTP.py
# @Software: PyCharm Community Edition
# @Describe: Desc
# @Issues  : Issues

import aiohttp
import asyncio
from BaseModule.HTTPRequest import getHeader


class SessionManager():
    session = None

    async def get_session(self):
        if self.session == None:
            conn = aiohttp.TCPConnector(ttl_dns_cache=60 * 60, limit=150)
            session = aiohttp.ClientSession(connector=conn)
            self.session = session
            return session
        else:
            return self.session


    async def get_url(self, url, headers=getHeader()):
        session = await self.get_session()
        # print('准备请求的url:{}'.format(url))
        async with session.get(url, headers=headers) as response:
            return (await response.read())


    # def flush_session(self):
    #     self.session.close()


def test1():
    async def get_tasks():
        s = SessionManager()
        tasks = [asyncio.ensure_future(s.get_url('https://www.baidu.com')) for i in range(10)]
        return await asyncio.wait(tasks)


    loop = asyncio.get_event_loop()
    results = loop.run_until_complete(get_tasks())
    loop.close()

    # print(tasks)
    print(results)

def text2():
    now = lambda :time.time()
    from threading import Thread
    def start_loop(loop):
        asyncio.set_event_loop(loop)
        loop.run_forever()

    def more_work(x):
        print('More work {}'.format(x))
        time.sleep(x)
        print('Finished more work {}'.format(x))
    start = now()
    new_loop = asyncio.new_event_loop()
    t = Thread(target=start_loop, args=(new_loop,))
    t.start()
    print('TIME: {}'.format(time.time() - start))
    new_loop.call_soon_threadsafe(more_work, 6)
    new_loop.call_soon_threadsafe(more_work, 3)

if __name__ == '__main__':
    test1()
    # import time
    # import functools
    # start = time.time()
    # loop = asyncio.get_event_loop()
    # s = SessionManager()
    # tasks = [asyncio.ensure_future(s.get_url('https://www.baidu.com')) for i in range(10)]
    # i = 0
    # loop.run_until_complete( asyncio.wait(tasks))
    # print(len(tasks))
    # s.session.close()
    # loop.stop()
    # loop.close()
    # # print(task)
    # print('cost : ',time.time()-start)
