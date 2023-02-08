import pprint

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
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

money = 0.00
more_coffee = True


def report():
    print("Water: " + str(resources["water"]) + "ml")
    print("Milk: " + str(resources["milk"])+ "ml")
    print("Coffee: " + str(resources["coffee"])+ "g")
    print("Money: $" + str(round(money, 2)))


def make_coffee( desired_item, resources):
    global MENU
    global money
    if desired_item == "latte":
        if resources["water"] >= MENU[desired_item]["ingredients"]["water"]:
            if resources["milk"] >= MENU[desired_item]["ingredients"]["milk"]:
                if resources["coffee"] >= MENU[desired_item]["ingredients"]["coffee"]:
                    resources["water"] -= MENU[desired_item]["ingredients"]["water"]
                    resources["milk"] -= MENU[desired_item]["ingredients"]["milk"]
                    resources["coffee"] -= MENU[desired_item]["ingredients"]["coffee"]
                    money += calculate_money(desired_item)
                    print("Here is your latte! Enjoy!")
                    return (resources)
                else:
                    print("Sorry there is not enough coffee.")
                    return()
            else:
                print("Sorry there is not enough milk.")
                return()
        else:
            print("Sorry there is not enough water.")
            return()
    if desired_item == "cappuccino":
        if resources["water"] >= MENU[desired_item]["ingredients"]["water"]:
            if resources["milk"] >= MENU[desired_item]["ingredients"]["milk"]:
                if resources["coffee"] >= MENU[desired_item]["ingredients"]["coffee"]:
                    resources["water"] -= MENU[desired_item]["ingredients"]["water"]
                    resources["milk"] -= MENU[desired_item]["ingredients"]["milk"]
                    resources["coffee"] -= MENU[desired_item]["ingredients"]["coffee"]
                    money += calculate_money(desired_item)
                    print("Here is your cappuccino! Enjoy!")
                    return (resources)
                else:
                    print("Sorry there is not enough coffee.")
                    return ()
            else:
                print("Sorry there is not enough milk.")
                return ()
        else:
            print("Sorry there is not enough water.")
            return ()
    if desired_item == "espresso":
        if resources["water"] >= MENU[desired_item]["ingredients"]["water"]:
            if resources["coffee"] >= MENU[desired_item]["ingredients"]["coffee"]:
                resources["water"] -= MENU[desired_item]["ingredients"]["water"]
                resources["coffee"] -= MENU[desired_item]["ingredients"]["coffee"]
                print("Here is your espresso! Enjoy!")
                money += calculate_money(desired_item)
                return (resources)
            else:
                print("Sorry there is not enough coffee.")
                return ()
        else:
            print("Sorry there is not enough water.")
            return ()



def calculate_money(desired_item):
    global MENU
    customers_change = 0.00
    print("Please insert coins: \n")
    quarters = float(input("How many quarters: "))
    dimes = float(input("How many dimes: "))
    nickels = float(input("How many nickels: "))
    pennies = float(input("How many pennies: "))
    customers_change = (quarters * .25) + (dimes * .10) + (nickels * .05) + (pennies * .01)
    if customers_change < MENU[desired_item]["cost"]:
        print("Amount given is less than the amount needed. Please insert more change.")
        calculate_money(desired_item)
    else:
        customers_change -= MENU[desired_item]["cost"]
        print("Here is your $" + str(round(customers_change, 2)))
        return(float(MENU[desired_item]["cost"]))


while more_coffee:
    desired_item = input("What would you like? (Espresso,Latte,Cappuccino): ")
    if desired_item.lower() == "report":
        report()
    elif desired_item.lower() == "off":
        print("Thanks for getting your coffee from us. Have a great day!")
        more_coffee = False
    elif desired_item.lower() == "espresso" or desired_item.lower() == "latte" or desired_item.lower() == "cappuccino":
        make_coffee(desired_item, resources)
    else:
        print("Please select from one of the listed items")