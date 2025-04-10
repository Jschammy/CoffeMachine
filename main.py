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

PROFIT = 0
RESOURCES = {
    "water": 1200,
    "milk": 1200,
    "coffee": 1200,
}


machine_on = True
menu_item = ""


def process_payment():
    """"Checks user payment against cost of beverage. Returns True if True, False if False."""
    price = MENU[menu_item]["cost"]
    print(f"Item price: ${price}")
    user_payment = 0
    user_payment += int(input("Please insert your quarters: ")) * 0.25
    user_payment += int(input("Please insert your dimes: ")) * 0.10
    user_payment += int(input("Please insert your nickels: ")) * 0.05
    user_payment += int(input("Please insert your pennies: ")) * 0.01
    user_payment = round(user_payment, 2)
    if user_payment >= price:
        print("Payment successful!")
        change = round(user_payment - price, 2)
        print(f"Your change is {change}")
        global PROFIT
        PROFIT += price
        return True
    else:
        print("Insufficient funds!")


def check_resources():
    """"Checks user drink choice ingredients against resources in coffee machine."""
    global RESOURCES
    ingredients = MENU[menu_item]["ingredients"]
    for ingredient in ingredients:
        if ingredients[ingredient] > RESOURCES[ingredient]:
            print(f"Insufficient resources: {ingredient}. Notify technician.")
            return False
        RESOURCES[ingredient] -= ingredients[ingredient]
    return True


while machine_on:

    user_input = input("Select a menu item (espresso, latte, cappuccino): ").lower()

    if user_input == "report":
        print(f"Total Profit: ${PROFIT}")
        print(RESOURCES)
    elif user_input == "off":
        machine_on = False
    elif user_input not in MENU.keys():
        print("Item not on menu. Please try again.")
    else:
        menu_item = user_input
        if check_resources():
            process_payment()