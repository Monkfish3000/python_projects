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

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def is_resource_sufficient(order_ings):
    """determines if there is enough of each ingredient to make user drink selection"""
    for ing in order_ings:
        if order_ings[ing] >= resources[ing]:
            print(f"Sorry, selection sold out. Not enough {ing}")
            return False
    return True


def is_transaction_successful(money_inserted, cost_of_drink):
    """checks if money inserted is sufficient for selected drink"""
    if money_inserted >= cost_of_drink:
        change = round(money_inserted - cost_of_drink, 2)
        print(f"Here is your change: ${change}.")
        global profit
        profit += cost_of_drink
        return True
    else:
        print("Sorry, you have not inserted enough money.")
        return False


def make_coffee(drink_name, order_ingredients):
    """calculates new amount of resources"""
    for ing in order_ingredients:
        resources[ing] -= order_ingredients[ing]
    print(f"Here is your {drink_name} ☕️")


def process_coins():
    """returns amount based on coins inserted"""
    print("Insert coins")
    total = int(input("How many quarters?: ")) * 0.25
    total += int(input("How many dimes?: ")) * 0.1
    total += int(input("How many nickels?: ")) * 0.05
    total += int(input("How many pennies?: ")) * 0.01
    return total

is_on = True

while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice == 'off':
        is_on = False
    elif choice == 'report':
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        drink = MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            total_amount_inserted = process_coins()
            if is_transaction_successful(total_amount_inserted, drink["cost"]):
                make_coffee(choice, drink["ingredients"])






