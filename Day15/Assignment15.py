import Menu_coffee_shop as menu # type: ignore
water = 0
milk = 0
coffee = 0
amount_paid = 5
order = ""
this_is_nothing =None

is_machine_on = False
menu_drinks =menu.MENU


def what_are_you_paying_with(order):
    print("Please insert coins. ")
    quarters = float(input("how many quarters?: "))
    dimes = float(input("how many dimes?: "))
    nickles = float(input("how many nickles?: "))
    pennies = float(input("how many pennies?: "))
    total = (quarters*0.25) +(dimes*0.1)+(nickles*0.05)+(pennies*0.01)
    final_total = total - order
    
    return total,final_total

def setting_recources():
    resources = menu.resources
    water = resources["water"]
    milk = resources["milk"]
    coffee = resources["coffee"]
    
    return water, milk, coffee
  
def making_report():
    print(f"Water: {water}ml") 
    print(f" Milk: {milk}ml")
    print(f"Coffee: {coffee}g")
    print(f"Money: ${amount_paid}")


def check_recources(order,water,milk,coffee,amount_paid):
    
    if order != "espresso":
    
        if water < menu_drinks[order]["ingredients"]["water"]:
            print("The machine is out of water please comeback later")
            return water,milk, coffee
        elif milk < menu_drinks[order]["ingredients"]["milk"]:
            print("The machine is out of milk please comeback later")
            return water,milk, coffee
        elif coffee < menu_drinks[order]["ingredients"]["coffee"]:
            print("The machine is out of coffee please comeback later")
            return water,milk, coffee
        elif amount_paid >= menu_drinks[order]["cost"]:
            water -= menu_drinks[order]["ingredients"]["water"] 
            milk -= menu_drinks[order]["ingredients"]["milk"] 
            coffee -= menu_drinks[order]["ingredients"]["coffee"] 
            return water,milk, coffee
        else:
            print("Sorry that's not enough money. Money refunded.")
            return water,milk, coffee
    elif water < menu_drinks[order]["ingredients"]["water"] and order == "espresso":
        print("The machine is out of water please comeback later")
        return water, coffee
    elif coffee < menu_drinks[order]["ingredients"]["coffee"] and order == "espresso":
        print("The machine is out of coffee please comeback later")
        return water, coffee
    elif  amount_paid >= menu_drinks[order]["cost"] and order == "espresso":
        water -= menu_drinks[order]["ingredients"]["water"] 
        coffee -= menu_drinks[order]["ingredients"]["coffee"] 
        return water,coffee
    else:
        print("Sorry that's not enough money. Money refunded.")
        return water, coffee

def ordering():
    order = input("What would you like? (espresso/latte/cappuccino) ").lower()
    if order == "off":
        exit()
        
    if order == "report":
        making_report()
    elif order not in menu_drinks:
        print("please pick a valid option")


    return order
    
#making_report()
water, milk, coffee = setting_recources()

while not is_machine_on:
    order = ordering()

    
    if order in menu_drinks:
        if order != "espresso" and water > menu_drinks[order]["ingredients"]["water"] and milk > menu_drinks[order]["ingredients"]["milk"] and coffee > menu_drinks[order]["ingredients"]["coffee"]:
            amount_paid,left_over = what_are_you_paying_with(menu_drinks[order]["cost"])
            water,milk,coffee = check_recources(order,water,milk,coffee,amount_paid)
            if amount_paid > menu_drinks[order]["cost"]:
                print(f"Here is ${left_over:.2f} in change.")
                print(f"Here is your {order} ☕️. Enjoy!")
            
            
        elif order == "espresso" and water > menu_drinks[order]["ingredients"]["water"]  and coffee > menu_drinks[order]["ingredients"]["coffee"]:
            amount_paid,left_over = what_are_you_paying_with(menu_drinks[order]["cost"]) 
            water,coffee = check_recources(order,water,milk,coffee,amount_paid)
            if amount_paid > menu_drinks[order]["cost"]:
                print(f"Here is ${left_over:.2f} in change.")
            
                print(f"Here is your {order} ☕️. Enjoy!")
        else:
            water,milk,coffee = check_recources(order,water,milk,coffee,amount_paid)

        
