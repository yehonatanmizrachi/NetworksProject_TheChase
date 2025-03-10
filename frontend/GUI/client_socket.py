import socket
import tkinter as tk
from part0 import start_part0
import simpleaudio as sa

HEADER = 1024
PORT = 5050
FORMAT = 'utf-8'
SERVER_IP = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER_IP, PORT)


class Client:
    def __init__(self):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.connect(ADDR)
        self.disconnect_message = "!DISCONNECT"
        self.lose_counter = -1
        self.root = tk.Tk()
        self.icon = tk.PhotoImage(file="./Photos/icon.png")
        self.root.iconphoto(False, self.icon)
        self.root.resizable(False, False)
        self.canvas = tk.Canvas(self.root)
        self.canvas.pack()
        self.audio = None
        self.button_bg = 'LightBlue2'
        self.font = "Purisa"
        self.exit = False

    def send(self, msg):
        msg = str(msg)
        self.server.send(msg.encode(FORMAT))

    def get_msg(self):
        msg = self.server.recv(HEADER).decode(FORMAT)
        return msg

    # close socket and exit game
    def close(self):
        self.server.close()

    def start_game(self, msg):
        self.lose_counter += 1
        start_part0(self, msg)

    def init_window(self, width, height, title):
        self.root.title(title)
        self.canvas.config(width=width, height=height)

    def start_audio(self, path):
        path = 'MP3/' + path + '.wav'
        wave_obj = sa.WaveObject.from_wave_file(path)
        self.audio = wave_obj.play()
