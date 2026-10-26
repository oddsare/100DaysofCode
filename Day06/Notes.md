# Day 6 Notes: Hangman (Assignment 6)

> **AI generated.** These notes were written by AI (Claude) to explain the Python stuff I used on Day 6. Every example was run to make sure it works.

Code for this day: [`Assignment6.py`](Assignment6.py), which uses [`Hangman_pieces.py`](Hangman_pieces.py) and [`words.py`](words.py)

---

## Importing my own files

**What it is:** On Day 4 I imported `random`, which comes with Python. You can also import **your own** `.py` files the same way. If `words.py` is in the same folder, `import words` lets me use anything inside it with `words.something`. Adding `as` gives it a shorter nickname.

```python
import words
import Hangman_pieces as hp

print(len(words.words))
print(words.words[0])
print(hp.hangman_6_life)
```

Output (run from inside the `Day06` folder):

```
6825
aback
  +---+
  |   |
  O   |
      |
      |
      |
=========
```

**Heads up:** The files have to be in the same folder, and you leave off the `.py` when you import.

**Why you'd use it:** It keeps the main game file short and tidy. The big word list and the ASCII pictures live in their own files, so `Assignment6.py` is just the game logic.

**Where I used it:** Lines 1 and 3 of `Assignment6.py`.

---

## random.choice()

**What it is:** `random.choice()` picks one random item straight out of a list. It's a shortcut for picking a random index with `randint()` and then grabbing that item.

```python
import random

words = ["apple", "tiger", "piano"]
print(random.choice(words))

# the long way, like I did on Day 5
print(words[random.randint(0, len(words) - 1)])
```

Output (it's random, so yours will be different):

```
tiger
apple
```

**Why you'd use it:** Picking a random word, a random enemy, a random question, etc.

**Where I used it:** `random.choice(words.words)` on line 8.

---

## list() to split a word into letters

**What it is:** `list()` on a string breaks it into a list where each letter is its own item.

```python
word = "sheep"
letters = list(word)
print(letters)
print(letters[1])
```

Output:

```
['s', 'h', 'e', 'e', 'p']
h
```

**Why you'd use it:** So the word can be compared to my list of blanks letter by letter, and checked with `==` once all the blanks are filled in.

**Where I used it:** `generated_word = list(random.choice(words.words))` on line 8.

---

## for loops

**What it is:** A `for` loop runs the indented code once for **each item** in a list (or each letter in a string). Each time round, the loop variable holds the next item.

```python
for letter in ["c", "a", "t"]:
    print(letter)

blanks = []
for letter in "tiger":
    blanks.append("_")
print(blanks)
```

Output:

```
c
a
t
['_', '_', '_', '_', '_']
```

**Why you'd use it:** When you want to do something to every item. Use `while` when you don't know how many times to loop, and `for` when you're going through a list.

**Where I used it:** Lines 12 and 13, which add one `_` to `blanks` for every letter in the word.

---

## range()

**What it is:** `range(n)` gives the numbers from `0` up to (but **not** including) `n`. It's usually used with `for` to loop a set number of times. `range(len(word))` gives every index position in a word.

```python
for i in range(3):
    print(i)

word = "cat"
for i in range(len(word)):
    print(i, word[i])
```

Output:

```
0
1
2
0 c
1 a
2 t
```

**Why you'd use it:** When you need the **position** of each item, not just the item. In hangman I need to know *where* the guessed letter is so I can put it in the right blank.

**Where I used it:** `for i in range(len(generated_word)):` on line 23.

---

## Changing an item in a list

**What it is:** You can replace an item in a list by putting its index in square brackets on the left of `=`.

```python
blanks = ["_", "_", "_", "_", "_"]
blanks[1] = "h"
blanks[2] = "e"
blanks[3] = "e"
print(blanks)
```

Output:

```
['_', 'h', 'e', 'e', '_']
```

**Why you'd use it:** To update one spot without rebuilding the whole list, like swapping a `_` for the letter the player guessed.

**Where I used it:** `blanks[i] = user_guess` on line 25.

---

## in and not in

**What it is:** `in` checks if something is inside a list or string, and gives back `True` or `False`. `not in` is the opposite.

```python
word = ["s", "h", "e", "e", "p"]
print("e" in word)
print("z" in word)
print("z" not in word)
print("app" in "apple")
```

Output:

```
True
False
True
True
```

**Why you'd use it:** A really quick way to check "is this letter in the word?" without writing a loop.

**Where I used it:** `if user_guess not in generated_word:` on line 26 decides if you lose a life.

---

## .lower()

**What it is:** `.lower()` gives back a copy of a string with every letter made lowercase. There's also `.upper()` for capitals.

```python
guess = "E"
print(guess.lower())
print("Hello World".lower())
print("hello".upper())
```

Output:

```
e
hello world
HELLO
```

**Why you'd use it:** So `"E"` and `"e"` count as the same guess. All the words in `words.py` are lowercase, so I make the guess lowercase too. (This would've saved me all the `or` checks on Day 3!)

