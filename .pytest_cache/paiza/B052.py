# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！

input_lines = input().split(' ')
field_h = int(input_lines[0])
field_w = int(input_lines[1])
count = int(input_lines[2])

def initField(field_h, field_w):
    field = list()
    for i in range(field_h):
        line = list()
        for j in range(field_w):
            line.append(0)
        field.append(line)
    return field

def putParticle(x, y, field):
    if(x-1 >= 0 and field[x][y] > field[x-1][y]):
        putParticle(x-1, y, field)
    elif(y+1 < len(field[x]) and field[x][y] > field[x][y+1]):
        putParticle(x, y+1, field)
    elif(x+1 < len(field) and field[x][y] > field[x+1][y]):
        putParticle(x+1, y, field)
    elif(y-1 >= 0 and field[x][y] > field[x][y-1]):
        putParticle(x, y-1, field)
    else:
        field[x][y] += 1
    return field

def printField(field):
    for i in range(len(field)):
        print(' '.join(map(str,field[i])))

#main
field = initField(field_h, field_w)
for i in range(count):
    input_lines2 = input().split(' ')
    x = int(input_lines2[1]) -1
    y = int(input_lines2[0]) -1
    putParticle(x, y, field)
printField(field)