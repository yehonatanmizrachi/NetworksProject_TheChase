STR_DB = {
    "part0": {
        "wantToPlay": "Do you want to play? (yes/no)",
        "wantToPlay_ans": "yes"
    },
    "part1": {
        "wantToPlay": "Do you want to play? (yes/no)",
        "wantToPlay_ans": "yes"
    },
    "part2": {
        "options": "Please choose one of the following options:\n"
                   "1- start at location 3 with your current money\n"
                   "2- start at location 2 with double money\n"
                   "3- start at location 4 with half money\n"

    },
    "part3": {
        "wantToPlay": "Do you want to play? (yes/no)",
        "wantToPlay_ans": "yes"
    },
    "end": {
        "chaserWin": "Game Over. Chaser Won!",
        "playerWin": "Well Played. You Won!",
        "playAgain": "Do you want to play again? (yes/no)"
    },
    "activateLifeLine": "Life line activated. Please select your answer:\n",
    "invalid": "Invalid input. Please try again",
    "p3Qheader": "Choose answer. 5 - for life line\n",
    
    "disconnect": "!DISCONNECT",
    "usedLifeLine": "you already used the life line. Please choose an answer.",
    "Q": [
        ["Which country is the smallest?", [["Israel", True], ["Syria", False], ["Egypt", False], ["Lebanon", False]]],
        ["Which country is the largest?", [["Russia", True], ["India", False], ["Israel", False], ["London", False]]],
        ["Which city is the northernmost?", [["Netanya", True], ["Yafo", False], ["Herzelia", False], ["Dimona", False]]],
        ["Which city is the southernmost?", [["Ashkelon", True], ["Haifa", False], ["Naharia", False], ["Ashdod", False]]],
        ["How many days are there in a year?", [["365", True], ["364", False], ["360", False], ["520", False]]],
        ["How many days are there in a month?", [["Depends", True], ["30", False], ["31", False], ["27", False]]],
        ["What is the second month?", [["February", True], ["January", False], ["March", False], ["April", False]]],
        ["What is the 11th month?", [["November", True], ["October", False], ["December", False], ["September", False]]],
        ["How many minutes are there per hour?", [["60", True], ["50", False], ["90", False], ["120", False]]],
        ["How many degrees are in a triangle?", [["180", True], ["190", False], ["90", False], ["100", False]]],
        ["What's the police phone number?", [["100", True], ["101", False], ["102", False], ["106", False]]],
        ["Which one is the best university?", [["Bar Ilan", True], ["Tel Aviv", False], ["Haifa", False], ["Ben Gurion", False]]],
        ["What color appears in a rainbow?", [["Yellow", True], ["Black", False], ["Silver", False], ["Pink", False]]],
        ["What color is not appears in a rainbow?", [["Gold", True], ["Green", False], ["Purple", False], ["Blue", False]]],
        ["How many colors are there in a rainbow?", [["7", True], ["5", False], ["8", False], ["10", False]]]
    ]

}


def copy_question(question):
    copy = [question[0], [ans.copy() for ans in question[1]]]
    return copy
