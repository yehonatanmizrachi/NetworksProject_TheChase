from StringBank import *


class GameLogic:
    @staticmethod
    def part0(client):
        client.send_msg(STR_BANK["part0"]["wantToPlay"])
        response = client.receive_msg()
        print(response.lower())
        if response.lower() == STR_BANK["part0"]["wantToPlay_ans"]:
            GameLogic.part1(client)
        else:
            print("client don't want to play")
            client.socket.close()

    @staticmethod
    def part1(client):
        client.send_msg("question1")
        if client.receive_msg() == "Answer1":
            client.player.add_money(5000)
        client.send_msg("question2")
        if client.receive_msg() == "Answer2":
            client.player.add_money(5000)
        client.send_msg("question3")
        if client.receive_msg() == "Answer3":
            client.player.add_money(5000)
        if client.player.get_money() > 0:
            GameLogic.part2(client)
        else:
            GameLogic.part0(client)

    @staticmethod
    def part2(client):
        client.send_msg("Choose option:")
        # receive valid input
        response = client.receive_valid_msg(["1", "2", "3"])
        if response == "1":
            GameLogic.part3(client)
        elif response == "2":
            # start in location 2 with double money
            client.player.dec_location()
            client.player.mul_money()
            GameLogic.part3(client)
        elif response == "3":
            # start in location 4 with half of the money
            client.player.inc_location()
            client.player.div_money()
            GameLogic.part3(client)

    @staticmethod
    def part3(client):
        # player
        client.send_msg("Choose answer. 5 - for life line")
        response = client.receive_valid_msg(["1", "2", "3", "4", "5"])
        if response in ["1", "2", "3", "4"]:
            correct = True  # add later from class Question
            if correct:
                client.player.inc_location()
        # life line
        else:
            pass
        # chaser
        client.chaser.play()
        response = client.send_game_status()
        if response == 0:
            GameLogic.part3()
        elif response == 2:
            client.reset()
            GameLogic.part1()
        # for 1, finish the function and close the socket in GameManager
    # return: 0 -> game is on. 1 -> game has ended and close. 2 -> game has ended and play again.
    @staticmethod
    def check_game_ended(client):
        # case 1: Chaser wins
        if client.player.get_location() == client.chaser.get_location():
            client.send_msg(STR_BANK["end"]["chaserWin"] + "\n" + STR_BANK["end"]["playAgain"])
            response = client.receive_valid_msg(["yes", "no"]).lower()
            if response == "yes":
                return 2
            else:
                return 1
        # case 2: Player wins
        elif client.player.get_location() == client.get_bank_location():
            client.send_msg(STR_BANK["end"]["playerWin"] + "\n" + STR_BANK["end"]["playAgain"])
            response = client.receive_valid_msg(["yes", "no"]).lower()
            if response == "yes":
                return 2
            else:
                return 1
        # case 3: Game continue
        else:
            return 0

