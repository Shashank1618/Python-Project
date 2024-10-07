def totalCost(budget,duration):
    return budget*duration


name=input("Hello User! Please Enter Your Name \n")

print(f"Hello {name.title()}, Welcome to Personalized Adventure Guide")
while True:
    try:
        destination=input("Where do you want to go ").strip().lower()
        if destination == "mountain":
            print("You are going to the mountain")
        elif destination == "beach":
            print("You are going to the beach")
        else:
            print("Enter the correct choice ")
            continue
        

        budget=int(input("Enter the budget : "))
        if budget >= 500:
            print("Luxury")
        elif budget >= 200:
            print("Good")
        elif budget > 0:
            print("Budget friendly")
        else:
            print("Invalid budget")
            continue
    
        days=int(input("Enter the number of days \n"))
        total=totalCost(budget,days)

        print(f"""
        days = {days} \n
        budget = {budget} \n
        total cost = {total}""")

        proceed = input("Do you want to plan another trip? (yes/no): ").strip().lower()
        if proceed != 'yes':
            print("Thank you for using the Personalized Adventure Guide!")
            break


    except  Exception as e:
        print("An error occurred: ", str(e))
