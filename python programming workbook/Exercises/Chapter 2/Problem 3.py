print("Initial price:")
diesel = "$1.47"
price95 = "$2.17"
price91 = "$2.06"
print("Diesel price", diesel)
print("95 price", price95)
print("91 unleaded price", price91)
print("")
print("Price increase of 10%:")

diesel = 1.47 / 100 * 10 + 1.47
dollars = diesel
print("Diesel price $", end = '')
print (dollars, end='')
print("")

price95 = 2.17 / 100 * 10 + 2.17
dollars = price95
print("95 price $", end = '')
print (dollars, end='')
print("")

price91 = 2.06 / 100 * 10 + 2.06
dollars = price91
print("91 price $", end = '')
print (dollars, end='')
print("")

