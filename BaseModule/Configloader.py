# -*- coding:utf-8 -*-
import sys
import os

try:
    from configparser import ConfigParser  # py3
except:
    from ConfigParser import ConfigParser  # py2
from BaseModule.Class import *

class Configloader():
    def __init__(self):
        pwd = os.path.split(os.path.abspath(__file__))[0]
        config_path = os.path.join(pwd,'Config.ini')
        self.config_file = ConfigParser()
        self.config_file.read(config_path)
    '''
    const
    '''

    @LazyProperty
    def account_expiretime(self):
        return int(self.config_file.get('Const','account_expiretime'))

    '''
    redis
    '''
    @LazyProperty
    def redis_host(self):
        return self.config_file.get('Server', 'redis_host')

    @LazyProperty
    def redis_port(self):
        return int(self.config_file.get('Server', 'redis_port'))

    @LazyProperty
    def redis_db(self):
        return int(self.config_file.get('Server', 'redis_db'))

    '''
    sqlserver
    '''
    @LazyProperty
    def sqlserver_host(self):
        return self.config_file.get('Server', 'sqlserver_host')

    @LazyProperty
    def sqlserver_db(self):
        return self.config_file.get('Server', 'sqlserver_db')

    @LazyProperty
    def sqlserver_user(self):
        return self.config_file.get('Server', 'sqlserver_user')

    @LazyProperty
    def sqlserver_pwd(self):
        return self.config_file.get('Server', 'sqlserver_pwd')

    '''
    mongodb
    '''
    @LazyProperty
    def mongodb_host(self):
        return self.config_file.get('Server', 'mongodb_host')

    @LazyProperty
    def mongodb_port(self):
        return int(self.config_file.get('Server', 'mongodb_port'))

    @LazyProperty
    def mongodb_user(self):
        return self.config_file.get('Server', 'mongodb_user')

    @LazyProperty
    def mongodb_password(self):
        return self.config_file.get('Server', 'mongodb_password')

    '''
    distributed Master
    '''
    @LazyProperty
    def master_host(self):
        return self.config_file.get('Server', 'master_host')

    @LazyProperty
    def master_port(self):
        return self.config_file.getint('Server', 'master_port')

if __name__ == '__main__':

    c = Configloader()
    print(c.sqlserver_pwd)
    print(c.mongodb_password)
    print(c.mongodb_user)
    print(c.master_host)