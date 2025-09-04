#Create a program for a specified task - pizza delivery program
#Hy Vo      August 24 2017

def order_options(): #function that asks for the choice between have pizza delivered or pick up
  while True:
    global options #globalised options variable
    options = input("""Welcome to Dream Pizzas. Would you like to have a delivery or pick up order? Type 1 for Delivery and 2 for Pick up:
    1) Delivery
    2) Pick up
    """)
    if options == "1": 
      customer_delivery_name() #move to the next function
    elif options == "2":
      pickup_order()
    else: #stop the customer from enter in other than the required value
      print("Please pick an option that suitable for you.")
      order_options()
    return options #make sure that this function to stop

def customer_delivery_name(): #function that ask for the customer's name when they pick delivery option
  import re
  global delivery_name
  while True:
    delivery_name = input("Please enter in your full name.")
    delivery_name = delivery_name.lower()
    if not re.match("^[a-z]*$", delivery_name):
      print("Only letters are allowed in your name. Please retry.")
      customer_delivery_name()
    elif len(delivery_name) > 15:
      print("It's seem that your name is too long. Please retry.")
      customer_delivery_name()
    elif delivery_name == "": #reask the question when nothing is entered
      print("Everyone should have a name, right? Please retry.")
      customer_delivery_name()
    else: 
      customer_address()
    return delivery_name

def customer_address(): #function that as for the customer address
  global address
  while True:
    address = input("Please enter in your address.")
    if address == "":
      print("We can't send your pizza if there are no place to go. Please retry.")
      customer_address()
    else:
      customer_contact_number()
    return address

def customer_contact_number(): #function that asks the customer for their contact number
  global number
  delivery_price = 0 #create delivery_price
  while True:
    number = input("What is your contact number?")
    try:
      int(number) #check if number is integer value
    except ValueError:
      try:
        float(number) #check if number is float value
      except ValueError: #reask the question if number is a float value
        print("It either not a number or you haven't enter any value. Please retry.")
        customer_contact_number()
    else:
      print("A $3 delivery charge has been added into your payment.")
      delivery_price += 3 #add the addition cost for delivery order
      pizza_number()
    return number

def pickup_order(): #function that ask the customer for their name when choosing the pick up option
  global pickup_name
  while True:
    pickup_name = input("Please enter in your full name.")
    if pickup_name == "":
      print("Everyone should have a name, right? Please retry.")
      pickup_order()
    else:
      pizza_number()
    return pickup_name

#create the regular and gourmet pizza list
regular_pizza_list = ["1) BBQ Italian Sausage - $8.50", "2) Beef and Mushroom - $8.50", "3) Ham and Apricot - $8.50", "4) Beef and Onion - $8.50", "5) Cheesy Garlic Pizza - $8.50", "6) Ham and Cheese - $8.50", "7) Hawaiian - $8.50"]
gourmet_pizza_list = ["8) Grilled Green and White Pizza - $13.50", "9) Asparagus & Potato Pizza - $13.50", "10) Cheeseburger Flatbread Pizza - $13.50", "11) Grilled Caprese Salad Pizza - $13.50", "12) Sunny Side Up Pizza - $13.50", "13) Pizza Cubano - $13.50"]

def pizza_number(): #function that asks for the amount of pizza the customer want to order
  while True:
    global number_of_pizza
    try:
      number_of_pizza = int(input("How many pizza would you like to order? You can only have 5 pizzas per order."))
    except ValueError: #if any other value is entered
      print("We assume you are here for some pizza, correct? Please retry.")
      continue
    else: 
      break
    return number_of_pizza
  if number_of_pizza >= 1 and number_of_pizza <= 5: #shrink the amount of pizza available to order
    print("We will present you with the pizza menu, pick {} of them according to your order.".format(number_of_pizza))

    print("Regular pizza:")
    for regular in regular_pizza_list: #print regular in the regular pizza list
      print(regular)
      
    print("Gourmet pizza:")
    for gourmet in gourmet_pizza_list:
      print(gourmet)
    type_of_pizza()
  elif number_of_pizza < 1 or number_of_pizza > 5: #only allow customer to pick the certain amount of pizza
    print("Sorry, you can only order between 1 to 5 pizzas. Please retry.")
    pizza_number()

