"""
CP1404/CP5632 Practical
Starter code for cumulative total income program
"""

"""
function main()
    initialize an empty list incomes
    get num_months from user
    for month from 1 to num_months
        get income for month from user
        add income to incomes list
    call print_income_report with num_months and incomes as parameters

function print_income_report(num_months, incomes)
    print "Income Report"
    set total to 0
    for month from 1 to num_months
        set income to incomes[month - 1]
        add income to total
        print formatted report for month, income, and total

"""


def main():
    """Display income report for incomes over a given number of months."""
    incomes = []
    num_months = int(input("How many months? "))  # Renamed months to num_months

    for month in range(1, num_months + 1):
        income = float(input(f"Enter income for month {month}: "))  # f-string used here
        incomes.append(income)

    print_income_report(num_months, incomes)


def print_income_report(num_months, incomes):
    """This function will print the income report with cumulative totals."""
    print("\nIncome Report\n-------------")
    total = 0
    for month in range(1, num_months + 1):
        income = incomes[month - 1]
        total += income
        print(f"Month {month:2} - Income: ${income:10.2f}           Total: ${total:10.2f}")


main()

