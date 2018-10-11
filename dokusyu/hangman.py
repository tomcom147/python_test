""" hangman.py """
import random

def hangman(word):
    wrong = 0
    stages = ["",
              "______    ",
              "|     |   ",
              "|     O   ",
              "|    /|\  ",
              "|    / \  ",
              "          "]
    reletters = list(word)
    board = ["_"] * len(word)
    win = False
    print("ハングマンへようこそ！")

    while wrong < len(stages) -1:
        inputchar = True
        while inputchar:
            print("\n")
            msg = "1文字を予想してね　：　"
            char = input(msg)
            if len(char) == 1:
                inputchar = False
            else:
                print("1文字だけ入力してね")
        if char in reletters:
            cind = reletters.index(char)
            board[cind] = char
            reletters[cind] = "$"
        else:
            wrong += 1
        print(" ".join(board))
        e = wrong + 1
        print("\n".join(stages[0:e]))
        if "_" not in board:
            print("あなたの勝ち！")
            print(" ".join(board))
            win = True
            break
    if not win:
        print("\n".join(stages[0:wrong + 1]))
        print("あなたの負け！正解は　{}.".format(word))

wordlist = ["cat",
            "human",
            "green",
            "indivisual",
            "apple",
            "banana",
            "peach"]

#print(wordlist[random.randint(0,len(wordlist)-1)])
#print(wordlist(random.randint(0,len(wordlist))))
hangman(wordlist[random.randint(0,len(wordlist)-1)])