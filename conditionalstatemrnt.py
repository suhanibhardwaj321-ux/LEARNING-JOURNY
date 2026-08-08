#traffic light
light=input("light:")
if(light=="red"):
    print("stop")
elif(light=="yellow"):
    print("look")
elif(light=="green"):
    print("go")
else:
    print("light is broken") 

#fee
a=int(input("a:"))
g=input("m/f:")
if((a==1 or a==2)and g=="m"):
    print("fee is 100")
elif(a==3 or a==4 or g=="f"):
    print("fee is 200")
elif(a==5 and g=="m"):
    print("fee is 300")
else:
    print("no fee")   

#single line if / ternary operator
food=input("food:")
eat="yes" if food=="cake" else "no"
print(eat)

food=input("food:")
print("sweet")if food=="cake" or food=="gulabjamun" else print("no sweet")

age=int(input("age:"))
vote=("yes","no")[age<=18]
print(vote)

sal=float(input("salary:"))
tax=sal*(0.1,0.2)[sal<=50000]
print(tax)