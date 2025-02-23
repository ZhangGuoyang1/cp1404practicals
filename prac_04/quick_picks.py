"""
function generate_quick_pick()
    initialize empty set quick_pick
    while size of quick_pick is less than NUMBERS_PER_PICK
        generate a random number between MIN_NUMBER and MAX_NUMBER
        add the number to quick_pick

    return sorted quick_pick as a list

function main()
    ask user "How many quick picks?"
    get user input as num_picks

    for i from 1 to num_picks
        call generate_quick_pick and store result in quick_pick
        print each number in quick_pick in a formatted manner (aligned)

if the program is executed as the main program
    call main

"""

import random

# Constants
MIN_NUMBER = 1
MAX_NUMBER = 45
NUMBERS_PER_PICK = 6


# Function to generate a quick pick line
def generate_quick_pick():
    # Create a set of random numbers (to ensure no duplicates)
    quick_pick = set()
    while len(quick_pick) < NUMBERS_PER_PICK:
        quick_pick.add(random.randint(MIN_NUMBER, MAX_NUMBER))

    # Return the sorted list of numbers
    return sorted(quick_pick)


# Main program
def main():
    # Ask the user how many quick picks they want
    num_picks = int(input("How many quick picks? "))

    # Generate and display the quick picks
    for _ in range(num_picks):
        quick_pick = generate_quick_pick()
        # Print the numbers in the correct format (aligned)
        print(" ".join(f"{num:2}" for num in quick_pick))


if __name__ == "__main__":
    main()
