# Rock paper scissors game
import random 

emojis = {'r': '🪨', 'p': '📄', 's': '✂️'} # Using dict to map emoji to each character
choices = ('r', 'p', 's')

while True:
    user_choice = input('Rock, Paper or Scissors? (r,p,s): ').lower()
    
    if user_choice not in choices:
        print('Invalid choice') # print error message when a user selects invalid option
        continue 
    
    computer_choice = random.choice(choices) 

    print(f'You chose {emojis[user_choice]}')
    print(f'Computer chose {emojis[computer_choice]}')

    if user_choice == computer_choice:
        print('Tie')
    elif (
        (user_choice == 'r' and computer_choice == 's') or 
        (user_choice == 's' and computer_choice == 'p') or
        (user_choice == 'p' and computer_choice == 'r')):
        print('You win')
    else:
        print('You lose')

    proceed = input('Continue? (y/n): ').lower()
    if proceed == 'n':
        break
