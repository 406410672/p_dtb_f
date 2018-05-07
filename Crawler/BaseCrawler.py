#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/21 13:50
# @Author  : HT
# @Site    : 
# @File    : BaseCrawler.py
# @Software: PyCharm Community Edition
# @Describe: Desc
# @Issues  : Issues
import json
import os
import signal
import sys
import time
from threading import Thread

RootPWD = os.path.join(os.path.split(os.path.abspath(__file__))[0],os.pardir)
sys.path.append(RootPWD)
from Socket import SocketProtocol as pc
from Socket.SocketClient import HTSocketClient
from BaseModule.Configloader import Configloader
from BaseModule.HTLogger import HTLogger
from BaseModule.DateProcessing import *

class BaseCrawler(HTLogger):
    def __init__(self, name):
        HTLogger.__init__(self, name)
        self.configLoader = Configloader()
        self.socketClient = HTSocketClient(ip=self.configLoader.master_host,
                                           port=self.configLoader.master_port)
        self.server_status = None
        self.clientId = None
        self.clientname = name
        # self.logger = HTLogger(name)

        def crawlerSignal():
            signal.signal(signal.SIGTERM, self.shutDownCrawler)
            signal.signal(signal.SIGINT, self.shutDownCrawler)
        crawlerSignal()


    def register(self):
        request = {
            pc.MSG_TYPE : pc.REGISTER ,
            pc.CLIENT_NAME : self.clientname
                   }
        response = self.socketClient.send(json.dumps(request))
        response = json.loads(response)
        self.logger.debug(response)
        self.server_status = response[pc.SERVER_STATUS]
        self.clientId = response[pc.CLIENT_ID]

    def actionCrawler(self):
        '''
        注册ClientID 并且启动心跳
        子类继承之后 需要调用
        :return:
        '''
        self.register()

        thread = Thread(target=self.heartBeat, name='heartBeat')
        thread.setDaemon(True)
        thread.start()

    def shutDownCrawler(self, a, b):
        request = {
            pc.MSG_TYPE : pc.UNREGISTER ,
            pc.CLIENT_ID : self.clientId
        }
        # 请求shutdown client
        self.socketClient.send(json.dumps(request))
        self.logger.error('shutdown client')
        exit(0)

    def heartBeat(self):
        while True:
            try:
                request = {
                    pc.MSG_TYPE: pc.HEARTBEAT,
                    pc.CLIENT_ID: self.clientId
                }
                response = self.socketClient.send(json.dumps(request))
                response = json.loads(response)

                error = response.get(pc.ERROR)
                if error != None:
                    if error == pc.ERR_NOT_FOUND:
                        # 重新注册
                        pass
                acction = response.get('ACTION_REQUIRED')
                if acction:
                    if acction == pc.RESUMED:
                        request = {
                            pc.MSG_TYPE: pc.RESUMED,
                            pc.CLIENT_ID: self.clientId
                        }
                        # 请求重启client
                        self.socketClient.send(json.loads(request))
                time.sleep(5)
            except Exception as error:
                self.logger.error('heartBeat error:{}',error)
                request = {
                    pc.CLIENT_ID : self.clientId,
                    pc.MSG_TYPE : pc.UNREGISTER
                }
                response = self.socketClient.send(json.dumps(request))
                self.logger.debug(response)


# if __name__ == '__main__':
#     basecrawler = BaseCrawler('测试5')
#     basecrawler.actionCrawler()
if __name__ == '__main__':
    am = BaseCrawler('d')
    from multiprocessing import Process

    process = Process(target=am.actionCrawler)
    process.start()
    process.join()