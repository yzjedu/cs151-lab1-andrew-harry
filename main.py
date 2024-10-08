# Programmers: Andrew Leimbach & Harry Li
# Course:  CS151, Dr. Zee
# Due Date: 9/18/2024
# Lab Assignment: 1
# Problem Statement: This task calculates and displays the price of gas, given total miles, miles per gallon, and gas price per gallon.
# Data In: The user enters the number of miles traveling, the miles per gallon their vehicle has, and the gas price per gallon.
# Data Out: The gas price will be outputted for the user to see.
# Credits: Class assignment

# Stores the user input as a variable under miles_traveling
miles_traveling = float(input('Enter miles traveling : ')) 

# Stores the user input as a variable under miles_per_gallon
miles_per_gallon = float(input('Enter miles per gallon for the vehicle : '))  

# Stores the user input as a variable under gas_price_per_gallon
gas_price_per_gallon = float(input('Enter gas price per gallon for the vehicle : ')) 

# Calculates the gas price and stores it in variable gas_price
gas_price = (miles_traveling / miles_per_gallon) * gas_price_per_gallon 


print(f"Your gas price for the trip: ${gas_price:.2f}") #Outputs a message displaying the gas price
