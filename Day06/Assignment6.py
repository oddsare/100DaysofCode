import Hangman_pieces as hp
import random
import words

print(hp.intro)

generated_word_full = random.choice(words.words)
generated_word = list(random.choice(words.words))
blanks =[]
score =6 
print(generated_word)

for i in generated_word:
    blanks.append("_")
    
print(*blanks)

while  score != 0 and  blanks != generated_word:
    user_guess = input("What is your guess: ").lower()
  
    if len(user_guess) >1 :
        print(" Your Guess needs to be 1 letter")
    else:
        for i in range(len(generated_word)):
            if generated_word[i] == user_guess:
                blanks[i] = user_guess
        if user_guess not in generated_word:
            print(f"You guessed {user_guess}, that's not in the word. You lose a life.")
            print(getattr(hp, f"hangman_{score}_life"))
            score -= 1
        print(f"****************************{score}/6 LIVES LEFT****************************")
        print(*blanks)
if blanks == generated_word:
    print("You win!")
else:
    print("Game over! The word was " + "".join(generated_word))