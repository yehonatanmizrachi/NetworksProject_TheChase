import tkinter as tk
import tkinter.font as tk_font
from part1 import start_part1

HEIGHT = 250
WIDTH = 400

BG = '#80c1ff'
FONT_STYLE = "Lucida Grande"


def start_part0(socket):
    root = tk.Tk()
    root.title("The Chase - part0")

    def want_to_play():
        socket.send("yes")
        root.destroy()
        start_part1(socket)

    def dont_want_to_play():
        root.destroy()
        socket.close()
        exit()

    canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
    canvas.pack()

    main_frame = tk.Frame(root, bg=BG, bd=10)
    main_frame.place(relwidth=1, relheight=1)

    font_style = tk_font.Font(family=FONT_STYLE, size=18)

    # do you want to play label
    welcome_label = tk.Label(main_frame, text="Do you want to play?", bg=BG, font=font_style)
    welcome_label.place(anchor='n', relx=0.5, rely=0.1, relwidth=1, relheight=0.2)
    # yes and no buttons
    yes_button = tk.Button(main_frame, text="yes", font='40', command=lambda: want_to_play())
    yes_button.place(anchor='n', relx=0.3, rely=0.6, relwidth=0.3, relheight=0.15)

    no_button = tk.Button(main_frame, text="no", font='40', command=lambda: dont_want_to_play())
    no_button.place(anchor='n', relx=0.7, rely=0.6, relwidth=0.3, relheight=0.15)

    root.mainloop()
