# Coffee Machine
# In this project, you will code a coffee machine simulator. The machine works with typical products: coffee, milk, and sugar, which you’ll order in the console. The machine has a limited supply of each product, and once you order a drink, the coffee machine will print the remaining supplies.

# The coffee machine has the following properties:
# - Money: the coffee machine has $0.50
# - Water: the coffee machine has 300ml of water
# - Milk: the coffee machine has 200ml of milk
# - Coffee: the coffee machine has 100g of coffee
# - Sugar: the coffee machine has 100g of sugar
# - Cups: the coffee machine has 9 cups
# - The coffee machine can make the following drinks:
# - Espresso:
# - Latte: requires 200ml of water, 150ml of milk, and 1g of coffee

from menu import MENU

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "sugar": 100,
    "cups": 9,
}
money = 0


def report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Sugar: {resources['sugar']}g")
    print(f"Cups: {resources['cups']}")
    print(f"Money: ${money}")


def check_resources(drink):
    for item in drink["ingredients"]:
        if drink["ingredients"][item] > resources[item]:
            print(f"Sorry, there is not enough {item}.")
            return False
    return True


def make_coffee(drink_name, drink):
    for item in drink["ingredients"]:
        resources[item] -= drink["ingredients"][item]
    print(f"Here is your {drink_name} ☕️. Enjoy!")


def process_coins():
    """Process the coins inserted by the user."""
    print("Please insert coins.")
    total = int(input("How many quarters? ")) * 0.25
    total += int(input("How many dimes? ")) * 0.10
    total += int(input("How many nickels? ")) * 0.05
    total += int(input("How many pennies? ")) * 0.01
    return total


def is_transaction_successful(money_received, drink_cost):
    """Check if the transaction is successful."""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change.")
        global money
        money += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def refill_resources():
    """Refill the resources of the coffee machine."""
    resources["water"] += 300
    resources["milk"] += 200
    resources["coffee"] += 100
    resources["sugar"] += 100
    resources["cups"] += 9

    print("Resources refilled successfully.")


def coffee_machine():
    """Main function to run the coffee machine."""
    is_on = True
    while is_on:
        choice = input("What would you like? (espresso/latte/cappuccino): ")
        if choice == "off":
            is_on = False
        elif choice == "report":
            report()
        elif choice == "refill":
            refill_resources()
        elif choice in MENU:
            if check_resources(MENU[choice]):
                payment = process_coins()
                if is_transaction_successful(payment, MENU[choice]["cost"]):
                    make_coffee(choice, MENU[choice])
        else:
            print("Invalid choice. Please try again.")


coffee_machine()