**Where I used it:** `input("What is your guess: ").lower()` on line 18.

---

## print(*list)

**What it is:** Putting a `*` in front of a list inside `print()` "unpacks" it. Every item gets printed with a space between, without the brackets, quotes and commas.

```python
blanks = ["_", "h", "e", "e", "_"]
print(blanks)
print(*blanks)
```

Output:

```
['_', 'h', 'e', 'e', '_']
_ h e e _
```

**Why you'd use it:** It makes the hangman blanks look like a real game instead of a Python list.

**Where I used it:** `print(*blanks)` on lines 15 and 31.

---

## -= and += shortcuts

**What it is:** `score -= 1` is short for `score = score - 1`. Same with `+=`, `*=` and `/=`.

```python
lives = 6
lives -= 1
print(lives)

points = 10
points += 5
print(points)
```

Output:

```
5
15
```

**Why you'd use it:** Less typing for really common stuff like losing a life or adding to a score.

**Where I used it:** `score -= 1` on line 29.

---

## while with two conditions

**What it is:** A `while` loop can use `and` / `or` just like an `if`. With `and`, the loop keeps going only while **both** are true, so it stops as soon as either one becomes false.

```python
lives = 2
found = False
turn = 0

while lives != 0 and not found:
    turn += 1
    print(f"Turn {turn}")
    if turn == 3:
        found = True
    else:
        lives -= 1

print(f"Lives left: {lives}")
```

Output:

```
Turn 1
Turn 2
Lives left: 0
```

**Why you'd use it:** A game usually ends for more than one reason. In hangman, you either run out of lives or guess the whole word.

**Where I used it:** `while score != 0 and blanks != generated_word:` on line 17.

---

## getattr()

**What it is:** `getattr(thing, "name")` gets something out of a module (or object) using its name **as a string**. Because it's a string, I can build the name with an f-string.

```python
import Hangman_pieces as hp

score = 3
picture = getattr(hp, f"hangman_{score}_life")
print(picture)

# that's the same as writing:
print(hp.hangman_3_life == picture)
```

Output (run from inside the `Day06` folder):

```
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
True
```

**Why you'd use it:** When the name of the thing you want depends on a variable. Here it means one line picks the right hangman picture for however many lives are left, instead of six `if` statements. (On Day 7 I did the same thing with a list instead.)

**Where I used it:** `print(getattr(hp, f"hangman_{score}_life"))` on line 28.

---

**Also used today (explained in earlier notes):** lists, `.append()`, `len()`, `"".join()` ([Day 5](../Day05/Notes.md)), if / else and `!=` / `==` ([Day 3](../Day03/Notes.md)), raw strings for the pictures in `Hangman_pieces.py` ([Day 3](../Day03/Notes.md)).
