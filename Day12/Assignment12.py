import random

art=r'''  / _ \_   _  ___  ___ ___  /__   \ |__   ___    /\ \ \_   _ _ __ ___ | |__   ___ _ __ 
 / /_\/ | | |/ _ \/ __/ __|   / /\/ '_ \ / _ \  /  \/ / | | | '_ ' _ \| '_ \ / _ \ '__|
/ /_\\| |_| |  __/\__ \__ \  / /  | | | |  __/ / /\  /| |_| | | | | | | |_) |  __/ |   
\____/ \__,_|\___||___/___/  \/   |_| |_|\___| \_\ \/  \__,_|_| |_| |_|_.__/ \___|_|    '''


def amount_of_guess(difficulty):
    if difficulty == "easy":
        guess = 10
        return guess
    if difficulty == "hard":
        guess = 5
        return guess
    
def random_number():
    return random.randint(0,100)

def check_guess(make_guess,random_number):
    if make_guess > random_number:
        return "Too high." , make_guess
    elif make_guess < random_number:
        return "Too low." , make_guess
    else:
        return f"You got it! The answer was {random_number}.",make_guess
    



print(art)
print(f"Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 0 and 100.")
difficulty =input("Choose a difficulty. Type 'easy' or 'hard': ")
guess =-1
is_game_over = False
random_num =random_number()

guess = amount_of_guess(difficulty)

print(f"You have {guess} attempts remaining to guess the number.")
while not is_game_over:
    
    make_a_guess , guess_number = check_guess(int(input(f"Make a guess: ")),random_num)
    if make_a_guess != False:
        print(make_a_guess)
        if  guess_number != random_num:
            guess -= 1
            print(f"You have {guess} attempts remaining to guess the number.")
        else:
            break
    if  guess == False:
        print("You lost")
        is_game_over = True
    
