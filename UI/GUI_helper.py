def update_gui_info(gui_list, info_list):
    gui_list[-1].set(info_list[-1])
    gui_list[-2].set(info_list[-2])
    for i in range(7):
        if i == info_list[1]:
            gui_list[0][i].set("Chaser")
        elif i == info_list[2]:
            gui_list[0][i].set("Player")
        else:
            gui_list[0][i].set("")


def update_gui_question(gui_list, q_list):
    for i in range(5):
        gui_list[i].set(q_list[i])


def substring_lines(string, start=0, end=-1):
    new_str = ""
    lines_counter = 0
    for letter in string:
        if lines_counter >= start:
            if lines_counter <= end or end == -1:
                new_str += letter
            else:
                break
        if letter == '\n':
            lines_counter += 1
    return new_str


def parse_question(server_msg):
    question = []
    counter = 0
    question.append(substring_lines(server_msg, 0, 0))
    server_msg = substring_lines(server_msg, 1)
    for i in range(1, 5):
        question.append("")
        while server_msg[counter] != '\n':
            question[i] += server_msg[counter]
            counter += 1
        question[i] = question[i][3:]
        counter += 1
    return question


def parse_ll(server_msg):
    pass

def parse_question_part2(server_msg):
    if server_msg[0] == 'P':
        server_msg = substring_lines(server_msg, 4)

    question = parse_question(substring_lines(server_msg, 14, 18))

    chaser_location = int(server_msg.find("Chaser") / 37) - 1
    player_location = int(server_msg.find("Player") / 37) - 1

    money = int(substring_lines(server_msg, 11, 11)[len("Money: "):])

    life_line_str = substring_lines(server_msg, 12, 12)[len("Life line: "):]
    life_line = False
    if life_line_str == "available\n":
        life_line = True

    return [question, chaser_location, player_location, money, life_line]
