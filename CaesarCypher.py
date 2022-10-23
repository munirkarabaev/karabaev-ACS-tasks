string = input("please input a string") 

num = int(input("please input the number of char you would like to shift")) 

for i in range(0,len(string)): 
    if ord(string[i]) >= ord('a') and ord(string[i]) <= ord('z'):
        
        if ord(string[i])+num >= ord('z')+1: 

            print(chr(ord(string[i])+num-26), end = '') 

        else: 

            print(chr(ord(string[i])+num), end = '')
    else:
        print(string[i], end='') 