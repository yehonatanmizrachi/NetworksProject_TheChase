import socket

HEADER = 1024
PORT = 5050
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
SERVER_IP = "10.0.0.5"
ADDR = (SERVER_IP, PORT)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.connect(ADDR)

connected = True
while connected:
    response = server.recv(HEADER).decode(FORMAT)
    if response == DISCONNECT_MESSAGE:
        connected = False
        continue
    print(response)
    user_input = input()
    server.send(user_input.encode(FORMAT))

# close socket and exit game
server.close()
