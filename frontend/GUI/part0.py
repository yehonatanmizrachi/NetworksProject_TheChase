import tkinter as tk
import tkinter.font as tk_font
from part1 import start_part1

WIDTH = 580
HEIGHT = 300
TITLE = "The Chase - part0"

BG = '#80c1ff'
FONT_STYLE = "Lucida Grande"


def start_part0(socket, start_game_msg):
    socket.start_audio("part0")
    socket.init_window(WIDTH, HEIGHT, TITLE)

    def want_to_play():
        socket.send("yes")
        main_frame.destroy()
        start_part1(socket)

    def dont_want_to_play():
        main_frame.destroy()
        socket.send("no")
        socket.close()
        exit()

    main_frame = tk.Frame(socket.root, bg=BG, bd=10)
    main_frame.place(relwidth=1, relheight=1)

    font_style = tk_font.Font(family=FONT_STYLE, size=18)

    # do you want to play label
    welcome_label_var = tk.StringVar()
    welcome_label = tk.Label(main_frame, textvariable=welcome_label_var, bg=BG, font=font_style)
    welcome_label.place(anchor='n', relx=0.5, rely=0.1, relwidth=1, relheight=0.4)

    welcome_label_var.set(start_game_msg)
    # yes and no buttons
    yes_button = tk.Button(main_frame, text="yes", font='40', command=lambda: want_to_play())
    yes_button.place(anchor='n', relx=0.3, rely=0.65, relwidth=0.3, relheight=0.15)

    no_button = tk.Button(main_frame, text="no", font='40', command=lambda: dont_want_to_play())
    no_button.place(anchor='n', relx=0.7, rely=0.65, relwidth=0.3, relheight=0.15)

    if not socket.lose_counter:
        socket.root.mainloop()
