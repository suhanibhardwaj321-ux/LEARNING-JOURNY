n=int(input("enter the value of n:"))
for i in range(1,n+1):
    print("")
    for j in range(1,n-i+1):
        print(" ",end=" ")
    for j in range(1,i+1):
        print("*",end=" ")
#another pattern
n=int(input("enter the value of n:"))
for i in range(1,n+1):
    print("")
    for j in range(1,i):
        print(" ",end=" ")
    for j in range(1,n-i+1+1):
        print("*",end=" ")
    
