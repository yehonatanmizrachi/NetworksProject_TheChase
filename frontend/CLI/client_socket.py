import socket

HEADER = 1024
PORT = 5050
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
try:
    SERVER_IP = socket.gethostbyname(socket.gethostname())
    ADDR = (SERVER_IP, PORT)
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.connect(ADDR)

except:
    print("Can't connect to the server. Please try later")
    exit()

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
