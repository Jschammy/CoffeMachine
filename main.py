import time

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


MACHINE_ON = True
drink = ""

def check_money(menu_item, money):
    price = MENU[menu_item]["cost"]
    print(f"Item price: ${price}")
    payment = 0
    payment += int(input("Please insert your quarters: ")) * 0.25
    payment += int(input("Please insert your dimes: ")) * 0.10
    payment += int(input("Please insert your nickels: ")) * 0.05
    payment += int(input("Please insert your pennies: ")) * 0.01
    if payment >= price:
        change = payment - price
        money += payment - change
        print("Payment successful...")
        time.sleep(2)
        return money
    else:
        print("Insufficient funds...")
        time.sleep(2)




#def check_resources():


def check_menu(menu_item):
    global MACHINE_ON
    menu_item = input("Select a menu item (espresso, latte, cappuccino): ").lower()

    if menu_item == "report":
        print(f"Total Profit: ${profit}")
    elif menu_item == "off":
        MACHINE_ON = False
    elif menu_item not in MENU.keys():
        print("Item not on menu. Please try again.")
        time.sleep(2)
    else:
        return menu_item


while MACHINE_ON:
    drink = check_menu(drink)
    check_money(drink, profit)
