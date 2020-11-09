import socket
import threading
from Client import *
from GameLogic import *


class GameManager:
    def __init__(self):
        ########################################
        # socket settings
        self.__port = 5050
        self.__ip = socket.gethostname()
        self.__address = (self.__ip, self.__port)
        # count how many active clients there is
        self.__active_clients = 0
        # the size of the msg in bytes.
        self.__msg_size = 1024
        self.__format = 'utf-8'
        self.__disconnect_message = "!DISCONNECT"
        self.__max_active_client = 3
        # server socket
        # AF_INET -> address family IPV4, SOCK_STREAM -> protocol TCP
        self.__socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.__socket.bind(self.__address)
        ########################################

    # start listening to requests(a thread that always runs in the background)
    # and open a new thread for each client
    def get_new_clients(self):
        print("server is listening...")
        self.__socket.listen()
        while True:
            # wait for a new connection
            client_socket, client_address = self.__socket.accept()
            if self.__active_clients < self.__max_active_client:
                # start a new thread for the client and start the game
                new_client = Client(client_socket, client_address)
                thread = threading.Thread(target=self.handle_client, args=(new_client,))
                thread.start()
                self.__active_clients += 1
                print(f"active connections: {self.__active_clients}")
            else:
                print("server is full. request denied!")
                client_socket.send("Server is full. Please try again later.".encode(self.__format))
                client_socket.close()

    def handle_client(self, client):
        GameLogic.part0(client)
        # assuming that the game ended
        client.socket.close()
        self.__active_clients -= 1


my_manager = GameManager()
my_manager.get_new_clients()
