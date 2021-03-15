from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


my_money_machine = MoneyMachine()
my_coffe_maker = CoffeeMaker()
my_menu = Menu()
order_selected = "mola"
while order_selected != "off":
  
  options = my_menu.get_items()
  order_selected = input(f"What would you like ({options}): ")
  
  if ( order_selected == "off"):
    
    print("machine off")
          
  elif (order_selected == "report"):
     
      current_resources.report()
     
  elif( order_selected in options):
    
    print("working")
    
    customer_choice = my_menu.find_drink(order_selected)
    can_i_order = my_coffe_maker.is_resource_sufficient(customer_choice)
    if( can_i_order == true):
      
      my_coffe_maker.make_coffee(customer_choice)
      
    else:
      print("there isn't enought ingredients")
    
    
  else:
    print("try again")  
  

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

print(a) = menu.menu.name

is_on = True

while is_on:
    options = menu.get_items()
    choice = input(f"What would you like? ({options}): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
      choice = "latte"
        drink = menu.find_drink(choice)
       
        
        is_enough_ingredients = coffee_maker.is_resource_sufficient(drink)
        is_payment_successful = money_machine.make_payment(drink.cost)
        if is_enough_ingredients and is_payment_successful:
            coffee_maker.make_coffee(drink)




