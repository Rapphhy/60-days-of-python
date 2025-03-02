import random 

emojis = {'r': '🪨', 'p': '📄', 's': '✂️'}  # Using dict to map emoji to each character
choices = ('r', 'p', 's')

def get_user_choice(): # user's choice
    while True:
        user_choice = input('Rock, Paper or Scissors? (r,p,s): ').lower()
        if user_choice in choices:
            return user_choice
        print('Invalid choice')  # print error message whenever a user selects an invalid option

def determine_winner(user_choice, computer_choice): #Determine winner
    if user_choice == computer_choice:
        return 'Tie'
    if ((user_choice == 'r' and computer_choice == 's') or 
       (user_choice == 's' and computer_choice == 'p') or 
       (user_choice == 'p' and computer_choice == 'r')):
        return 'You win'
    return 'You lose'

while True:
    user_choice = get_user_choice()  
    computer_choice = random.choice(choices)  #bringing this into the while loop to ensure that computer generates a new random choice every round

    print(f'You chose {emojis[user_choice]}')  
    print(f'Computer chose {emojis[computer_choice]}')

    print(determine_winner(user_choice, computer_choice))  

    if input('Continue? (y/n): ').lower() == 'n': #break when user selects n
        break
