# run report for coffee machine
MENU = \
{
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


# printing a report
print(f"Water: {resources['water']}ml")
print(f"Milk: {resources['milk']}ml")
print(f"Coffee: {resources['coffee']}g")

# check if enough water f-n
def water_check(order):
    if resources['water'] >= MENU[order]['ingredients']['water']:
        return True
    else:
        return False

# check if enough milk f-n
def milk_check(order):
    if resources['milk'] >= MENU[order]['ingredients']['milk']:
        return True
    else:
        return False

# check if enough milk f-n
def coffee_check(order):
    if resources['coffee'] >= MENU[order]['ingredients']['coffee']:
        return True
    else:
        return False

# def a function for prompting how many coins user wants to insert. Takes string as an argument - coin name
# f-n doesn't allow negative numbers or non int values.
def prompt_for_coin(coin):
    while True:
        try:
            num_coins = int(input(f"how many {coin}s? "))
        except ValueError:
            print('has to be a number')
            continue
        if num_coins >= 0:
            return num_coins
        else:
            print('enter a positive number')

while True:
    while True:
        order = input("What do you want: espresso/latte/cappuccino ")
        if order not in MENU.keys():
            continue
        else:
            break

    order_price = MENU[order]['cost']
    print("That'll cost: $", order_price)
    while True:
        # prompt for coins. pennies, nickels, dimes and quarters
        pennies = prompt_for_coin('penny')
        nickels = prompt_for_coin('nickel')
        dimes = prompt_for_coin('dime')
        quarters = prompt_for_coin('quarter')
        break    # get out of the while loop or else it'll keep prompting for pennies,nickels, etc

    amount = (pennies * 1 + nickels * 5 + dimes * 10 + quarters * 25) / 100

    # if not enough money for the drink, return to the beginning of the loop
    if amount < order_price:
        print('are you broke')
        continue    # goes back to the beginning of while loop

    # if the money is sufficient, continue with order
    else:
        if order == 'espresso':
            if water_check(order) and coffee_check(order):
                print("yeah we have everything, you'll get your drink")
                resources['water'] -= MENU[order]['ingredients']['water']
                resources['coffee'] -= MENU[order]['ingredients']['coffee']
            else:
                print('we are short on something dude')
        else:
            if water_check(order) and milk_check(order) and coffee_check(order):
                resources['water'] -= MENU[order]['ingredients']['water']
                resources['coffee'] -= MENU[order]['ingredients']['coffee']
                resources['milk'] -= MENU[order]['ingredients']['milk']
                print('yeah we have everything')
            else:
                print('we are short on something')

        print(resources)

    change = amount - order_price
    print("Here's your change ", change)






