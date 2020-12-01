def update_gui_question(gui_list, q_list):
    for i in range(5):
        gui_list[i].set(q_list[i])


def parse_question(server_msg):
    question = []
    counter = 0
    for i in range(5):
        question.append("")
        while server_msg[counter] != '\n':
            question[i] += server_msg[counter]
            counter += 1
        counter += 1
    return question
