import tkinter as tk
import tkinter.font as tk_font
from GUI_helper import update_gui_question
HEIGHT = 400
WIDTH = 550
BG = '#80c1ff'
FONT_STYLE = "Lucida Grande"


def choose_answer(index):
    print(index)


def start_part1(socket):
    root = tk.Tk()
    root.title("The Chase - part1")

    canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
    canvas.pack()

    font_style = tk_font.Font(family=FONT_STYLE, size=18)

    main_frame = tk.Frame(root, bg=BG, bd=10)
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

    update_gui_question(gui_list,
                        ["What color is not appears in a rainbow?", "Ben Gurion","Ben Gurion","Ben Gurion","Ben Gurion"])

    root.mainloop()

