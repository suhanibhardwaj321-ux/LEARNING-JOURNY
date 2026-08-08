n=int(input("value of n:"))
f=1
if n<0:
    print("not define for negative no")
for i in range(1,n+1):
    f=f*i
    print(f)

#second method
n=int(input("value of n:"))
f=1

for i in range(1,n+1):
    if n<0:
       print("not define for negative no")

    f=f*i
    print(f"fact of{i}is {f}")

