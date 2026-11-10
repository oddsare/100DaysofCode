from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

is_game_on = False
menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()


while not is_game_on:
    order = input("What would you like? (espresso/latte/cappuccino/):  ")


    

    if order == "off":
        exit()
    elif order == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink =menu.find_drink(order)
        can_make = coffee_maker.is_resource_sufficient(drink)
        if can_make == True:
            
          
            total = money_machine.make_payment(drink.cost)
            if total == True:
                coffee_maker.make_coffee(drink)
           
    
