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