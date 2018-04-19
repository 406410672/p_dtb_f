#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/19 15:24
# @Author  : HT
# @Site    : 
# @File    : SocketClient.py
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


import sys
import socket


class HTSocketClient(object):
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port

    def send(self,message):
        '''
        :param message:
        :return:
        '''
        message = message + '\0'
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((self.ip, self.port))
        s.sendall(bytes(message, encoding='utf-8'))
        response = s.recv(1024 * 8)
        s.close()
        return response



if __name__ == '__main__':
    htS = HTSocketClient(ip='192.168.62.112', port=20050)
    content = '''
    sk = socket.socket()
    sk.connect(("127.0.0.1", 8888))  # 主动初始化与服务器端的连接
    while True:
        send_data = input("输入发送内容:")
        sk.sendall(bytes(send_data, encoding="utf8"))
        if send_data == "byebye":
            break
        accept_data = str(sk.recv(1024), encoding="utf8")
        print("".join(("接收内容：", accept_data)))
    sk.close()0'''
    bytes()
    response = htS.send()
    print(response)