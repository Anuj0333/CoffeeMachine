# This is a sample Python script.
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
profit=0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
def is_resources_sufficient(order_ingredients):
    """return true when order can be made, false if ingredients are insufficient."""
    for i in order_ingredients:
        if order_ingredients[i]>=resources[i]:
            print(f"sorry there is not enough water{i}.")
            return False
    return True


def process_coins():
    """return the total calculated from coins inserted."""
    print("plz insert coins.")
    total=int(input("how many quarters??:"))*0.25
    total += int(input("how many dines?:")) * 0.10
    total += int(input("how many nickles?:")) * 0.05
    total += int(input("how many pennies?:")) * 0.01
    return total


def is_transaction_successful(money_received, drink_cost):
    """return when the payment is accepted, false is if money is insufficient ."""
    if money_received>=drink_cost:
        change=round(money_received-drink_cost,2)
        print(f"Here is ${change} in change.")
        global profit
        profit+= drink_cost
        return True
    else:
        print("sorry that's not enough money, Money refunded.")
        return False

def make_coffe(drink_name,order_ingredients):
    """deduct the required ingredients from the resources."""
    for i in order_ingredients:
        resources[i]-=order_ingredients[i]
    print(f"Here is your {drink_name} ")


is_on =True
while is_on:
    choice=input(" what whould you like? (espresso/latte/cappuccino): ")
    if choice =="off":
        is_on=False
    elif choice=="report":
        print(f"Water:{resources['water']}ml")
        print(f"Milk:{resources['milk']}ml")
        print(f"Coffee:{resources['coffee']}g")
        print(f"Money:${profit}")
    else:
        drink=MENU[choice]
        if is_resources_sufficient(drink["ingredients"] ) :
            payment= process_coins()
            if is_transaction_successful(payment,drink["cost"]):
                make_coffe(choice,drink["ingredients"])
