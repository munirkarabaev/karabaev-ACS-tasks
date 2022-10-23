sentence= input("please input a sentence") 

num = 1 

for i in range(0,len(sentence)): 

    if sentence[i] == " ": 

        num = num+1 

    #End if 

#Next i 

print(num, "words") 