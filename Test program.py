global customer_order
customer_order = []
global customer_price
customer_price = []
global delivery_charge
delivery_charge = 3
def customer_info():
  print("Welcome to Dream Pizza")
  global user_name
  user_name = input("What's your name?")
  global user_delivery
  user_delivery = input("Would you like your pizza delivered?")

  if user_delivery.lower() == "yes":
    global user_address
    user_address = input("What is your address?")
    global user_number
    user_number = input("What is your phone number?")
    global customer_price
    customer_price.append(delivery_charge)
  else:
    del customer_price[:]

def customer_order():
  global pizza_menu_regular
  pizza_menu_regular = ["Ham & Cheese", "Hawaiian", "Meatlovers", "Pepperoni", "Vegetarian", "Cheesy"]
  global pizza_menu_gourmet
  pizza_menu_gourmet = ["Chicken & Cranberry", "BBQ Chicken & Bacon", "Butter Chicken Pizza", "Seafood Deluxe", "Chicken Satay Pizza", "Smoked Salmon Pizza"]
  global regular_pizza
  regular_pizza = 8.50
  global gourmet_pizza
  gourmet_pizza = 13.50
  global user_input
  while True:
    user_input = input("""What would you like to order?
Pleae type the number which that pizza represents
Regular Pizzas
 1) Ham & Cheese - $8.50
 2) Hawaiian - $8.50
 3) Meatlovers - $8.50
 4) Pepperoni - $8.50
 5) Vegetarian - $8.50
 6) Cheesy - $8.50
 Gourmet Pizzas
 7) Chicken & Cranberry - $13.50
 8) BBQ Chicken & Bacon - $13.50
 9) Butter Chicken Pizza - $13.50
 10) Seafood Deluxe - $13.50
 11) Chicken Satay Pizza - $13.50
 12) Smoked Salmon Pizza - $13.50
 When finished type 'end' to complete order""")
    if user_input == "1":
      customer_order.append(pizza_menu_regular[0])
      customer_price.append(regular_pizza)
    if user_input == "2":
      customer_order.append(pizza_menu_regular[1])
      customer_price.append(regular_pizza)
    if user_input == "3":
      customer_order.append(pizza_menu_regular[2])
      customer_price.append(regular_pizza)
    if user_input == "4":
      customer_order.append(pizza_menu_regular[3])
      customer_price.append(regular_pizza)
    if user_input == "5":
      customer_order.append(pizza_menu_regular[4])
      customer_price.append(regular_pizza)
    if user_input == "6":
      customer_order.append(pizza_menu_regular[5])
      customer_price.append(regular_pizza)
    if user_input == "7":
      customer_order.append(pizza_menu_gourmet[0])
      customer_price.append(gourmet_pizza)
    if user_input == "8":
      customer_order.append(pizza_menu_gourmet[1])
      customer_price.append(gourmet_pizza)
    if user_input == "9":
      customer_order.append(pizza_menu_gourmet[2])
      customer_price.append(gourmet_pizza)
    if user_input == "10":
      customer_order.append(pizza_menu_gourmet[3])
      customer_price.append(gourmet_pizza)
    if user_input == "11":
      customer_order.append(pizza_menu_gourmet[4])
      customer_price.append(gourmet_pizza)
    if user_input == "12":
      customer_order.append(pizza_menu_gourmet[5])
      customer_price.append(gourmet_pizza)
    if user_input.lower() == "end":
      break

def customer_order_display():
  if user_delivery.lower() == "yes":
    print("Your order has been placed")
    print("Name: {}".format(user_name))
    print("Method: Delivery")
    print("Address: {}".format(user_address))
    print("Phone Number: {}".format(user_number))
    print("Customer's order: {}".format(customer_order))
    print("Total Price: ${:.2f}".format(sum(customer_price)))

  if user_delivery.lower() == "no":
    print("Your order has been placed")
    print("Name: {}".format(user_name))
    print("Method: Pick Up")
    print("Customer's order: {}".format(customer_order))
    print("Total Price: ${:.2f}".format(sum(customer_price)))
  return

customer_info()
customer_order()
customer_order_display()
