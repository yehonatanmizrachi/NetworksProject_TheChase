import tkinter as tk
import tkinter.font as tk_font
from PIL import Image, ImageTk
from GUI_helper import *

WIDTH = 700
HEIGHT = 600
TITLE = "The Chase - part2"

FONT_STYLE = "Lucida Grande"


def start_part2(socket):
    def check_game_over(server_msg):
        if server_msg[0] == 'G' or server_msg[0] == 'W':
            main_frame.destroy()
            money_frame.destroy()
            ll_frame.destroy()
            location_frame.destroy()
            end_msg = ""
            if server_msg[0] == 'G':
                end_msg = "Game Over. Chaser Won ☹!\nDo you want to play again?"
                socket.audio.stop()
                socket.start_audio("lose")
            elif server_msg[0] == 'W':
                end_msg = "Well Played. You Won " + money_label_var.get() + "🙂!\nDo you want to play again?"
                socket.audio.stop()
                socket.start_audio("win")
            socket.start_game(end_msg)
            return 0
        else:
            return 1

    def choose_answer(index):
        socket.send(index)
        current_msg = socket.get_msg()
        if check_game_over(current_msg):
            if index == 5:
                ll_label.destroy()
                load1 = Image.open("Photos/dead@80px.png")
                render1 = ImageTk.PhotoImage(load1)
                ll_label2 = tk.Button(ll_frame, image=render1, bg="SteelBlue2", state="disabled")
                ll_label2.image = render1
                ll_label2.place(anchor='n', relx=0.5, rely=0.1, relwidth=1, relheight=0.8)

                life_line(current_msg, q_gui_list)
                ans3_button["state"] = "disabled"
                ans4_button["state"] = "disabled"
                ll_label_var.set("0")
            else:
                ans3_button["state"] = "normal"
                ans4_button["state"] = "normal"
                current_info_list = parse_question_part2(current_msg)
                update_gui_question(q_gui_list, current_info_list[0])
                update_gui_info(info_gui_list, current_info_list)

    socket.init_window(WIDTH, HEIGHT, TITLE)

    font_style = tk_font.Font(family=FONT_STYLE, size=15)

    main_frame = tk.Frame(socket.root, bg="SteelBlue4", bd=10)
    main_frame.place(anchor='nw', relx=0.3, rely=0, relwidth=0.7, relheight=1)
    # question
    q_label = tk.StringVar()
    question_label = tk.Label(main_frame, bg="SteelBlue4", font=font_style, textvariable=q_label)
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

    q_gui_list = [q_label, ans1_label, ans2_label, ans3_label, ans4_label]

    # life line
    ll_frame = tk.Frame(socket.root, bg="SteelBlue2")
    ll_frame.place(anchor='nw', relx=0, rely=0, relwidth=0.3, relheight=0.2)

    ll_label_var = tk.StringVar()
    load = Image.open("Photos/lifeline@80px.png")
    render = ImageTk.PhotoImage(load)
    ll_label = tk.Button(ll_frame, image=render, bg="SteelBlue2", command=lambda: choose_answer(5))
    ll_label.image = render
    ll_label.place(anchor='n', relx=0.5, rely=0.1, relwidth=1, relheight=0.8)

    # money
    money_frame = tk.Frame(socket.root, bg="SteelBlue1")
    money_frame.place(anchor='nw', relx=0, rely=0.2, relwidth=0.3, relheight=0.2)

    money_label_var = tk.StringVar()
    money_label = tk.Label(money_frame, bg="SkyBlue2", font=font_style, textvariable=money_label_var)
    money_label.place(anchor='n', relx=0.5, rely=0.1, relwidth=1, relheight=0.8)

    # locations
    location_frame = tk.Frame(socket.root, bg="SteelBlue1")
    location_frame.place(anchor='nw', relx=0, rely=0.4, relwidth=0.3, relheight=0.6)

    location_labels = []
    location_labels_vars = []
    for i in range(8):
        location_labels_vars.append(tk.StringVar())
        location_labels.append(tk.Label(location_frame, bg="CadetBlue1", bd=0.01, font=font_style, textvariable=location_labels_vars[i]))
        location_labels[i].place(anchor='n', relx=0.5, rely=0.1 + 0.1*i, relwidth=0.9, relheight=0.08)
    location_labels_vars[-1].set("Bank")
    info_gui_list = [location_labels_vars, money_label_var, ll_label_var]

    # first question
    msg = socket.get_msg()
    info_list = parse_question_part2(msg)
    update_gui_question(q_gui_list, info_list[0])
    update_gui_info(info_gui_list, info_list)
