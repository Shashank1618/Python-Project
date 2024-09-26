def totalCost(budget,days):
    return budget*days

def getValidNumber(prompt):
    while True:
        try:
            value=input(prompt)
            return value
        except ValueError:
            print("Invalid Input! Enter again")

def destination(dest):
    dest=str(dest).lower().strip()
    if dest == "mountain":
        print("Oh! you are going for an adventure")
    elif dest == "beach":
        print("You are going to the Beach, the best place to heal")
    else:
        print("Enter the correct choice")

def Amount(budget):
    if budget >= 500:
        print("Luxury Budget")
    elif  budget >= 200:
        print("Good Budget")
    elif budget > 0:
        print("Budget friendly")
    else:
        print("Invalid budget")

def display(days,budget,total):
    print(f""" \nNo. of Days are : {days} \n
Your Budget was : {budget} \n
Your Total Expenditure will be : {total}""")


name=input("Hello User! Please Enter Your Name \n")
print(f"Hello {name.title()}, Welcome to Personalized Adventure Guide")
dest=getValidNumber("Where do you want to go : ")
destination(dest)
budget=int(getValidNumber("Enter the Budget : "))
Amount(budget)
days=int(getValidNumber("Enter the Number of days : "))
total=totalCost(budget,days)
display(days,budget,total)
