import socket
import threading


class Server:
    def __init__(self, ip, port):
        self.port = port
        self.ip = ip
        self.address = (self.ip, self.port)
        # count how many active clients there is
        self.active_clients = 0
        ########################################
        # server settings
        # the size of the msg in bytes.
        self.header = 64
        self.format = 'utf-8'
        self.disconnect_message = "!DISCONNECT"
        self.max_active_client = 3
        ########################################
        # server socket
        # AF_INET -> address family IPV4, SOCK_STREAM -> protocol TCP
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind(self.address)

    # each client runs on a different thread
    def listen_client(self, sck, addr):
        print(f"{addr} connected successfully.")
        connected = True
        while connected:
            # get msg size(bytes)
            msg_length = sck.recv(self.header).decode(self.format)
            if msg_length:
                msg_length = int(msg_length)
                # wait for a new massage
                msg = sck.recv(msg_length).decode(self.format)
                if msg == self.disconnect_message:
                    connected = False

                print(f"[{addr}] {msg}")
                sck.send("Msg received".encode(self.format))
        sck.close()

    # start listening to requests(a thread that always runs in the background)
    # and open a new thread for each client
    def start(self):
        print("server is listening...")
        self.socket.listen()
        while True:
            # wait for a new connection
            # CREATE HERE NEW CLIENT INSTANCE
            client_socket, client_address = self.socket.accept()
            if self.active_clients >= self.max_active_client:
                thread = threading.Thread(target=self.listen_client, args=(client_socket, client_address))
                thread.start()
                self.active_clients += 1
                print(f"active connections: {self.active_clients}")
            else:
                print("server is full. request denied!")


# testing:
my_server = Server("192.168.100.6", 5050)
my_server.start()
