#Create a program for a specified task - pizza delivery program
#Hy Vo      August 24 2017

def welcome(message): #function that greed the customer
  print(message)
  function_routine()

def customer_name(letters, length, error): #function that ask for name
  import re 
  global name
  while True:
    name = input("Please enter in your full name.")
    name = name.lower() #turn all characters lowercased
    if name == "": #check for no input value
      print(error)
      customer_name(letters, length, error) 
    elif not re.match("^[a-z]*$", name): #check if input value is not a letter
      print(letters)
      customer_name(letters, length, error)
    elif len(name) > 15 or len(name) < 2: #check if input value have the length of between 2 and 15 characters
      print(length)
      customer_name(letters, length, error)
    else: #break the loop when all criteria are met
      name = name.title() #captitalised the first character in a word
      break 
    return name

def customer_address(error): #function that ask for address
  global address
  while True:
    address = input("Please enter in your address.")
    if address == "": #check for no input value
      print(error)
      customer_address(error)
    else: #break the loop when all criteria are met
      break
    return address

def customer_contact_number(error): #function that ask for contact number
  global number
  while True:
    number = input("What is your contact number?")
    try: #check if number is integer value
      int(number) 
    except ValueError:
      try: #check if number is float value
        float(number) 
      except ValueError: #display the error message
        print(error)
        customer_contact_number(error)
    else: #break the loop when all criteria are met
      break
    return number

#create the regular and gourmet pizza list
regular_pizza_list = ["1) BBQ Italian Sausage - $8.50", "2) Beef and Mushroom - $8.50", "3) Ham and Apricot - $8.50", "4) Beef and Onion - $8.50", "5) Cheesy Garlic Pizza - $8.50", "6) Ham and Cheese - $8.50", "7) Hawaiian - $8.50"]
gourmet_pizza_list = ["8) Grilled Green and White Pizza - $13.50", "9) Asparagus & Potato Pizza - $13.50", "10) Cheeseburger Flatbread Pizza - $13.50", "11) Grilled Caprese Salad Pizza - $13.50", "12) Sunny Side Up Pizza - $13.50", "13) Pizza Cubano - $13.50"]

def pizza_number(error, limit): #function that ask for the amount of pizza the customer want to order
  while True:
    global number_of_pizza
    try:
      number_of_pizza = int(input("How many pizza would you like to order? You can only have 5 pizzas per order."))
    except ValueError: #check for other input type
      print(error)
      continue

    else: #break the loop when all criteria are met
      break
    return number_of_pizza
  if number_of_pizza >= 1 and number_of_pizza <= 5: #check if number of pizzz ordered is between 1 and 5
    print("We will present you with the pizza menu, pick {} of them according to your order.".format(number_of_pizza))

    print("Regular pizza:")
    for regular in regular_pizza_list: #print regular pizza in the regular pizza list
      print(regular)
      
    print("Gourmet pizza:")
    for gourmet in gourmet_pizza_list: #print gourmet pizza in the gourmet pizza list
      print(gourmet)
    
  elif number_of_pizza < 1 or number_of_pizza > 5: #check if number of pizza ordered is lower than 1 and more than 5
    print(limit)
    pizza_number(error, limit)

def type_of_pizza(limit, error): #function that let customer choose their pizza
  global price_per_pizza
  price_per_pizza = 0
  total_pizza_amount = number_of_pizza
  while total_pizza_amount > 0: #check if total amount of pizza is still more than 0
    try:
      choices = int(input("Pick {} of the pizza that you order. Type between 1 and 13 to get your pizza.".format(total_pizza_amount)))
      if choices < 1 or choices > 13: #check if the customer's choice is smaller than 1 and higher than 13
        print(limit)
      elif choices >= 1 and choices <= 13: #check if the customer's choice is between 1 and 13
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
      print(error)
  

pizza_ordered = [] #create an empty customer's pizza choice list

def amount_of_pizza(pizza_list): #funciton that reveal the pizza the customer have chosen
  print(pizza_list)
  if len(pizza_ordered) > 0: #the list shouldn't be empty when output
    for task in pizza_ordered: #print out the list of pizza that the customer had ordered
      print(task)
  

def order_options(error): #function that ask for the choice between have pizza delivered or pick up
  while True:
    global options #globalised options variable
    options = input("""Would you like to have a delivery or pick up order?:
    1) Delivery
    2) Pick up
    """)
    options = options.lower()
    if options == "1" or options == "delivery": #check if the customer chose delivery
      break
    elif options == "2"or options == "pick up": #check if the customer chose pick up
      break
    else: #stop the customer from enter in other than the required value
      print(error)
      order_options(error)
    return options #make sure that this function to stop

def pizza_costs(charge): #function that calculate the cost of all the pizza combined
  total_cost = price_per_pizza
  delivery_price = 0 #create delivery_price
  print("Here is the total cost for all of your pizza:")
  if options == "1" or options == "delivery": #add the addition delivery price when the order is delivery
    delivery_price += 3
    print("${:.2f}, with ${} delivery cost".format(delivery_price + total_cost, delivery_price))
  else: #only have the output of the cost of pick up order
    print("${:.2f}".format(total_cost))
  
    
def customer_checkout_info(info): #function that let customer check their delivery/pick up contact information
  print(info)
  if options == "1" or options == "delivery": #check if delivery option is chosen
    print("Name: {}.".format(name))
    print("Address: {}.".format(address))
    print("Number: {}.".format(number))
  else: #check for other chosen option
    print("Name: {}.".format(name))
  

def new_order(farewell, error):  #function that ask for input option to make new order or exit
  while True:
    global order
    order = input("""Would you like to start a new order or exit the program? Type 1 to create a new order and 2 to exit the program.
    1) New order
    2) Exit
    """)
    order = order.lower() 
    if order == "1" or order == "new order": #bring the customer back to the order options
      break
    elif order == "2" or order == "exit": #say thank you for good measure
      print(farewell) 
      break
    else: #make sure that a proper input is enter i
      print(error)
      new_order(farewell, error)
    return order

def function_routine(): #function that control the way all other functions in the program is called
  customer_name("Only letters are allowed in your name. Please retry.", "It's seem that your name is either too short or too long. Please retry.", "Everyone should have a name, right? Please retry.")
  customer_address("We can't send your pizza if there are no place to go. Please retry.")
  customer_contact_number("It either not a number or you haven't enter any value. Please retry.")
  pizza_number("We assume you are here for some pizza, correct? Please retry.", "Sorry, you can only order between 1 to 5 pizzas. Please retry.")
  type_of_pizza("Sorry, you can only type in between 1 and 13 designated on the menu. Please retry.", "Pick your favourite pizza. Don't worry, you have a moment to consider your option.")
  amount_of_pizza("Here is the list of pizza you have ordered:")
  order_options("Please pick an option that suitable for you.")
  pizza_costs("A $3 delivery charge has been added into your payment.")
  customer_checkout_info("Your contact details are:")
  new_order("Thank you for visiting Dream Pizzas.", "That wasn't an option. Please pick one of them.")
  if order == "1" or order == "new order": #check if the customer want to make a new order
    function_routine() #loop the function

#call function
welcome("Welcome to Dream Pizzas.")
