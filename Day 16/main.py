from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()

is_on = True

while is_on:
    choice = menu.get_items()
    answer = input(f"What would you like? {choice}: ").lower()
    if answer == 'off':
        is_on = False
    elif answer == 'report':
        money_machine.report()
        coffee_maker.report()
    else:
        drink = menu.find_drink(answer)
        if coffee_maker.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)





