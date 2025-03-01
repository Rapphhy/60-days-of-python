# Rock paper scissors game
import random 

emojis = {'r': '🪨', 'p': '📄', 's': '✂️'} # Using dict to map emoji to each character
choices = ('r', 'p', 's')

def determine_winner(user_choice, computer_choice):
    """Determines the winner based on choices."""
    if user_choice == computer_choice:
        return 'Tie'
    elif (
        (user_choice == 'r' and computer_choice == 's') or 
        (user_choice == 's' and computer_choice == 'p') or 
        (user_choice == 'p' and computer_choice == 'r')):
        return 'You win'
    return 'You lose'

while True:
    user_choice = input('Rock, Paper or Scissors? (r,p,s): ').lower()
    
    if user_choice not in choices:
        print('Invalid choice') # print error message when a user selects invalid option
        continue 
    
    computer_choice = random.choice(choices) 

    print(f'You chose {emojis[user_choice]}')
    print(f'Computer chose {emojis[computer_choice]}')

    print(determine_winner(user_choice, computer_choice))

    proceed = input('Continue? (y/n): ').lower()
    if proceed == 'n':
        break
