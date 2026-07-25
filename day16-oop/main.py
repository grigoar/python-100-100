# coffee machine project

# 1. print report
# 2. check resources sufficient
# 3. process coins
# 4. check transaction successful
# 5. make coffee


class CoffeeMachine:
    def __init__(self):
        self.resources = {
            "water": 300,
            "milk": 200,
            "coffee": 100,
        }
        self.profit = 0

    def report(self):
        print(f"Water: {self.resources['water']}ml")
        print(f"Milk: {self.resources['milk']}ml")
        print(f"Coffee: {self.resources['coffee']}g")
        print(f"Profit: ${self.profit}")

    def is_resource_sufficient(self, drink):
        for item in drink.ingredients:
            if drink.ingredients[item] > self.resources[item]:
                print(f"Sorry there is not enough {item}.")
                return False
        return True

    def process_coins(self):
        print("Please insert coins.")
        total = int(input("how many quarters? ")) * 0.25
        total += int(input("how many dimes? ")) * 0.10
        total += int(input("how many nickels? ")) * 0.05
        total += int(input("how many pennies? ")) * 0.01
        return total

    def is_transaction_successful(self, drink_cost):
        money_received = self.process_coins()
        if money_received >= drink_cost:
            change = round(money_received - drink_cost, 2)
            print(f"Here is ${change} in change.")
            self.profit += drink_cost
            return True
        print("Sorry that's not enough money. Money refunded.")
        return False

    def make_coffee(self, order):
        for item in order.ingredients:
            self.resources[item] -= order.ingredients[item]
        print(f"Here is your {order.name} ☕️. Enjoy!")


class Menu:
    def __init__(self):
        self.drinks = {
            "latte": {"water": 200, "milk": 150, "coffee": 24},
            "espresso": {"water": 50, "coffee": 18},
            "cappuccino": {"water": 250, "milk": 100, "coffee": 22},
        }

    def get_drink(self, name):
        return self.drinks[name]

    def is_resource_sufficient(self, drink):
        is_enough = True
        for item in drink.ingredients:
            if drink.ingredients[item] > coffee_machine.resources[item]:
                print(f"Sorry there is not enough {item}.")
                is_enough = False
        return is_enough


# Drink class
class Drink:
    def __init__(self, name, ingredients, cost):
        self.name = name
        self.ingredients = ingredients
        self.cost = cost

    def get_cost(self):
        return self.cost

    def get_name(self):
        return self.name

    def get_ingredients(self):
        return self.ingredients


# main program
coffee_machine = CoffeeMachine()
menu = Menu()

while True:
    choice = input("What would you like? (latte/espresso/cappuccino): ")
    if choice == "off":
        break
    elif choice == "report":
        coffee_machine.report()
    elif choice == "latte":
        drink = Drink("latte", {"water": 200, "milk": 150, "coffee": 24}, 2.50)
        if menu.is_resource_sufficient(drink):
            if coffee_machine.is_transaction_successful(drink.get_cost()):
                coffee_machine.make_coffee(drink)
