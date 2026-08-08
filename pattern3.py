n=int(input("enter the value of n:"))
for i in range(1,n+1):
    print("")
    for j in range(1,n-i+1):
        print(" ",end=" ")
    for j in range(1,2*i):
        print("*",end=" ")



#another pattern type
n=int(input("enter the value n:"))
for i in range(1,n+1):
    print("")
    for j in range(1,n-i+1):
        print(" ",end=" ")
    for j in range(1,2*i):
        print("*",end=" ")
for i in range(1,n+1):
    print("")
    for j in range(1,n-j+1):
        print(" ",end=" ")
    for j in range(1,2*n-i+1+1):
        print("*",end=" ")
