# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！

count = int(input())

outputword = ""
word_aft = ""
outputword = ""
match = False
match_num = 0

for i in range(0, count):
    word_aft = input()
    print("count : " + str(i))
    print("outputword : " + outputword)
    print("word_aft : " + word_aft)
    
    for j in range(0, len(outputword)):
        print("comp outputword : " + outputword[j:])
        print("comp word_aft : " + word_aft[:len(outputword[j:])])
        if(outputword[j:] == word_aft[:len(outputword[j:])]):
            print("match : " + outputword[j:])
            #outputword += word_aft[len(outputword[j:]):]
            match = True
            match_word = outputword[j:]
            print("match_num : " + str(j))
            break
        else:
            match = False
    if(match == True):
        print("match!")
        print("out_bef : " + outputword)
        print(word_aft[match_num+len(match_word):])
        outputword += word_aft[match_num+len(match_word):]
        print("out_aft : " + outputword)
        
    else:
        print("unmatch!")
        print("out_bef : " + outputword)
        outputword += word_aft
        print("out_aft : " + outputword)
        #match = False
    #outputword = word_aft
    

"""
for i in range(0, count):
    word2 = input()
    print("w1 : " + word1)
    print("w2 : " + word2)
    
    for j in range(0, len(word1)):
        if(word1[-j-1:] == word2[:j+1]):
            print("match : " +word1[-j-1:])
            #print("word2 : " +word2[:j+1])
            #print(word1[:-j-1])
            #outputword += word1
            outputword += word2[j+1:]
            flag = True
            print("in  : " +word2[j+1:])
            print("out : " +outputword)
    print(flag)
    if(flag != True):
        #print(flag)
        outputword += word2
        print("in  : " +word2)
        print("out : " +outputword)
    flag = False
        
    word1 = word2
 """ 
print(outputword)