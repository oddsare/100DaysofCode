chest= (r'''*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     '"=.|                  |
|___________________|__"=._o'"-._        '"=.______________|___________________
          |                '"=._o'"=._      _'"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; '"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .' ' '' ,  '"-._"-._   ". '__|___________________
          |           |o'"=._' , "' '; .". ,  "-._"-._; ;              |
 _________|___________| ;'-.o'"=._; ." ' ''."' . "-._ /_______________|_______
|                   | |o;    '"-.o'"=._''  '' " ,__.--o;   |
|___________________|_| ;     (#) '-.o '"=.'_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      '".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print(chest)
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

start_Treasure_hunt = input("You're at a cross road. Where do you want to go? Type \"Left\" or \"right\" \n")

if start_Treasure_hunt == "Left" or start_Treasure_hunt == "left":
    going_left = input("You come to a lake. There is an island in the middle of the lake. Type wait to \"wait\" for a boat. Type swin to \"swim\"" \
    " across\n")
    if going_left == "Wait" or going_left == "wait":
        choose_wait = input("You arrive at the island unharmed. There is a house wth 3 doors. One \" red\" , one \" yellow\"  and one \" blue\" . Which color door" \
        "do you choose? \n")    
        if choose_wait == "Red" or choose_wait == "red":
            print("It's a room full of fire. Game Over. ") 
        elif choose_wait == "Yellow" or choose_wait == "yellow":
            print("You found the treasure! You Win!")
        else:
            print("You enter a room of beasts. Game Over.")
    elif going_left == "Swim" or going_left == "swim":
        print("You get attacked by an angry trout. Game Over.")
elif start_Treasure_hunt == "Right" or start_Treasure_hunt =="right":
    print("You fell into a hole. Game Over. ")
