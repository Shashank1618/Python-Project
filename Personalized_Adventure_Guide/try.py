"""
Take an int value from user.
Keep on asking if wrong input is given
"""
def getValidNumber(prompt):
    while True:
        try:
            value=int(input(prompt))
            return value
        except ValueError:
            print("Invalid Input! Enter again")

print(getValidNumber("test"))