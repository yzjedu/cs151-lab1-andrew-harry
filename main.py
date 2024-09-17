# Programmers: Andrew Leimbach & Harry Li
# Course:  CS151, Dr. Zee
# Due Date: 9/18/2024
# Lab Assignment: 1
# Problem Statement: This task calculates and displays the price of gas, given total miles, miles per gallon, and gas price per gallon.
# Data In: User enters the number of miles traveling, the miles per gallon their vehicle has, and the gas price per gallon.
# Data Out: The gas price will be outputted for user to see.
# Credits: Class assignment

miles_traveling = float(input('Enter miles traveling : '))
miles_per_gallon = float(input('Enter miles per gallon for the vehicle : '))
gas_price_per_gallon = float(input('Enter gas price per gallon for the vehicle : '))

gas_price = (miles_traveling / miles_per_gallon) * gas_price_per_gallon

print(f"Your gas price for the trip: ${gas_price:.2f}")