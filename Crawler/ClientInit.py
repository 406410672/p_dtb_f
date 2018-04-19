
from Socket.SocketClient import HTSocketClient
from Socket.SocketProtocol import *
from BaseModule.Configloader import Configloader
from BaseModule.DateProcessing import *
import json


class ClientInit():
    def __init__(self):
        self.loader = Configloader()
        self.socket = HTSocketClient(ip=self.loader.master_host, port=self.loader.master_port)
        self.client_id = ''

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


if __name__ == '__main__':
    cilent = ClientInit()
    cilent.registered()
