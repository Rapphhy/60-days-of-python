# User rolls the dice and has two options yes or  no. This can be in either upper case or lower case.
# If user selects yes it displayed number between 1 and 6, if no it displayed "Thanks for playing"
# And if any other option is selected outside any of these two user gets "Invalid option"


import random

while True:
    option = input("Roll the dice (yes/no):- ").lower()
    if option == 'yes':
        die1 = random.randint(1,6)
        die2 = random.randint(1,6)
        print(f'({die1}, {die2})')
    elif option == 'no':
        print("Thanks for playing") 
        break
    else:
        print("Invalid option")   