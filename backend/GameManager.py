import socket
import threading
from Client import *
from GameLogic import *


class GameManager:
    def __init__(self):
        ########################################
        # socket settings
        self.port = 5050
        self.ip = "192.168.100.6"
        self.address = (self.ip, self.port)
        # count how many active clients there is
        self.active_clients = 0
        # the size of the msg in bytes.
        self.msg_size = 1024
        self.format = 'utf-8'
        self.disconnect_message = "!DISCONNECT"
        self.max_active_client = 3
        # server socket
        # AF_INET -> address family IPV4, SOCK_STREAM -> protocol TCP
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind(self.address)
        ########################################

    # start listening to requests(a thread that always runs in the background)
    # and open a new thread for each client
    def get_new_clients(self):
        print("server is listening...")
        self.socket.listen()
        while True:
            # wait for a new connection
            client_socket, client_address = self.socket.accept()
            if self.active_clients < self.max_active_client:
                # start a new thread for the client and start the game
                new_client = Client(client_socket, client_address)
                thread = threading.Thread(target=GameLogic.start_part0, args=(new_client,))
                thread.start()
                self.active_clients += 1
                print(f"active connections: {self.active_clients}")
            else:
                print("server is full. request denied!")
                client_socket.send("Server is full. Please try again later.".encode(self.format))
                client_socket.close()


my_manager = GameManager()
my_manager.get_new_clients()
