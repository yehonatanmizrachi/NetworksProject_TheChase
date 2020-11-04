from Player import *
from Chaser import *
import time

class Client:
    def __init__(self, socket, address):
        ########################################
        # socket settings
        self.socket = socket
        self.address = address
        self.msg_size = 1024
        self.format = 'utf-8'
        ########################################
        self.player = Player()
        self.chaser = Chaser()

    def send_msg(self, msg):
        self.socket.send(msg.encode(self.format))
        # wait 0.1 sec so that each message will be sent separately
        time.sleep(0.1)

    def receive_msg(self):
        return self.socket.recv(self.msg_size).decode(self.format)
