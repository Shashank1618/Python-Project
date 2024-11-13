 #list.append()
#list.insert()
'''

while true:
    name=input("Enter user name:")
    print("Enter marks separated by space")
    
marks=[]
for i in range(6):
    temp=int(input())
    marks.append(temp)

sum1=sum(marks)

avg=sum1/5

if(avg>=90):
    print("You got A Grade")
elif(avg>=80) and (avg<90):
    print("You got B Grade")
elif(avg>=70) and (avg<80):
    print("You got C Grade")
elif(avg>=60) and (avg<70):
    print("You got B Grade")
else:
    print("You failed in Exam")  '''

#sum() len()
#list comprehension: picking each value from l converting each value into inther and storingit into ans
#map: It is iterator(range is also iterator) i.e in order to print it we have to convert it into list otherwise it will print object
#l=marks.split()#['10','11','14']
#ans=[int(score) for score in l]

            #ans=map(int,l)
#l is the sequence
#for each value in l whose datatype is string it is passed into the integer function and then store it 
#into ans

names=[]
scores={}

def take_input():
    while True:
        temp_name=input("Enter name: ")
        temp_name.title()
        if temp_name=="Done":
            break
        else:
            names.append(temp_name)
            marks=input("Enter Marks sep by space: ").split()
            marks=list(map(int,marks))
            scores[temp_name]=marks
        print("------------------------------------------------------------------")

def avg(scores):
    return sum(scores)/len(scores)

def grade(avg):
    if(avg>=90):
        return 'A'
    elif(avg>=80) and (avg<90):
        return 'B'
    elif(avg>=70) and (avg<80):
        return 'C'
    elif(avg>=60) and (avg<70):
        return 'D'
    else:
        return 'Fail'

def output():
    for name in names:
        average=avg(scores[name])
        grading=grade(average)
        print(f"The grade of {name} is {grading}")

take_input()
output()