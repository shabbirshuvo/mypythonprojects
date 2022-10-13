from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu_obj = Menu()
coffee_maker_obj = CoffeeMaker()
money_machine_obj = MoneyMachine()

control = True
while control:
    menu_items = str(menu_obj.get_items())
    coffee_type_selection = input(f"Which coffee would you like? {menu_items}: ")
    if coffee_type_selection == "off":
        print("Welcome service team")
        break
    elif coffee_type_selection == "report":
        coffee_maker_obj.report()
        money_machine_obj.report()
    elif coffee_type_selection == "espresso" or coffee_type_selection == "latte" or coffee_type_selection == "cappuccino":

        items_of_the_order = menu_obj.find_drink(coffee_type_selection)
        if items_of_the_order is None:
            pass  # this block should never run unless there is logical error on the top
        else:
            if_have_sufficient_resources = coffee_maker_obj.is_resource_sufficient(items_of_the_order)
            # print(if_have_sufficient_resources)
            if if_have_sufficient_resources:
                # find cost of the item
                item_cost = items_of_the_order.cost
                # print(item_cost)

                # process coins and make payments
                if money_machine_obj.make_payment(item_cost):
                    coffee_maker_obj.make_coffee(items_of_the_order)
            else:
                pass
                # print("Sorry do not have enough resources")

    else:
        print("sorry wrong selection, select again")
