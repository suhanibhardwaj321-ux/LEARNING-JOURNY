subject1=int(input("enter marks of subject1:"))
subject2=int(input("enter marks of subject2:"))
subject3=int(input("enter marks of subject3:"))
total=subject1+subject2+subject3
per=(total/300)*100
if subject1<30 or subject2<30 or subject3<30:
    print("fail")
else:
    if per>=90:
        print("first")
    elif per>=60:
        print("second")
    elif per>=30:
          print("third")
    else:
            print("fail")
print(total)
print(per)
            
