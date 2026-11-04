import random

art =r'''.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _' |/ __| |/ / |/ _' |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
'-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\
      |  \/ K|                            _/ |                
      '------'                           |__/           '''

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
player = []
house = []
player_total = 0
house_total = 0
number_of_cards = 0
players_aces = 0
house_aces =0

def draw_cards(user_cards,number):
    number_of_11 = 0
    for i in range(number):
        card= random.choice(cards)
        user_cards.append(card)


def check_for_ll(user_cards,how_many_aces):
    for i in range(len(user_cards)):
        if user_cards[i] == 11:
            how_many_aces +=1
    return how_many_aces
                  
do_you_want_to_play = input(f"Do you want to play a game of Blackjack? Type 'y' or 'n':  ")   
draw_cards(player,2)
draw_cards(house,1)

players_aces =check_for_ll(player,players_aces)
house_aces =check_for_ll(house,house_aces)

player_total = sum(player)
    
house_total =sum(house)
number_of_cards =0
house_number_of_cards = 0
itterating_number = 0

while True:
    
    
 
    for i in range(players_aces):
        if player_total > 21 and 11 in player:
            player[player.index(11)] = 1
            player_total -= 10
    
    print(f"Your cards: {player}, current score: {player_total}")
    print(f"Computer's first card: {house_total}")
    another_card = input(f"Type 'y' to get another card, type 'n' to pass: ").lower()
    if another_card == "y":
        
        number_of_cards += 1
        itterating_number = 1+ number_of_cards
        draw_cards(player,1)
       
    
        player_total += player[itterating_number]
        players_aces =check_for_ll(player,players_aces)

        if player_total >21 and 11 not in player:
            print(f"Your final hand: {player}, final score: {player_total}")
            print(f"Computer's final hand: {house}, final score: {house_total}")
            print("You went over. You lose 😭")
            break
    #do logic to give computer as many cards as needed and give player 1 card at a time 
    
    
    
    
    
    if another_card == "n":
        while True:
            for i in range(house_aces):
                if house_total > 21 and 11 in house:
                    house[house.index(11)] = 1
                    house_total -= 10
                    
            if house_total < 17:
                house_number_of_cards += 0
                house_itterating_number = 1+ house_number_of_cards
                draw_cards(house,1)
                house_total += house[house_itterating_number]
                house_aces =check_for_ll(house,house_aces)
            elif house_total > 17:
                for i in range(house_aces):
                    if house_total > 21 and 11 in house:
                        house[house.index(11)] = 1
                        house_total -= 10
                if house_total >17:
                        break
                
                
        
        print(f"Your final hand: {player}, final score: {player_total}")
        print(f"Computer's final hand: {house}, final score: {house_total}")
        #if statements on how to win and why
        if house_total >21:
            print("Opponent went over. You win 😁")
        elif house_total > player_total:
            print("House beat you. House always wins")
        elif house_total == player_total:
            print("Draw, you got lucky")
        elif player_total >house_total:
            print("You beat the house. You win 😁")
        do_you_want_to_play_again = input(f"Do you want to play a game of Blackjack? Type 'y' or 'n': ")    
        if do_you_want_to_play_again == "y":
            player = []
            house = []
            draw_cards(player,2)
            draw_cards(house,1)
            players_aces =check_for_ll(player,players_aces)
            house_aces =check_for_ll(house,house_aces)

            
            player_total = sum(player)
    
            house_total =sum(house)
            number_of_cards =0
            house_number_of_cards = 0
            itterating_number = 0
            False
        else:
            exit()


# I solve 2 things the how many aces  problem and getting the cards 