def type_of_pizza(): #function that let customer choose their pizza
  global price_per_pizza
  price_per_pizza = 0
  total_pizza_amount = number_of_pizza
  while total_pizza_amount > 0: #offer the choices when with the number of pizza ordered
    try:
      choices = int(input("Pick {} of the pizza that you order. Type between 1 and 13 to get your pizza.".format(total_pizza_amount)))
      if choices < 1 or choices > 13: #let the customer knows that they can only type in between 1 to 13
        print("Sorry, you can only type in between 1 and 13 designated on the menu. Please retry.")
      elif choices >= 1 and choices <= 13: #if the user have chose one of the pizza
        if choices == 1:
          total_pizza_amount -= 1 #decrease the amount of pizza the customer hava pick
          pizza_ordered.append(regular_pizza_list[0]) #add the customer's pizza option into their chosen option list
          price_per_pizza += 8.50 #add $8.50 (the cost of each regular pizza) to the total cost
        elif choices == 2:
          total_pizza_amount -= 1
          pizza_ordered.append(regular_pizza_list[1])
          price_per_pizza += 8.50
        elif choices == 3:
          total_pizza_amount -= 1
          pizza_ordered.append(regular_pizza_list[2])
          price_per_pizza += 8.50
        elif choices == 4:
          total_pizza_amount -= 1
          pizza_ordered.append(regular_pizza_list[3])
          price_per_pizza += 8.50
        elif choices == 5:
          total_pizza_amount -= 1
          pizza_ordered.append(regular_pizza_list[4])
          price_per_pizza += 8.50
        elif choices == 6:
          total_pizza_amount -= 1
          pizza_ordered.append(regular_pizza_list[5])
          price_per_pizza += 8.50
        elif choices == 7:
          total_pizza_amount -= 1
          pizza_ordered.append(regular_pizza_list[6])
          price_per_pizza += 8.50
        elif choices == 8:
          total_pizza_amount -= 1
          pizza_ordered.append(gourmet_pizza_list[0])
          price_per_pizza += 13.50 #add $13.50 (the cost of each gourmet pizza) to the total cost
        elif choices == 9:
          total_pizza_amount -= 1
          pizza_ordered.append(gourmet_pizza_list[1])
          price_per_pizza += 13.50
        elif choices == 10:
          total_pizza_amount -= 1
          pizza_ordered.append(gourmet_pizza_list[2])
          price_per_pizza += 13.50
        elif choices == 11:
          total_pizza_amount -= 1
          pizza_ordered.append(gourmet_pizza_list[3])
          price_per_pizza += 13.50
        elif choices == 12:
          total_pizza_amount -= 1
          pizza_ordered.append(gourmet_pizza_list[4])
          price_per_pizza += 13.50
        elif choices == 13:
          total_pizza_amount -= 1
          pizza_ordered.append(gourmet_pizza_list[5])
          price_per_pizza += 13.50
    except ValueError: #let customer knows that they have entered wrong or no value
      print("Pick your favourite pizza. Don't worry, you have a moment to consider your option.")
  amount_of_pizza()

pizza_ordered = [] #create an empty customer's pizza choice list

def amount_of_pizza(): #funciton that reveal the pizza the customer have chosen
  print("Here is the list of pizza you have ordered:")
  if len(pizza_ordered) > 0: #the list shouldn't be empty when output
    for task in pizza_ordered:
      print(task)
  pizza_costs()

def pizza_costs(): #function that calculate the cost of all the pizza combined
  total_cost = price_per_pizza
  print("Here is the total cost for all of your pizza:")
  if options == "1": #add the addition delivery price when the order is delivery
    print("${:.2f}".format(delivery_price + total_cost))
  else: #only have the output of the cost of pick up order
    print("${:.2f}".format(total_cost))
  customer_checkout_info()
    
def customer_checkout_info(): #function that let customer check their delivery/pick up contact information
  print("Your contact details are:")
  if options == "1": #use the customer's delivery info
    print("Name: {}.".format(delivery_name))
    print("Address: {}.".format(address))
    print("Number: {}.".format(number))
  else: #use the customer's pickup info if they choose for a pick up order
    print("Name: {}.".format(pickup_name))
  new_order()

def new_order():  #function that asks for input option to make new order or exit
  while True:
    global order
    order = input("""Would you like to start a new order or exit the program? Type 1 to create a new order and 2 to exit the program.
    1) New order
    2) Exit
    """)
    if order == "1": #bring the customer back to the order options
      order_options()
    elif order == "2": #say thank you for good measure
      print("Thank you for visiting Dream Pizzas.") 
      break
    else: #make sure that a proper input is enter i
      print("That wasn't an option. Please pick one of them.")
      new_order()
    return order

#call_function
order_options()


