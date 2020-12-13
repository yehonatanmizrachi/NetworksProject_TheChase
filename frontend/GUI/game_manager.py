from client_socket import *
import atexit


def exit_game():
    client_socket.send(client_socket.disconnect_message)
    client_socket.close()


atexit.register(exit_game)

START_PLAY_MSG = "Do you want to play?"

client_socket = Client()
response = client_socket.get_msg()
if response[0] == 'S':
    print("Server is full. Please try again later.")
    exit()
client_socket.start_game(START_PLAY_MSG)

