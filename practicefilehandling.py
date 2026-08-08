'''with open("practice.txt","w") as f:
    f.write("hi everyone\n we are learning file i/o\n")
    f.write("usin java.\n i like the program java")'''

#replace all ocurrences of java with python
'''with open("practice.txt","r") as f:
    data=f.read()
new_data=data.replace("java","python")
print(new_data)
#overwrite data
with open("practice.txt","w") as f:
    f.write(new_data)

#found the data
word="learning"
with open("practice.txt","r") as f:
    data=f.read()
    if(word in data):
        print("found")
    else:
        print("not found")
def checkfor_line():#check the learning word blongs to  line 
    word="learning"
    data=True
    line_no=1
    with open("practice.txt","r") as f:
        while data:
            data=f.readline()
            if(word in data):
                print(line_no)
                return
            line_no +=1    
    return -1
checkfor_line()'''
#containing no seprate by comma, print the cunt even no
count=0
with open("practice1.txt","r")as f:
    data=f.read()
    #print(data)
    '''num=""
    for i in range(len(data)):
        if(data[i]==","):
            print(int(num))
            num=""
        else:
            num +=data[i] '''
    #another way
    nums=data.split(",")
    for val in nums:
        if(int(val)%2==0):
            count +=1
print(count)               

