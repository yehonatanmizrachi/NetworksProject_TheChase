from Player import *
from Chaser import *
import time
from StringDB import *
import random


class Client:
    # for each client generate random sequence of questions
    @staticmethod
    def get_random_questions():
        random_questions = list(range(len(STR_DB["Q"])))
        random.shuffle(random_questions)
        return random_questions

    # beautify questions for the client
    @staticmethod
    def parse_question(question):
        msg = f"\n{question[0]}\n"
        for i, ans in enumerate(question[1]):
            msg += f"{i+1}: {ans[0]}\n"
        return msg

    def __init__(self, socket, address, bank_location=7):
        ########################################
        # socket settings
        self.socket = socket
        self.address = address
        self.msg_size = 1024
        self.format = 'utf-8'
        self.player = Player()
        self.chaser = Chaser()
        self.bank_location = bank_location
        self.random_questions = Client.get_random_questions()
        self.current_question = 0
        self.num_of_part1_q = 3
        ########################################

    def send_msg(self, msg):
        self.socket.send(msg.encode(self.format))
        # wait 0.1 sec so that each message will be sent separately
        time.sleep(0.1)

    def receive_msg(self):
        return self.socket.recv(self.msg_size).decode(self.format)

    # checks if the msg is valid. If not, ask for a new response
    def receive_valid_msg(self, options):
        response = self.receive_msg().lower()
        while response not in options:
            self.send_msg(STR_DB["invalid"])
            response = self.receive_msg().lower()
        return response

    # generate the status of the game - money, locations, life line, etc.
    def get_game_status(self):
        board = ["      " for i in range(self.bank_location + 1)]
        board[self.player.get_location()] = "Player"
        board[self.chaser.get_location()] = "Chaser"
        board[self.bank_location] = " Bank "

        game_status_msg = f"-------------------------------------\n"
        for i, position in enumerate(board):
            game_status_msg += f"|        {i}         |     {position}     |\n"
        game_status_msg += f"-------------------------------------\n"

        game_status_msg += f"\nMoney: {self.player.get_money()} \n" \
                           f"Life line: {'unavailable' if self.player.get_life_line_status() else 'available'}\n" \

        return game_status_msg

    def get_bank_location(self):
        return self.bank_location

    # use before starting a another game
    def reset(self):
        del self.player
        self.player = Player()
        del self.chaser
        self.chaser = Chaser()
        self.current_question = 0
        self.random_questions = Client.get_random_questions()

    def ask_question(self, part=3):
        question = self.get_next_question()
        # msg header
        msg = ''
        ans_range = 0
        if part == 1:
            ans_range = len(question[1])
        elif part == 3:
            msg += self.get_game_status()
            msg += STR_DB["p3Qheader"]
            ans_range = len(question[1]) + 1
        # add the question to the header
        msg += Client.parse_question(question)

        self.send_msg(msg)
        # get the response
        response = int(self.receive_valid_msg([str(i + 1) for i in range(ans_range)])) - 1

        # if used life line
        if response == len(question[1]):
            if not self.player.get_life_line_status():
                new_ans = []
                # make the 50/50 life line
                for i, ans in enumerate(question[1]):
                    if ans[1]:
                        new_ans.append(ans)
                        question[1].pop(i)
                for ans in question[1][0:int(len(question[1])/2)]:
                    new_ans.append(ans)
                random.shuffle(new_ans)
                question[1] = new_ans

                msg = STR_DB["activateLifeLine"]
                msg += Client.parse_question(question)
                self.send_msg(msg)
                response = int(self.receive_valid_msg([str(i + 1) for i, x in enumerate(range(0, len(question[1])))]))-1
                self.player.used_life_line = True
            else:
                self.send_msg(STR_DB["usedLifeLine"])
                response = int(self.receive_valid_msg([str(i + 1) for i, x in enumerate(range(0, len(question[1])))]))-1

        return question[1][response][1]

    def get_next_question(self):
        question = copy_question(STR_DB["Q"][self.random_questions[self.current_question]])
        random.shuffle(question[1])
        self.current_question += 1
        return question
