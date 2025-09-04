currentBal = 100.0

print("Initial balance: $", currentBal)
print("Purchased 3 short tracks at 1.79")
print("Purchased 4 medium tracks at 2.5")
print("purchased 2 long tracks at 4.5")
short = 1.79 * 3
medium = 2.5 * 4
long = 4.5 * 2

purchasedBal = short + medium + long
finalBal = currentBal - purchasedBal
dollars = finalBal
print("Final balance: $", end = '')
print (dollars, end='')
print("")

