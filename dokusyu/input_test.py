a = input("type a number:")
b = input("type another:")

try:
    a = int(a)
    b = int(b)
    print(a/b)
except (ZeroDivisionError, ValueError):
    print("Error : Invalid input")