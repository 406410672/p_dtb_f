#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/19 14:23
# @Author  : HT
# @Site    : 
# @File    : HTLogger.py
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



import logging
import os
from logging.handlers import TimedRotatingFileHandler


ROOT_PWD = os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir)

class HTLogger(logging.Logger):
    def __init__(self, name, level=logging.DEBUG,
                 StreamHandler = True,
                 FileHandler = True,
                 formatter = '%(asctime)s - %(name)s - %(levelname)s - line:%(lineno)d - %(message)s'):
        #基类的结构函数需要手动调用
        logging.Logger.__init__(self, name = name, level=level)
        self.name = name
        self.formatter = formatter
        if StreamHandler == True:
            self.__SetStreamHandler()
        if FileHandler == True:
            self.__SetFileHandler()

    def __SetStreamHandler(self):
        handler = logging.StreamHandler()
        handler.set_name(self.name)
        formatter = logging.Formatter(self.formatter)
        handler.setFormatter(formatter)
        self.addHandler(handler)

    def __SetFileHandler(self):
        logPwd = os.path.join(ROOT_PWD, 'log')
        logFilePath = os.path.join(logPwd, '{}'.format(self.name))
        if os.path.exists(logPwd) == False:
            os.mkdir(logPwd)
        handler = TimedRotatingFileHandler(filename = logFilePath,
                                           when='D',
                                           interval=1,
                                           backupCount=5,
                                           )
        formatter = logging.Formatter(self.formatter)
        handler.setFormatter(formatter)
        handler.suffix = '%Y-%m-%d.log'
        self.addHandler(handler)

if __name__ == '__main__':
    logger = HTLogger('test')
    logger.error('info')