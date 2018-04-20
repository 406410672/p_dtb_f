#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/19 15:21
# @Author  : HT
# @Site    : 
# @File    : SocketServer.py
# @Software: PyCharm Community Edition
# @Describe: Desc
# @Issues  : Issues
try:
    import platform

    if platform.python_version()[0] == 2:
        import sys

        reload(sys)
        sys.setdefaultencoding('utf8')
except Exception as error:
    print('setdefaultencoding error:{}'.format(error))


import sys,os
import socket

from threading import Thread

class HTSocketServer(object):
    def __init__(self, callback, ip, port):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.callback = callback
        try:
            self.socket.bind((ip, port))
        except Exception as error:
            print('bind ip error',error)
        self.socket.listen(10)


    def startListening(self):
        while True:
            cnn,address = self.socket.accept()
            # self.processingConnection(cnn)
            thread = Thread(target=self.processingConnection, args=(cnn,), name='processingConnection')
            thread.setDaemon(True)
            thread.start()


    def processingConnection(self, cnn):
        content = str()

        while True:
            recv = cnn.recv(1)
            recv = str(recv, encoding='utf-8')
            if  '\0' in recv:
                break
            content += recv
        ask = self.callback(content)
        ask = ask + '\0'
        cnn.sendall(bytes(ask, encoding='utf-8'))
        cnn.close()
        # try:
        #     while True:
        #         recv = cnn.recv(100)
        #         recv = str(recv, encoding='utf-8')
        #         if  '\0' in recv:
        #             break
        #         content += recv
        #     print(content)
        #     ask = self.callback(content)
        #     cnn.sendall(ask)
        #     cnn.close()
        # except Exception as error:
        #     print('processing Connection error:{}'.format(error))

    def start(self):
        thread = Thread(target=self.startListening, name='startListening')
        thread.setDaemon(True)
        thread.start()


def callback(mesesage):
    print(mesesage)
    return 'ask'

if __name__ == '__main__':
    socket = HTSocketServer(callback=callback, ip='localhost',port=20050)
    socket.start()
