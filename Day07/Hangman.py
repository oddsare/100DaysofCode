import Hangman_pieces
import random
import words

Computer_choice = random.choice(words.words)

lives = 6 
hangman_icon = 0
guessed_right = []
Hangman_pieces_list = [Hangman_pieces.hangman_6_life,Hangman_pieces.hangman_5_life,Hangman_pieces.hangman_4_life,Hangman_pieces.hangman_3_life, Hangman_pieces.hangman_2_life,Hangman_pieces.hangman_1_life]
n = len(Computer_choice)
guessed_right += ['_'] * n
print(Hangman_pieces.intro)
print("Welcome to Hangman")
print(*guessed_right)
while  guessed_right != list(Computer_choice) and lives != 0:
    
    User_choice =input("What letter are you choosing? ")
    
    for i in range(len(Computer_choice)):
        if Computer_choice[i] == User_choice:
            
            guessed_right[i] = User_choice
    if User_choice not in Computer_choice:
        lives -= 1
        
        print("You guess wrong")
        print(Hangman_pieces_list[hangman_icon])
        hangman_icon += 1
        print(f"****************************{lives}/6 LIVES LEFT****************************")
        
        
    print(*guessed_right)
    if lives == 0:
        print("Game over! The word was " +"".join(Computer_choice))
    
# cannot do player choice because that is in the while loop