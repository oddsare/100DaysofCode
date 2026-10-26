# Day 7 Notes: Hangman

> **AI generated.** These notes were written by AI (Claude) to explain the Python stuff I used on Day 7. Every example was run to make sure it works.

Code for this day: [`Hangman.py`](Hangman.py), which uses [`Hangman_pieces.py`](Hangman_pieces.py) and [`words.py`](words.py)

This is my second version of hangman. Most of what it uses is explained in the [Day 6 notes](../Day06/Notes.md). These are the new bits.

---

## Multiplying a list: ['_'] * n

**What it is:** `*` on a list repeats it. `['_'] * 5` makes a list with five `'_'` in it. It works on strings too.

```python
word = "tiger"
blanks = ['_'] * len(word)
print(blanks)
print("ha" * 3)
```

Output:

```
['_', '_', '_', '_', '_']
hahaha
```

**Why you'd use it:** It makes a list of blanks in one line. On Day 6 I needed a `for` loop with `.append()` to do the same thing.

**Where I used it:** `['_'] * n` on line 12 of `Hangman.py`.

---

## += on a list

**What it is:** `my_list += other_list` adds every item from `other_list` onto the end of `my_list`. It's like doing `.append()` for each item.

```python
guessed_right = []
guessed_right += ['_'] * 3
print(guessed_right)

guessed_right += ['x', 'y']
print(guessed_right)
```

Output:

```
['_', '_', '_']
['_', '_', '_', 'x', 'y']
```

**Why you'd use it:** To add a bunch of items to a list at once.

**Where I used it:** `guessed_right += ['_'] * n` on line 12.

---

## A list of pictures + a counter to pick one

**What it is:** Lists can hold anything, including big multi-line strings like ASCII art. If I keep a counter variable and add 1 to it each time, I can use it as the index to show the next picture in order.

```python
stages = ["stage 0: head", "stage 1: body", "stage 2: arm"]
wrong_guesses = 0

print(stages[wrong_guesses])
wrong_guesses += 1
print(stages[wrong_guesses])
wrong_guesses += 1
print(stages[wrong_guesses])
```

Output:

```
stage 0: head
stage 1: body
stage 2: arm
```

**Why you'd use it:** It's a simpler way to step through pictures in order than the `getattr()` trick from Day 6. Adding a new picture is just adding it to the list.

**Where I used it:** `Hangman_pieces_list` on line 10 holds all six pictures, `hangman_icon` on line 8 is the counter, and `print(Hangman_pieces_list[hangman_icon])` on line 28 shows the right one.

---

## Comparing whole lists with == and !=

**What it is:** `==` works on whole lists too. Two lists are equal only if they have the same items **in the same order**.

```python
guessed = ['c', 'a', 't']
answer = list("cat")
print(guessed == answer)

guessed = ['c', '_', 't']
print(guessed != answer)
print(['t', 'a', 'c'] == answer)
```

Output:

```
True
True
False
```

**Why you'd use it:** It's an easy way to check if the player has filled in every blank: if the blanks list matches the word, they won.

**Where I used it:** `while guessed_right != list(Computer_choice) and lives != 0:` on line 16.

---

## The game loop

**What it is:** Most games are built the same way: a `while` loop that keeps asking for a move, updates things (letters, lives), shows the result, and checks if the game is over. When the loop ends, you check *why* it ended to say if the player won or lost.

```python
word = "hi"
guesses = ["h", "z", "i"]    # pretend these were typed in
blanks = ['_'] * len(word)
lives = 2
turn = 0

while blanks != list(word) and lives != 0:
    guess = guesses[turn]
    turn += 1
    for i in range(len(word)):
        if word[i] == guess:
            blanks[i] = guess
    if guess not in word:
        lives -= 1
    print(*blanks, f"({lives} lives)")

if blanks == list(word):
    print("You win!")
else:
    print("Game over!")
```

Output:

```
h _ (2 lives)
h _ (1 lives)
h i (1 lives)
You win!
```

**Why you'd use it:** It's the backbone of pretty much every game: hangman, quizzes, number guessing, and so on.

**Where I used it:** Lines 16 to 35 of `Hangman.py`. (My version doesn't have the "You win!" part yet, only "Game over!".)

---

**Also used today (explained in earlier notes):** importing my own files, `random.choice()`, `for` + `range()`, `in` / `not in`, `print(*list)`, `-=` ([Day 6](../Day06/Notes.md)), `"".join()` and `len()` ([Day 5](../Day05/Notes.md)).
