import socket

HEADER = 1024
PORT = 5050
FORMAT = 'utf-8'
SERVER_IP = "10.0.0.8"
ADDR = (SERVER_IP, PORT)


class Client:
    def __init__(self):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.connect(ADDR)
        self.disconnect_message = "!DISCONNECT"

    def send(self, msg):
        msg = str(msg)
        self.server.send(msg.encode(FORMAT))

    def get_msg(self):
        msg = self.server.recv(HEADER).decode(FORMAT)
        print(msg)
        return msg

    # close socket and exit game
    def close(self):
        self.server.close()
