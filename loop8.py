n=int(input("value of for the check armstrong no"))
sum=0
i=n
while i>0:
    digit=i%10
    sum=sum+digit**3
    i//=10
if n==sum:
    print("armstromg no")
else:
    print("not armstrong no")
    
