def getQuantity():
    while True:
        try:
            quantity = int(input("Enter the quantity of item: "))
            if quantity <= 0:
                print('Quantity must be positive.')
            else:
                return quantity
        except ValueError:
            print("Invalid quantity! Enter Again:")

def display(cart):
    print(cart)

def totalCost(cart, prices):
    tot_amount=0
    total=0
    for i in cart:
        for j in prices:
            if i==j:
                tot_amount=cart[i]
                total+=tot_amount*prices[j]
    return total

def applyDiscount(total):
    if total >=5000:
        print("Your Discount is 40%")
        total=(40/100)*total
    elif total >=3000:
        print("Your Discount is 20%")
        total=(20/100)*total
    elif total >=1000:
        print("Your Discount is 5%")
        total=(5/100)*total
    else:
        print("There is No Discount")
    return total

def checkout(cart, prices):
    display(cart)
    total = totalCost(cart, prices)
    display(f'{total} before discount')
    total = applyDiscount(total)
    return total

def main():
    items = ['Apples', 'Mosambi', 'Anar', 'Aam']
    prices = { 'Apples': 20, 'Anar': 33.5, 'Aam': 45.7, 'Anar': 40, 'Mosabmi': 22.8}

    cart = {}
    print("Welcome to the Virtual Shopping Cart!")
    print("Available items:")
    while True:
        for element in items:
            print(element)

        choice = input("Enter the item name or Done to finish").capitalize()
        if choice == 'Done':
            break
        elif choice in items:
            quantity = getQuantity()
            if choice in cart:
                cart[choice] = cart[choice] + quantity  # we can replace  it with cart.upadate({choice: (cart.getattr(choice) + quantity)})
                print(f'{choice} updated by {quantity}')
            else:
                cart[choice] = quantity
                print(f"{choice} added to cart!")
        else:
            print("Item not available.")
    if cart:
        print(f"The Price to be paid is {checkout(cart, prices)}")
    else:
        print("The cart is empty")

main()