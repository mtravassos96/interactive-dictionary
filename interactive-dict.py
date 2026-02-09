"""
Exercise from the course "Python 3 from Beginner to Expert - Learn Python from Scratch"
by Arkadiuz Włodarczyk
Chapter 6: Advanced Types

Write a program that will allow the user to:
    1) Add new definitions
    2) Search existing definitions
    3) Delete the definition that he has chosen


Features:
User Interface
    a) Add new definitions -> maybe try .update())
    b) Search existing definitions -> .get() to return a value
    c) Delete the definition that he has chosen -> .pop()
    d) Clear all -> .clear()
    e) "Exit" option
"""

# Auxiliary functions
## Checks and parses values str to int
def parse_input(value):
    if value.isdigit():
        return int(value)
    return value

## Displays dictionary
def show_dict(userDict):
    if userDict:
        print(f"Your dictionary:")
        for k, v in userDict.items():            
            print(f"{k}: {v}")
    else:
        print("Your dictionary is empty.")

## Adds key-value to dictionary
def add_definition(userDict):
    key = parse_input(input("Enter the key: "))
    value =  parse_input(input("Enter the value: "))
    userDict.update({key: value})
    print(f"Added {key}: {value}\n")

## Searches for value using a key
def search_definition(userDict):
    while True:
        key = parse_input(input("Inform the key: "))
        value = userDict.get(key)

        if value is not None:
            print(f"The value for {key} is {value}\n")
            break
        else:
            print(f"The key {key} isn't valid. Try again.\n")

## Delete key-value in dictionary
def del_definition(userDict):
    while True:
        key = parse_input(input("Inform the key: "))        

        try:
            value = userDict.pop(key)
            print(f"You deleted the value {value}\n")
            break
        except KeyError:
            print(f"The key {key} isn't valid. Try again.\n")

## Clear entire dictionary
def clear_dictionary(userDict):
    while True:
        choice = input("Do you wish to clear your entire dict? (Y/N): ").upper()        

        if choice == "Y":            
            userDict.clear()
            print("Dict cleared!\n")
            break            
        elif choice == "N":
            print("Returning to menu.\n")
            break
        else:
            print("Invalid input. Please enter Y or N.\n")           


# Main program
def main():
    userDict = {}

    while True:
        print("===== MENU =====")
        print("1. Check your dict")
        print("2. Add new definition")
        print("3. Search definition")
        print("4. Delete definition")
        print("5. Clear dict")
        print("6. Exit program")

        try:
            userChoice = int(input("Your choice: "))
            print()
        except ValueError:
            print("Invalid input. Please enter a number from 1 to 6.\n")
            continue

        print()
        match userChoice:
            case 1:
                show_dict(userDict)
            case 2:
                add_definition(userDict)
            case 3:
                search_definition(userDict)           
            case 4:
                del_definition(userDict)
            case 5:
                clear_dictionary(userDict)            
            case 6:
                print("Goodbye!")
                break
            case _:
                print("Invalid choice. Please choose a number from 1 to 6.\n")

if __name__ == "__main__":
    main()
