from client_socket import *

START_PLAY_MSG = "Do you want to play?"

client_socket = Client()
client_socket.get_msg()
client_socket.start_game(START_PLAY_MSG)
