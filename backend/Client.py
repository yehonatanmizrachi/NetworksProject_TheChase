from Player import *
from Chaser import *
import time


class Client:
    def __init__(self, socket, address, bank_location=7):
        ########################################
        # socket settings
        self.socket = socket
        self.__address = address
        self.__msg_size = 1024
        self.__format = 'utf-8'
        ########################################
        self.player = Player()
        self.chaser = Chaser()
        self.__bank_location = bank_location

    def send_msg(self, msg):
        self.socket.send(msg.encode(self.__format))
        # wait 0.1 sec so that each message will be sent separately
        time.sleep(0.1)

    def receive_msg(self):
        return self.socket.recv(self.__msg_size).decode(self.__format)

    # checks if the msg is valid. If not, ask for a new response
    def receive_valid_msg(self, options):
        response = self.receive_msg()
        while response not in options:
            self.send_msg("Invalid input. Please try again.")
            response = self.receive_msg()
        return response

    def send_game_status(self):
        game_status_msg = f"Your money: {self.player.get_money()} \n" \
                          f"Your location: {self.player.get_location()} \n" \
                          f"Chaser's location: {self.chaser.get_location()} \n" \
                          f"Life line: {'available' if self.player.get_life_line_status() else 'unavailable'}"
        self.send_msg(game_status_msg)

    def get_bank_location(self):
        return self.__bank_location

    def reset(self):
        del self.player
        self.player = Player()
        del self.chaser
        self.chaser = Chaser()
