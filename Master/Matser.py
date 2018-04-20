#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/19 16:22
# @Author  : HT
# @Site    : 
# @File    : Matser.py
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

import os
import json
import time
RootPWD = os.path.join(os.path.split(os.path.abspath(__file__))[0],os.pardir)

from BaseModule.HTLogger import HTLogger
from BaseModule.Configloader import Configloader
from Socket.SocketServer import HTSocketServer
from Socket import SocketProtocol as pc
from BaseModule import DateProcessing as dp

CLIENT_LOST_TIME = 60 * 10
class Master(object):
    def __init__(self):
        self.configLoader = Configloader()
        self.socketServer = HTSocketServer(callback=self.onMessage,
                                           ip=self.configLoader.master_host,
                                           port=self.configLoader.master_port)
        self.logger = HTLogger('master.log')
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

    def onMessage(self, message):
        '''
        :param message:
        :return:
        '''
        self.logger.error(message)
        request_obj = json.loads(message)
        response = dict()
        response[pc.SERVER_STATUS] = self.server_status
        if request_obj[pc.MSG_TYPE] == pc.REGISTER:
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

        clientid = request_obj.get(pc.CLIENT_ID)
        response = dict()
        if clientid is None:
            response[pc.ERROR] = pc.ERR_NOT_FOUND
            return json.dumps(response)
        elif self.clients[clientid]['status'] == pc.ERROR_CONNECTION_LOST:
            response[pc.ACTION_REQUIRED] = pc.RESUME_REQUIRED
            return response

        #注销
        if request_obj[pc.MSG_TYPE] == pc.UNREGISTER:
            # self.clients.remove(clientId)
            del self.clients[clientid]
            return json.dumps(response)
        #心跳
        elif request_obj[pc.MSG_TYPE] == pc.HEARTBEAT:
            self.clients[clientid]['time'] = time.time()
            return json.dumps(response)
        elif request_obj[pc.MSG_TYPE] == pc.Application_Tasks
        else :
            return json.dumps(response)



    def period_check(self):
        while True:
            log = str()
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