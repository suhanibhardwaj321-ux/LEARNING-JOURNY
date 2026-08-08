st=float(input("enter the starting reading"))
ed=float(input("enter the ending reading"))
unit=ed-st
if unit<=100:
    bill=unit*2.5
elif unit<=300:
    bill=100*2.5+((unit-100)*3)
elif unit<=500:
    bill=100*2+200*3+((unit-300)*3.5)
else:
       bill=unit*4
print(bill)       
