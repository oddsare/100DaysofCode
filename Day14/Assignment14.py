import random
import game_data as gd # type: ignore
import os


art =r'''    __  ___       __             
   / / / (_)___ _/ /_  ___  _____
  / /_/ / / __ '/ __ \/ _ \/ ___/
 / __  / / /_/ / / / /  __/ /    
/_/ ///_/\__, /_/ /_/\___/_/     
   / /  /____/_      _____  _____
  / /   / __ \ | /| / / _ \/ ___/
 / /___/ /_/ / |/ |/ /  __/ /    
/_____/\____/|__/|__/\___/_/        '''


vs = r''' _    __    
| |  / /____
| | / / ___/
| |/ (__  ) 
|___/____(_)'''

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def random_person():
   return random.choice(gd.data[1:])


def who_is_higher():
    if person1["follower_count"] > person2["follower_count"]:
        return "A"
    elif person1["follower_count"] < person2["follower_count"]:
        return "B"
is_game_over = False
score = 0 # if this gets itterating then it will reset the score  to zero

print(art)
######################################
while not is_game_over:
    person1 =random_person()
    person2 = random_person()


    print(f"Compare A: {person1["name"]}, {person1["description"]}, from {person1["country"]}.")
    print(vs)
    print(f"Compare B: {person2["name"]}, {person2["description"]}, from {person2["country"]}.")


    highest_count = who_is_higher()
    print(f"This is the highest_count variable {highest_count}")
        
    who_has_more = input(f"Who has more followers? Type 'A' or 'B': ").capitalize()

    if who_has_more == highest_count:
        score += 1
        clear()
        print(art)
        print(f"You're right! Current score: {score}.")
        
    else:
        print(f"Sorry, that's wrong. Final score: {score}")
        is_game_over = True



