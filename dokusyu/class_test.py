class Orange:
    def __init__(self, w, c):
        self.weight = w
        self.color = c
        print("Created!")

org = Orange(10, "dark orange")
print(org.weight)
print(org.color)

print("\n")

org.weight = 999
org.color = "yellow"
print(org.weight)
print(org.color)