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
    "water": 1200,
    "milk": 1200,
    "coffee": 1200,
}


def check_resources(drink_ingredients):
    """Returns True when there are enough ingredients and False when there are not enough."""
    for item in drink_ingredients:
        if drink_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True


def process_coins():
    """Returns the calculated total from all inserted coins."""
    print("Please insert coins")
    total = int(input("How many quarters do you have?: ")) * 0.25
    total += int(input("How many dimes do you have?: ")) * 0.1
    total += int(input("How many nickels do you have?: ")) * 0.05
    total += int(input("How many pennies do you have?: ")) * 0.01
    return total


def is_transaction_successful(money_received, drink_cost):
    """Returns True when payment accepted or False when not."""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Change: ${change}")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough. Money refunded.")
        return False


def make_coffee(drink_name, drink_ingredients):
    """Deduct required ingredients from resources."""
    for item in drink_ingredients:
        resources[item] -= drink_ingredients[item]
    print(f"Here is your {drink_name}")


machine_is_on = True

while machine_is_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if choice == "off":
        machine_is_on = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        drink = MENU[choice]
        if check_resources(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])
