# Menna Elgayar - Project1
# Due Monday, October 17th 
# The purpose of this program is to create a python program with price and option list for a hotel guest

#Hotel Marbella Price List


#Input and Assign values to the following variables; name, number of days, cost per night, tax.

name = str(input("Customer name: ")) # prompts user to enter their name

number_of_days = int(input("number of days: ")) # prompts user to enter number of days

cost_per_night = int(input("cost per night (100,125,150,200): ")) # prompts user to select price

cost = number_of_days * cost_per_night # calculates the cost for the stay

tax = 0.08 # tax value

taxes = cost * 0.08 # calculates taxes per night

total_charge = cost + taxes # calculates the total charge including tax


# output

print("Hotel Marbella")

print(name,":",number_of_days,"days at cost", cost_per_night) 

print("") #adds spacing

print("............... .................. ................") # displays seperation

print ("") #adds spacing

print("Tax Amount:",taxes) #displays tax 

print("Total charges:",total_charge) #displays total charges

print("Thank you for staying at Hotel Marbella") # displays thank you message



# Pseudocode for the program



