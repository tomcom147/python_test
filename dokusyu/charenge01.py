"""
str = "カミュ"
print(str[0])
print(str[1])
print(str[2])

a = input("入力１：")
b = input("入力２：")
print("私は昨日{}を書いて、{}に送った！".format(a,b))

print("aldous Huxley was born in 1894.".capitalize())

splited = "どこで？だれが？いつ？".split("？")
print(splited)

x = "aldous huxley was born in 1894. he was born in the United Kingdom.".title()
print(x)
"""
fox = ["The", "fox", "jumped", "over", "the", "fence", "."]
fox = " ".join(fox)
print(fox)
fox = fox[0: -2] + "."
print(fox)