# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！

input_lines = input('[ステージ高さ] [ステージ幅] [ブロック数] : ').split(' ')

stage_h = int(input_lines[0])
stage_w = int(input_lines[1])
blocknum = int(input_lines[2])

def makeField(x, y):
    field = list()
    for i in range(x):
        line = list()
        for j in range(y):
            line.append(0)
        field.append(line)
    return field

def maxBlock(block_w, position, field):
    max_h = len(field)
    for i in range(len(field)):
        for j in range(position, position + block_w):
            if (field[i][j] == 1 ):
                max_h = i
                break
        else:
            continue
        break
        
    return max_h

def putBlock(block_h, block_w, position, field):
    max_h = maxBlock(block_w, position, field) - 1
    for i in range(block_h):
        for j in range(position, position + block_w):
            field[max_h - i][j] = 1
    return field

def printField(field):
    for i in range(len(field)):
        for j in range(len(field[i])):
            if(field[i][j] == 0): print('.', end='')
            else: print('#', end='')
        print('')

#main
field = makeField(stage_h, stage_w)
printField(field)

for i in range(blocknum):
    input_lines2 = input('[ブロック高さ] [ブロック幅] [配置位置] : ').split(' ')
    block_h = int(input_lines2[0])
    block_w = int(input_lines2[1])
    position = int(input_lines2[2])
    putBlock(block_h, block_w, position, field)
    printField(field)
