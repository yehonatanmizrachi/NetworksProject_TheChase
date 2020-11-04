
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

    # @staticmethod
    # def start_part2(client):




