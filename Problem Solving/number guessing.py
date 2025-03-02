import random 

secret_number = random.randint(1, 100)  # Computer generates  a random number

def get_user_guess():
    user_guess = int(input("Guess a number (1 - 100): ")) # user's selection
    if user_guess < 1:
        print("Too low!")
    elif user_guess > 100:
        print("Too high!")
    else:
        return user_guess

while True:
    user_guess = get_user_guess()  
    if user_guess == secret_number:
        print(f"Congratulations! You guessed right: {secret_number}") #print congratulatory message when user guess right
        break  

    print("Guess higher!" 
          if user_guess < secret_number 
          else "Guess lower!")    #prompt the user to guess higher or lower  
