import socket

HEADER = 1024
PORT = 5050
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
SERVER = "192.168.100.3"
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)


def send(msg):
    message = msg.encode(FORMAT)
    client.send(message)
    print(client.recv(HEADER).decode(FORMAT))


# start game msg
print(client.recv(HEADER).decode(FORMAT))
client_input = input()
send(client_input)
client_input = input()
send(client_input)
client_input = input()
send(client_input)
client_input = input()
send(client_input)
client_input = input()
send(client_input)
client_input = input()
send(client_input)
client_input = input()
send(client_input)
send("3")

send(DISCONNECT_MESSAGE)