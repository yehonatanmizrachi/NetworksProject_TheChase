import tkinter as tk
import tkinter.font as tk_font
from part2 import start_part2
from GUI_helper import *

WIDTH = 550
HEIGHT = 400
TITLE = "The Chase - part1"
BG = '#80c1ff'
FONT_STYLE = "Lucida Grande"
PLAY_AGAIN_MSG = "You don't have any money ☹\nDo you want to play again?"

q_counter = 0


def start_part1(socket):
    global q_counter
    q_counter = 0
    
    def choose_option(current_msg):
        def init_location(option):
            socket.send(option)
            options_frame.destroy()
            start_part2(socket)

        socket.start_audio("part2")

        options_frame = tk.Frame(socket.root, bg=BG, bd=10)
        options_frame.place(relwidth=1, relheight=1)

        choose_label = tk.Label(options_frame, text="Choose one of the following options:", bg=BG, font=font_style)
        choose_label.place(anchor='n', relx=0.5, rely=0.05, relwidth=1, relheight=0.3)

        op1_button = tk.Button(options_frame, text="start at location 3 with your current money", font='40', command=lambda: init_location(1))
        op1_button.place(anchor='n', relx=0.5, rely=0.4, relwidth=0.8, relheight=0.15)

        op2_button = tk.Button(options_frame, text="start at location 2 with double money", font='40', command=lambda: init_location(2))
        op2_button.place(anchor='n', relx=0.5, rely=0.6, relwidth=0.8, relheight=0.15)

        op3_button = tk.Button(options_frame, text="start at location 4 with half money", font='40', command=lambda: init_location(3))
        op3_button.place(anchor='n', relx=0.5, rely=0.8, relwidth=0.8, relheight=0.15)

    def choose_answer(index):
        global q_counter
        socket.send(index)
        if q_counter < 3:
            current_q = socket.get_msg()
            parsed_current_q = parse_question(current_q)
            update_gui_question(gui_list, parsed_current_q)
            q_counter += 1
        else:
            main_frame.destroy()
            current_msg = socket.get_msg()
            socket.audio.stop()
            if current_msg[0] == "D":
                socket.audio.stop()
                socket.start_audio("lose")
                socket.start_game(PLAY_AGAIN_MSG)
            else:
                choose_option(current_msg)

    socket.init_window(WIDTH, HEIGHT, TITLE)

    font_style = tk_font.Font(family=FONT_STYLE, size=15)

    main_frame = tk.Frame(socket.root, bg=BG, bd=10)
    main_frame.place(relwidth=1, relheight=1)
    # question
    q_label = tk.StringVar()
    question_label = tk.Label(main_frame, bg=BG, font=font_style, textvariable=q_label)
    question_label.place(anchor='n', relx=0.5, rely=0.1, relwidth=1, relheight=0.2)

    # answers
    ans1_label = tk.StringVar()
    ans1_button = tk.Button(main_frame, textvariable=ans1_label, font='40', command=lambda: choose_answer(1))
    ans1_button.place(anchor='n', relx=0.3, rely=0.4, relwidth=0.3, relheight=0.2)

    ans2_label = tk.StringVar()
    ans2_button = tk.Button(main_frame, textvariable=ans2_label, font='40', command=lambda: choose_answer(2))
    ans2_button.place(anchor='n', relx=0.7, rely=0.4, relwidth=0.3, relheight=0.2)

    ans3_label = tk.StringVar()
    ans3_button = tk.Button(main_frame, textvariable=ans3_label, font='40', command=lambda: choose_answer(3))
    ans3_button.place(anchor='n', relx=0.3, rely=0.65, relwidth=0.3, relheight=0.2)

    ans4_label = tk.StringVar()
    ans4_button = tk.Button(main_frame, textvariable=ans4_label, font='40', command=lambda: choose_answer(4))
    ans4_button.place(anchor='n', relx=0.7, rely=0.65, relwidth=0.3, relheight=0.2)

    gui_list = [q_label, ans1_label, ans2_label, ans3_label, ans4_label]

    # first question
    msg = socket.get_msg()
    parsed_q = parse_question(msg)
    update_gui_question(gui_list, parsed_q)

    q_counter += 1
