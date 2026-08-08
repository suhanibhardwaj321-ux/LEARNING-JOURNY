num=int(input("enter the value of terms:"))
n1=0
n2=1
c=0
print(n1)
print(n2)
for i in range(1,num+1):
    n3=n1+n2
    print(n3)
    n1=n2
    n2=n3
