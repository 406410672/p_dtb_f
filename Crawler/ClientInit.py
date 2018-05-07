
from Socket.SocketClient import HTSocketClient
from Socket.SocketProtocol import *
from BaseModule.Configloader import Configloader
from BaseModule.HTLogger import HTLogger
from BaseModule.DateProcessing import *
from BaseModule import HTTPRequest as http
from Master.Task import Const as C
from BaseModule.HTMLParser import HTMLParser as hp
import json
from Crawler.Task.TaskManager import TaskManager as TM
class ClientInit():
    def __init__(self):
        self.loader = Configloader()
        self.socket = HTSocketClient(ip=self.loader.master_host, port=self.loader.master_port)
        self.client_id = ''
        self.taskManager = TM()
        self.logger = HTLogger('crawl_client.log')

    def registered(self):
        time = datetime_to_timestamp(get_datestr())
        parm = {MSG_TYPE: REGISTER, CLIENT_NAME: '12', REQUEST_TIME: time}
        response = self.socket.send(json.dumps(parm))
        d = json.loads(response)
        print(d)

    def heartbeat(self):
        time = datetime_to_timestamp(get_datestr())
        parm = {MSG_TYPE: HEARTBEAT, CLIENT_ID: self.client_id, REQUEST_TIME: time}
        response = self.socket.send(json.dumps(parm))
        d = json.loads(response)
        print(d)

    def application_task(self):
        time = datetime_to_timestamp(get_datestr())
        parm = {MSG_TYPE: APPLICATION_TASKS, CLIENT_ID: 6, REQUEST_TIME: time}
        response = self.socket.send(json.dumps(parm))
        response_dict = json.loads(response)
        error = response_dict.get(ERROR)
        if error :
            self.logger.error('application task error:%s'%(response_dict))
        else:
            self.processing_task(response_dict)

    def processing_task(self, task_response):

        self.taskManager.download_task(task_response)
        # parse_rule = task_response[PARSE_RULE]
        # storage_rule = task_response[STORAGE_RULE]
        # items = task_response['items']
        # task_id = task_response['task_id']
        # domain = task_response['domain']
        #
        # crawl_obj = list()
        # for item in items:
        #     url = item['url']
        #     item_response = http.get(url=url)
        #     crawl_obj.append(item_response.content)
        #
        # for content in crawl_obj:
        #     data = hp.parser(content=content, task_info=task_response)
        #     print(data)



if __name__ == '__main__':
    cilent = ClientInit()
    cilent.registered()
    # time.sleep(2)
    print(cilent.application_task())
