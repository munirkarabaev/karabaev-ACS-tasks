strinng = input("Please enter a string that you would like to be reversed")

def reverse(a, i):
    
    if i < len(a):
        i=i+1
        reverse(a, i)
        print(a[i-1])
    
    i=i-1


reverse(strinng, 0)
