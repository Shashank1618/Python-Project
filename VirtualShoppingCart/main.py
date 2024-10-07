def getQuantity():

def checkout(cart, prices):
    display(cart)
    total=totalCost(cart,prices)
    print(f'{total} before discount')
    total=applyDiscount(total)
    return total

def main():
    items=['Apples','Musambi','Aam']
    prices={'Apples':34,'Musambi':10,'Aam':45}
    cart={}
    print("Welcome to Shopping, select items")

    while True:
        print('Available items:')
        for ele in items:
            print(ele)

            