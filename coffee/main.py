# makes  3 hit flavours
# espresso 50ml water 18g coffee beans price = 1.50
# latte 200ml water 150ml milk 24g coffee beans price = 2.50
# cappuccino 250ml water 150ml milk 24g coffee beans price = 3.00


MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 500,
    "milk": 200,
    "coffee": 100,
}


def check_resources(order):
    for resource in MENU[order]["ingredients"]:
        if resources[resource] < MENU[order]["ingredients"][resource]:
            print("Sorry, not enough {}".format(resource))
            return False
    return True


def process_coins():
    add_coins = True
    while add_coins:
        if input("Would you like to add coins? (y/n)") == "y":
            print("You can pay using, quarters, dimes, nickels, and pennies")
            quarters = int(input("How many quarters?"))
            dimes = int(input("How many dimes?"))
            nickels = int(input("How many nickels?"))
            pennies = int(input("How many pennies"))
            total_coins = round(
                (quarters * .25 + dimes * .10 + nickels * .05 + pennies * .01), 2)
            print("You have added ${} ".format(total_coins))
            add_coins = False
            return total_coins

        else:
            s
            print("Thank you for your business")
            add_coins = False


def order_coffee():
    order = input("What would you like? (espresso/latte/cappuccino):")
    if check_resources(order):
        print(f"Your {order} will cost ${MENU[order]['cost']}")
        cash = process_coins()
        if cash >= MENU[order]['cost']:
            for resource in MENU[order]["ingredients"]:
                resources[resource] -= MENU[order]["ingredients"][resource]
            if cash - MENU[order]['cost'] > 0:
                change = cash - MENU[order]['cost']
                print("Your change is ${}".format(change))
            print("Enjoy your coffee!")
        else:
            print("You didn't add enough money")


order_coffee()
