import imp
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


# clear the screen
def clear():
    import os
    os.system('cls' if os.name == 'nt' else 'clear')


is_on = True

while is_on:
    print("Welcome to the Coffee Maker!")
    print("1. Make a coffee")
    print("2. Check the coffee maker's resources")
    print("3. Check the money machine's profit")
    print("4. Exit")
    choice = input("What would you like to do? ")
    if choice == "1":
        menu = Menu()
        print(menu.get_items())
        order_name = input("What would you like to order? ")
        order = menu.find_drink(order_name)
        if order:
            coffee_maker = CoffeeMaker()
            if coffee_maker.is_resource_sufficient(order):
                money_machine = MoneyMachine()
                if money_machine.make_payment(order.cost):
                    coffee_maker.make_coffee(order)
                else:
                    print("Sorry that's not enough money. Money refunded.")
            else:
                print("Sorry, we can't make that.")
        else:
            print("Sorry, that item is not available.")
    elif choice == "2":
        coffee_maker = CoffeeMaker()
        coffee_maker.report()
    elif choice == "3":
        money_machine = MoneyMachine()
        money_machine.report()
    elif choice == "4":
        is_on = False
    else:
        print("Sorry, that is not a valid option.")
    clear()
