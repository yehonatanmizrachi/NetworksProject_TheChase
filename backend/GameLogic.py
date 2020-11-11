from StringDB import *
from Client import *


class GameLogic:
    @staticmethod
    def part0(client):
        client.send_msg(STR_DB["part0"]["wantToPlay"])
        response = client.receive_valid_msg(["yes", "no"])
        if response == STR_DB["part0"]["wantToPlay_ans"]:
            GameLogic.part1(client)
        else:
            client.send_msg(STR_DB["disconnect"])
            client.socket.close()

    @staticmethod
    def part1(client):
        if client.ask_question(1):
            client.player.add_money(5000)

        if client.ask_question(1):
            client.player.add_money(5000)

        if client.ask_question(1):
            client.player.add_money(5000)

        if client.player.get_money() > 0:
            GameLogic.part2(client)
        else:
            GameLogic.part0(client)

    @staticmethod
    def part2(client):
        # add table in strDB
        client.send_msg("Choose option:[1,2,3]")
        # receive valid input
        response = client.receive_valid_msg(["1", "2", "3"])
        if response == "1":
            GameLogic.part3(client)
        elif response == "2":
            # start in location 2 with double money
            client.player.dec_location()
            client.player.mul_money()
            GameLogic.part3(client)
        else:
            # start in location 4 with half of the money
            client.player.inc_location()
            client.player.div_money()
            GameLogic.part3(client)

    @staticmethod
    def part3(client):
        # player
        if client.ask_question(3):
            client.player.inc_location()
        # chaser
        client.chaser.play()

        status = GameLogic.check_game_ended(client)
        if status == 0:
            GameLogic.part3(client)
        elif status == 2:
            client.reset()
            GameLogic.part1(client)
        # for 1, finish the function and close the socket in GameManager
    # return: 0 -> game is on. 1 -> game has ended and close. 2 -> game has ended and play again.

    @staticmethod
    def check_game_ended(client):
        # case 1: Chaser wins
        if client.player.get_location() == client.chaser.get_location():
            client.send_msg(STR_DB["end"]["chaserWin"] + "\n" + STR_DB["end"]["playAgain"])
            response = client.receive_valid_msg(["yes", "no"]).lower()
            if response == "yes":
                return 2
            else:
                return 1
        # case 2: Player wins
        elif client.player.get_location() == client.get_bank_location():
            client.send_msg(STR_DB["end"]["playerWin"] + "\n" + STR_DB["end"]["playAgain"])
            response = client.receive_valid_msg(["yes", "no"]).lower()
            if response == "yes":
                return 2
            else:
                return 1
        # case 3: Game continue
        else:
            return 0

