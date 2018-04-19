# -*- coding:utf-8 -*-
import sys
import os

import configparser


class Configloader():

    def __init__(self):
        pwd = os.path.split(os.path.abspath(__file__))[0]
        config_path = os.path.join(pwd,'Config.ini')
        self.config_file = configparser.ConfigParser()
        self.config_file.read(config_path)
    '''
    const
    '''
    def account_expiretime(self):
        return int(self.config_file.get('Const','account_expiretime'))

    '''
    redis
    '''
    def redis_host(self):
        return self.config_file.get('Server', 'redis_host')

    def redis_port(self):
        return int(self.config_file.get('Server', 'redis_port'))

    def redis_db(self):
        return int(self.config_file.get('Server', 'redis_db'))

    '''
    sqlserver
    '''
    def sqlserver_host(self):
        return self.config_file.get('Server', 'sqlserver_host')

    def sqlserver_db(self):
        return self.config_file.get('Server', 'sqlserver_db')

    def sqlserver_user(self):
        return self.config_file.get('Server', 'sqlserver_user')

    def sqlserver_pwd(self):
        return self.config_file.get('Server', 'sqlserver_pwd')

    '''
    mongodb
    '''
    def mongodb_host(self):
        return self.config_file.get('Server', 'mongodb_host')

    def mongodb_port(self):
        return int(self.config_file.get('Server', 'mongodb_port'))

    def mongodb_user(self):
        return self.config_file.get('Server', 'mongodb_user')

    def mongodb_password(self):
        return self.config_file.get('Server', 'mongodb_password')

    '''
    distributed Master
    '''
    def master_host(self):
        return self.config_file.get('Server', 'master_host')

    def master_port(self):
        return self.config_file.getint('Server', 'master_port')

if __name__ == '__main__':

    c = Configloader()
    print(c.sqlserver_pwd())
    print(c.mongodb_password())
    print(c.mongodb_user())