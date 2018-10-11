colors = ["purple", "orange", "green"]

guess = input("何色でしょう？（英語で入力してください）：")

if guess in colors:
    print("あたり！")
else:
    print("ハズレ！")