from Client import *


class GameLogic:
    @staticmethod
    # part0 = beginning part
    def part0(client):
        # ask player if he wants to play
        client.send_msg(STR_DB["part0"]["wantToPlay"])
        response = client.receive_valid_msg(["yes", "no"])
        if response == STR_DB["part0"]["wantToPlay_ans"]:
            GameLogic.part1(client)
        else:
            client.send_msg(STR_DB["disconnect"])
            client.socket.close()

    # part 1 - ask the first 3 question
    @staticmethod
    def part1(client):
        for i in range(client.num_of_part1_q):
            # ask question for part 1 (without life line)
            if client.ask_question(1):
                client.player.add_money(5000)
        # continue only if the player has money
        if client.player.get_money() > 0:
            GameLogic.part2(client)
        else:
            GameLogic.part0(client)

    # part 2 - player choose initial location
    @staticmethod
    def part2(client):
        client.send_msg(STR_DB['part2']['options'])
        # receive valid input
        response = client.receive_valid_msg(["1", "2", "3"])
        #  1- start at location 3
        if response == "1":
            GameLogic.part3(client)
        # 2- start at location 2 with double money
        elif response == "2":
            # start in location 2 with double money
            client.player.dec_location()
            client.player.mul_money()
            GameLogic.part3(client)
        # 3- start at location 4 with half money
        else:
            # start in location 4 with half of the money
            client.player.inc_location()
            client.player.div_money()
            GameLogic.part3(client)

    # part 3 - questions and answers
    @staticmethod
    def part3(client):
        # player is playing
        if client.ask_question():
            client.player.inc_location()
        # chaser is playing
        client.chaser.play()

        # check if game is over
        status = GameLogic.check_game_ended(client)
        # the game is on! continue
        if status == 0:
            GameLogic.part3(client)
        # the game is over! play again
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
            # ask the player if he wants to play again
            response = client.receive_valid_msg(["yes", "no"]).lower()
            if response == "yes":
                return 2
            else:
                client.send_msg(STR_DB["disconnect"])
                return 1
        # case 2: Player wins
        elif client.player.get_location() == client.get_bank_location():
            client.send_msg(STR_DB["end"]["playerWin"] + "\n" + STR_DB["end"]["playAgain"])
            # ask the player if he wants to play again
            response = client.receive_valid_msg(["yes", "no"]).lower()
            if response == "yes":
                return 2
            else:
                client.send_msg(STR_DB["disconnect"])
                return 1
        # case 3: Game continue
        else:
            return 0

