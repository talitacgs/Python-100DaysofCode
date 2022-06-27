from data import MENU, resources

money_machine = 0


def resources_sufficient(order_ingredients):
    # Return True if it is possible to make coffee and False if some ingredient is missing
    for item in order_ingredients:
        if resources[item] < order_ingredients[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True


def process_coins():
    # Return the total calculated from coins inserted by user
    print('Please insert coins!')
    quarters = int(input('how many quarters ?: ')) * 0.25
    dimes = int(input('how many dimes ?: ')) * 0.10
    nickles = int(input('how many nickles ?: ')) * 0.05
    pennies = int(input('how many pennies ?: ')) * 0.01
    money_user = quarters + dimes + nickles + pennies
    return money_user


def transaction_successful(money, coffee_cost):
    # Return True if coins inserted are enough and False if payment is insufficient
    if money >= coffee_cost['cost']:
        change = round(money - coffee_cost['cost'], 2)
        print(f'${change} dollars in change')
        global money_machine
        money_machine += coffee_cost['cost']
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def resources_report(answers, order_ingredients):
    # Deduct required ingredients from the resources
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f'Here is your {answers} ☕')


end_coffee = True

while end_coffee:
    answer = input('What would you like? (espresso/latte/cappuccino): ').lower()
    if answer == 'off':
        end_coffee = False
    elif answer == 'report':
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f'Money: $ {money_machine}')
    else:
        coffee = MENU[answer]
        if resources_sufficient(coffee['ingredients']):
            payment = process_coins()
            if transaction_successful(payment, coffee):
                resources_report(answer, coffee['ingredients'])
