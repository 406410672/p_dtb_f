#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/19 16:22
# @Author  : HT
# @Site    : 
# @File    : Matser.py
# @Software: PyCharm Community Edition
# @Describe: Desc
# @Issues  : Issues

import os
import json
import time
RootPWD = os.path.join(os.path.split(os.path.abspath(__file__))[0],os.pardir)

from BaseModule.HTLogger import HTLogger
from BaseModule.Configloader import Configloader
from Socket.SocketServer import HTSocketServer
from Socket import SocketProtocol as pc
from BaseModule import DateProcessing as dp
from Master.Task.TaskManager import TaskManager
CLIENT_LOST_TIME = 60 * 10
class Master(object):
    def __init__(self):
        self.configLoader = Configloader()
        self.socketServer = HTSocketServer(callback=self.on_message,
                                           ip=self.configLoader.master_host,
                                           port=self.configLoader.master_port)
        self.logger = HTLogger('master.log')
        self.task_manager = TaskManager()
        self.clients = dict()
        self.server_status = pc.SERVER_RUNNING

        self.socketServer.start()

    def get_clientid(self):
        i = 0
        for key in self.clients.keys():
            if i < int(key):
                i = int(key)
        i += 1
        return str(i)

    def on_message(self, message):
        '''
        :param message:
        :return:
        '''
        request_obj = json.loads(message)
        response = dict()
        response[pc.SERVER_STATUS] = self.server_status
        request_type = request_obj[pc.MSG_TYPE]
        self.logger.debug('recive a request type:{}  message len:{}'.format(request_type,len(message)))
        # 注册
        if request_type == pc.REGISTER:
            clientid = self.get_clientid()
            clientName = request_obj[pc.CLIENT_NAME]
            client = {
                'time': time.time(),
                'status': pc.SERVER_RUNNING,
                'name': clientName
            }
            self.clients[clientid] = client
            response[pc.CLIENT_ID] = clientid
            return json.dumps(response)

        clientid = str(request_obj.get(pc.CLIENT_ID))
        response = dict()
        response[pc.SERVER_STATUS] = self.server_status



        if clientid is None or self.clients.get(clientid) is None:
            response[pc.ERROR] = pc.ERR_NOT_FOUND
            return json.dumps(response)
        elif self.clients.get(clientid).get('status') == pc.ERROR_CONNECTION_LOST:
            response[pc.ACTION_REQUIRED] = pc.RESUME_REQUIRED
            return json.dumps(response)

        # 注销
        if request_type == pc.UNREGISTER:
            del self.clients[clientid]
            return json.dumps(response)
        # 心跳
        elif request_type == pc.HEARTBEAT:
            self.clients[clientid]['time'] = time.time()
            return json.dumps(response)
        # 申请任务
        elif request_type == pc.APPLICATION_TASKS:
            app_tasks_response = self.get_task_opration(request_obj=request_obj)
            if app_tasks_response is None:
                pass
            else:
                response.update(app_tasks_response)
            return json.dumps(response)
        # 上传任务
        elif request_type == pc.UPLOAD_TASKS:
            upload_task_response = self.upload_task_operation(request_obj=request_obj)
            response.update(upload_task_response)
            return json.dumps(response)
        else:
            return json.dumps(response)

    def get_task_opration(self, request_obj):
        response = self.task_manager.get_task(request_obj)
        return response

    def upload_task_operation(self, request_obj):
        response = self.task_manager.upload_task(request_obj)
        return response

    def period_check(self):
        while True:
            clientlens = self.clients.__len__()
            if clientlens == 0:
                log = 'not any crawler'
            else:
                log = '\n----------当前一共有{}个CrawlerClient --------------\n'.format(clientlens)
                for clientId, client in self.clients.items():
                    clientStatus = self.clients[clientId]['status']
                    clientTime = client['time']
                    clientName = client['name']
                    log += 'clientId:{} clientName:{}    \nclientStatus:{}     lastHeartbeattime:{} \n'.format(clientId,
                                                                                                               clientName,
                                                                                                               clientStatus,
                                                                                                               dp.time_stamp_to_time(
                                                                                                                   clientTime))
                    if time.time() - clientTime >= CLIENT_LOST_TIME:
                        self.clients[clientId]['status'] = pc.ERROR_CONNECTION_LOST
                    else:
                        continue
                log += '---------------------------------------------\n'

            self.logger.debug(log)
            time.sleep(30)


def run():
    master = Master()
    master.period_check()
    # try:
    #     scheduler = BlockingScheduler()
    #     scheduler.add_job(master.period_check, 'interval', seconds = 10)
    #     scheduler.start()
    # except Exception,error:
    #     print 'create BlockingScheduler error:',error

if __name__ == '__main__':
    run()