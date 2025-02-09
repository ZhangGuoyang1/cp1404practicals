"""
<Pseudocode:>
function main()
    get number_of_items as integer
    while number_of_items < 0
        print "Invalid number of items!"
        get number_of_items as integer

    total_price = 0
    for i from 1 to number_of_items
        get price_of_item as float
        while price_of_item < 0
            print "Invalid price! Please enter a positive value."
            get price_of_item as float
        total_price = total_price + price_of_item

    if total_price > 100
        total_price = total_price * 0.9

    print "Total price for", number_of_items, "items is", total_price formatted to 2 decimal places

"""


def main():
    number_of_items = int(input("Number of items: "))
    while number_of_items < 0:
        print("Invalid number of items!")
        number_of_items = int(input("Number of items: "))
    total_price = 0
    for i in range(number_of_items):
        price_of_item = float(input(f"Price of item {i + 1}: "))
        while price_of_item < 0:
            print("Invalid price! Please enter a positive value.")
            price_of_item = float(input(f"Price of item {i + 1}: "))
        total_price += price_of_item
    if total_price > 100:
        total_price *= 0.9
    print(f"Total price for {number_of_items} items is ${total_price:.2f}")


if __name__ == "__main__":
    main()


