class GameLogic:
    @staticmethod
    def start_part0(client):
        client.send_msg("Do you want to play? (yes/no)")
        response = client.receive_msg()
        print(response.lower())
        if response.lower() == "yes":
            GameLogic.start_part1(client)
        else:
            print("client don't want to play")
            client.socket.close()

    @staticmethod
    def start_part1(client):
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
            GameLogic.start_part2(client)
        else:
            GameLogic.start_part0(client)

    @staticmethod
    def start_part2(client):
        client.send_msg("Choose option:")
        # receive valid input
        response = client.receive_valid_msg(["1", "2", "3"])
        if response == "1":
            GameLogic.start_part3(client)
        elif response == "2":
            # start in location 2 with double money
            client.player.dec_location()
            client.player.mul_money()
            GameLogic.start_part3(client)
        elif response == "3":
            # start in location 4 with half of the money
            client.player.inc_location()
            client.player.div_money()
            GameLogic.start_part3(client)

    @staticmethod
    def start_part3(client):
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
        client.send_game_status()

        print(f"Location: {client.player.get_location()} Money: {client.player.get_money()}")



