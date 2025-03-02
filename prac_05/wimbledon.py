"""
Word Occurrences
Estimate: 30 minutes
Actual:   41 minutes
"""

"""
function main()
    set filename to '/mnt/data/wimbledon.csv'  # The file path
    call read_file function with filename and store the results in champions_dict and countries_set

    call display_champions with champions_dict
    call display_countries with countries_set


function display_champions(champions_dict)
    print "Wimbledon Champions: "
    for each player, wins in sorted champions_dict
        print player and wins


function display_countries(countries_set)
    print "\nThese countries have won Wimbledon: "
    sort countries_set into sorted_countries
    print sorted_countries as a comma-separated string


function read_file(filename)
    create an empty dictionary champions_dict to store player names and their win counts
    create an empty set countries_set to store the countries

    open the file at the given filename with encoding 'utf-8-sig'
    create a CSV reader for the file
    skip the header row

    for each row in the file:
        get the winner's name from column 3 (row[2])
        get the winner's country from column 2 (row[1])

        if winner is already in champions_dict:
            increment their win count by 1
        else:
            add the winner to champions_dict with 1 win

        add the winner's country to countries_set

    return champions_dict and countries_set


if program is run as main
    call main function


"""


# Updated code with main function placed first

# Main function to orchestrate the solution
def main():
    filename = '/mnt/data/wimbledon.csv'  # The file path
    champions_dict, countries_set = read_file(filename)

    display_champions(champions_dict)
    display_countries(countries_set)


# Function to display champions and their win counts
def display_champions(champions_dict):
    print("Wimbledon Champions: ")
    for player, wins in sorted(champions_dict.items()):
        print(f"{player} {wins}")


# Function to display sorted list of countries that have won
def display_countries(countries_set):
    print("\nThese countries have won Wimbledon: ")
    sorted_countries = sorted(countries_set)
    print(", ".join(sorted_countries))


# Updated function to read the file and process data correctly
def read_file(filename):
    champions_dict = {}
    countries_set = set()

    with open(filename, "r", encoding="utf-8-sig") as in_file:
        reader = csv.reader(in_file)
        next(reader)  # Skip the header row
        for row in reader:
            winner = row[2]  # The winner's name is in column 3
            country = row[1]  # Winner's country is in column 2

            # Count the number of wins for each player
            if winner in champions_dict:
                champions_dict[winner] += 1
            else:
                champions_dict[winner] = 1

            # Add the winner's country to the set
            countries_set.add(country)

    return champions_dict, countries_set


# Re-running the program
main()
