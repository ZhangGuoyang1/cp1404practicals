"""
CP1404/CP5632 - Practical
Capitalist Conrad wants a stock price simulator for a volatile stock.
The price starts off at $10.00, and, at the end of every day there is
a 50% chance it increases by 0 to 10%, and
a 50% chance that it decreases by 0 to 5%.
If the price rises above $1000, or falls below $0.01, the program should end.
The price should be displayed to the nearest cent (e.g. $33.59, not $33.5918232901)
"""

"""
DEFINE MAX_INCREASE = 0.175 
DEFINE MAX_DECREASE = 0.05   
DEFINE MIN_PRICE = 1.00      
DEFINE MAX_PRICE = 100.00   
DEFINE INITIAL_PRICE = 10.00
DEFINE FILENAME = "stock_price_simulation.txt"

SET price = INITIAL_PRICE
SET number_of_days = 0

open FILENAME as out_file for writing

print "Starting price: $" + format price to 2 decimal places to out_file

while MIN_PRICE <= price <= MAX_PRICE
    number_of_days += 1
    SET price_change = 0
    
    if random integer between 1 and 2 is 1
        price_change = random floating-point number between 0 and MAX_INCREASE
    else
        price_change = random floating-point number between -MAX_DECREASE and 0

    price = price * (1 + price_change)
    print "On day " + number_of_days + " price is: $" + format price to 2 decimal places to out_file

close out_file


"""
import random

MAX_INCREASE = 0.175  # 17.5%
MAX_DECREASE = 0.05  # 5%
MIN_PRICE = 1.00  # Minimum price of $1
MAX_PRICE = 100.00  # Maximum price of $100
INITIAL_PRICE = 10.00
FILENAME = "stock_price_simulation.txt"

# Initialize variables
price = INITIAL_PRICE
number_of_days = 0

# Open file for writing output
out_file = open(FILENAME, 'w')

# Write the starting price to the file
print(f"Starting price: ${price:,.2f}", file=out_file)

# Simulate the stock price changes
while MIN_PRICE <= price <= MAX_PRICE:
    number_of_days += 1
    price_change = 0
    # generate a random integer of 1 or 2
    # if it's 1, the price increases, otherwise it decreases
    if random.randint(1, 2) == 1:
        # generate a random floating-point number between 0 and MAX_INCREASE
        price_change = random.uniform(0, MAX_INCREASE)
    else:
        # generate a random floating-point number between negative MAX_DECREASE and 0
        price_change = random.uniform(-MAX_DECREASE, 0)

    # Update the price
    price *= (1 + price_change)

    # Write the day and price to the file
    print(f"On day {number_of_days} price is: ${price:,.2f}", file=out_file)

# Close the file
out_file.close()
