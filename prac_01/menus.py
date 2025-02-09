"""
<Pseudocode:>
function main()
    get name
    menu = "(H)ello\n(G)oodbye\n(Q)uit"
    print menu
    get choice as uppercase input
    while choice is not "Q"
        if choice is "H"
            print "Hello" followed by name
        else if choice is "G"
            print "Goodbye" followed by name
        else
            print "Invalid choice"
        print menu
        get choice as uppercase input
    print "Finished"
"""


def main():
    name = input("Enter name: ")
    menu = "(H)ello\n(G)oodbye\n(Q)uit"
    print(menu)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "H":
            print(f"Hello {name}")
        elif choice == "G":
            print(f"Goodbye {name}")
        else:
            print("Invalid choice")
        print(menu)
        choice = input(">>> ").upper()
    print("Finished.")


if __name__ == "__main__":
    main()
