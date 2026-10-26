import random



#we could make a def block and  have both the player and the user draw from it  honestly lets do that 

player_choice = int(input("What do you choose Rock(1), Paper(2) or Scissors(3)?  \n"))

ai_choice = random.randint(1,3)

if ai_choice == 1:
    print("The Computer has choosen ROCK")
    print("""
        _______
    ---'   ____)
        (_____)
        (_____)
        (____)
    ---.__(___)
    """) 
elif ai_choice == 2:
    print("The Computer has choosen PAPER")
    print("""
        _______
    ---'    ____)____
            ______)
            _______)
            _______)
    ---.__________)
    """)
else:
    print("The Computer has choosen Scissors")
    print("""
        _______
    ---'   ____)____
            ______)
        __________)
        (____)
    ---.__(___)
    """)


if player_choice == 1:
    print("The you have choosen ROCK")
    print("""
        _______
    ---'   ____)
        (_____)
        (_____)
        (____)
    ---.__(___)
    """) 
elif player_choice == 2:
    print("The you have choosen PAPER")
    print("""
        _______
    ---'    ____)____
            ______)
            _______)
            _______)
    ---.__________)
    """)
else:
    print("The you have choosen Scissors")
    print("""
        _______
    ---'   ____)____
            ______)
        __________)
        (____)
    ---.__(___)
    """)




if ai_choice == player_choice:
    print("DRAW")
elif ai_choice == 1:
    if player_choice == 2:
        print("Player Wins")
    else:    
        print("Computer Wins")
elif ai_choice == 2:
    if player_choice == 3:
        print("Player Wins")
    else:
        print("Computer Wins")
elif ai_choice == 3:
    if player_choice == 1:
        print("Player Wins")
    else:
        print("Computer Wins")





    
