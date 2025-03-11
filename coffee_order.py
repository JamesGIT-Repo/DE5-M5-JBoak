### A simple Coffee ordering script ###
def check_quantity(input):
    try:
        quantity = int(input)
        return quantity > 0
    except ValueError:
        return False

name = input("What is your name")
order = input("What coffee would you like?")

while True:
    quantity = input("How many would you like?")

    if check_quantity(quantity):
        print(f"Hi {name}, your order of {quantity} {order}(s) is accepted and being made.")
        break
    else:
        print("Quantity entered is not valid. It has to be a positive integer.")
