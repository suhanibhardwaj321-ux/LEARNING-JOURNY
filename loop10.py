n=int(input("input thr value of no:"))
a=0
b=1
c=0
i=1
while c<n:
    c=a+b
    a=b
    b=c
if c==n:
    print("fibonaci no")
else:
    print("not febonaci no")
