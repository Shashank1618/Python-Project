#Menu of Restaurant

menu={
    'coffee':30,
    'pizza':100,
    'pasta':40,
    'salad':20,
    'burger':50,
    'fries':30,
    'drinks':15
}

print("\nWelcome to Apna Cafe and Restaurant\n")
print("Menu List")

print("Coffee:30 \nPizza: Rs100\nPasta: Rs40\nSalad: Rs20\nBurger: Rs50\nFries: Rs30\nDrinks: Rs15")
print()

total_cost=0
item=input("Please select your choice of food and drinks from the menu list :").lower().strip()

if item in menu:
    total_cost+=menu[item]
    print(f"Your item '{item}' has been added to your order.")
    
else:
    print("Sorry, this item is not available")


while True:
    another_item=input("Do you want to add another item in your order? (y/n) :").lower()
    if another_item=='y':
        item2=input("Please select another item:").lower().strip()
        if item2 in menu:
            total_cost+=menu[item2]
            print(f"Your item '{item2}' has added to order")
        else:
            print("Sorry, item is not available")
    
    elif another_item=='n':
        break
    else:
        print("Invalid Choice, Please input y or n")

print("Your total payable amount :Rs" , total_cost)




