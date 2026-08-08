n=int(input("value for palindorme from 1 t0 input no"))
rev=0
print("all paliondorme 1 to n are:-")
for i in range(1,n+1):
    m=i
    while(i!=0):
        rev=(rev*10)+(i%10)
        i=i//10
    if rev==m:
        print(m,end=" ")
    rev=0    
