class Items:
    def __init__(self,name,price,quantity):
        self.name=name
        self.price=price
        self.quantity=quantity
    
    def update(self,quantity):
        self.quantity=quantity
    def getname(self):
        return self.name            

    
    def displayItems(self):
        print(f'''Name  of Item: {self.name}\nPrice of Item: {self.price}\n1Quantity: {self.quantity}''')
   




#Creating an Inventory
#managing the inventory(list of items)
#Adding item
#Updating details
#Displaying inventory
#List Of objects


class Inventory:#To manage the multiple items,separate process  We can also add
    def __init__(self):
        self.items=[]

    def addItems(self, name,price,quantity):
        self.items.append(Items(name,price,quantity))

    def updateQuantity(self,items,quantity):
       
       # for i in self.items:
           # if(i.getname()==items):
            #   self.items[self.items.indexOf(i)]=quant
             #   print(i.displayItems())

    def displayItems(self):
        pass

inventory1=Inventory()
inventory2=Inventory()
inventory1.addItems("Pen",14,150)
inventory2.addItems("Pen",14,150)
inventory1.updateQuantity("Pen",2500)


#Can you write return statement in a constructor function

#name of the item
#if it exists in inventory
#inventory