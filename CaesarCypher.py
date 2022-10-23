string = input("please input a string") 

num = int(input("please input the number of char you would like to shift")) 

for i in range(0,len(string)): 
    if ord(string[i]) >= ord('a') and ord(string[i]) <= ord('z'): #checks if character is between a and z
        
        if ord(string[i])+num >= ord('z')+1: # checks if the character will be shifted past z

            print(chr(ord(string[i])+num-26), end = '') #moves back to the beginning of the alphabet if the character is shifted past z

        else: 

            print(chr(ord(string[i])+num), end = '')
        #end if
    else:
        print(string[i], end='') #prints capital and spaces as normal
    #end if
#next i