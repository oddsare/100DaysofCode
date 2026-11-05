# How to Set Up a Program (and Why)

> **AI generated.** These notes were written by AI (Claude) to explain how to lay out a Python program, using things from my first 11 days. Every example was run to make sure it works.

---

## The big picture

Most Python programs follow the same order, top to bottom:

1. **Imports**
2. **Settings and data** that don't change
3. **Functions**, each doing one job
4. **The main program** at the bottom, which uses the functions

Here's a whole (tiny) program laid out that way:

```python
# 1. Imports
import math

# 2. Settings and data that don't change
LOGO = "=== Mini Quiz ==="
QUESTIONS = {"2 + 2": "4", "Capital of France": "paris"}

# 3. Functions (one job each)
def ask(question):
    answer = input(f"{question}? ")
    return answer.lower() == QUESTIONS[question]

def play_game():
    print(LOGO)
    score = 0
    for question in QUESTIONS:
        if ask(question):
            score += 1
    percent = math.floor(score / len(QUESTIONS) * 100)
    print(f"You got {score} out of {len(QUESTIONS)} ({percent}%)")

# 4. The main program
if __name__ == "__main__":
    while input("Play the quiz? (y/n) ").lower() == "y":
        play_game()
    print("Bye")
```

Output (if I type `y`, then `4`, then `Paris`, then `n`):

```
Play the quiz? (y/n) y
=== Mini Quiz ===
2 + 2? 4
Capital of France? Paris
You got 2 out of 2 (100%)
Play the quiz? (y/n) n
Bye
```

**Why this order:** Python reads a file from top to bottom. Imports and functions have to exist **before** the code that uses them runs, so they go first. It also means you always know where to look: data at the top, the "how" in the middle, and the "what happens" at the bottom.

The sections below go through each part.

---

## Plan it with comments first

**What it is:** Before writing code, write the steps as comments. Then fill in the code under each one.

```python
# 1. Get two numbers
first = 3
second = 4

# 2. Add them up
total = first + second

# 3. Show the answer
print(f"{first} + {second} = {total}")
```

Output:

```
3 + 4 = 7
```

**Why:** It's much easier to fix a plan than to fix half-written code. I did this for my Blackjack game: I wrote the steps as comments ("give 2 cards to the player and 1 card to the dealer", "if player busts, say you lose") and then built each one.

---

## Imports go at the top

**What it is:** Every `import` goes at the very top of the file.

```python
import math

print(math.sqrt(16))
```

Output:

```
4.0
```

**Why:** Anyone reading the file sees straight away what it depends on. It's also guaranteed to be loaded before any code tries to use it.

**Where I've done this:** `import random` at the top of Days 4, 5, 6, 7 and 11, and `import os` on Day 10.

---

## Settings and data near the top, in CAPITALS

**What it is:** Values that never change while the program runs (the card list, a rule like "the house stands on 17", the logo) go near the top. People usually write their names in CAPITALS. That's just a habit to say "don't change this", because Python doesn't stop you.

```python
CARDS = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
HOUSE_STANDS_ON = 17

house_total = 16
if house_total < HOUSE_STANDS_ON:
    print("House draws")
```

Output:

```
House draws
```

**Why:** If the rule changes, you change it in **one** place. In my Day 11 game, the number 17 appears on three lines (88, 94 and 99), and getting one of them wrong froze the game. With `HOUSE_STANDS_ON`, there would only be one 17 to get right.

---

## Functions before the code that uses them

**What it is:** A `def` has to come **before** the line that calls it.

```python
def greet(name):
    print(f"Hi {name}")

greet("Sam")
```

Output:

```
Hi Sam
```

**Heads up:** If `greet("Sam")` came before the `def`, Python would crash with `NameError: name 'greet' is not defined`, because it hasn't read the function yet.

**Why:** Putting all the functions together in the middle of the file means they're always defined by the time the main program runs.

---

## One job per function, named with a verb

**What it is:** Each function should do **one** thing, and its name should say what that is, usually starting with a verb: `deal_card`, `calculate_score`, `compare`.

```python
def deal_card(deck, hand):
    hand.append(deck[0])

def calculate_score(hand):
    return sum(hand)

hand = []
deal_card([10], hand)
deal_card([7], hand)
print(calculate_score(hand))
```

Output:

```
17
```

**Why:** Small functions are easy to read, test and fix. When my Ace logic had bugs, the version with a separate `calculate_total` function was much easier to test than Ace code spread through the main loop.

---

## Pass things in, return things out

**What it is:** Give a function what it needs through its **parameters**, and get the answer back with `return`, instead of having it read and change variables from outside.

```python
def add_bonus(score, bonus):
    return score + bonus

score = 10
score = add_bonus(score, 5)
print(score)
```

Output:

```
15
```

**Why:** You can see exactly what goes in and what comes out, so there are no surprises. In my Day 8 cipher, the functions added to a list made outside them, so calling them twice in one run would have mixed two messages together.

---

## If you write the same code twice, make it a function

**What it is:** When the same lines appear in two places, put them in a function and call it from both.

```python
def new_hand():
    hand = [10, 7]
    print(f"New hand: {hand}")
    return hand

player = new_hand()
player = new_hand()
```

Output:

```
New hand: [10, 7]
New hand: [10, 7]
```

**Why:** If you fix a bug in copied code, you have to remember to fix every copy. In my Day 11 game, the dealing and resetting code is written out twice (lines 35 to 46 and lines 119 to 130).

---

## A main game function and a play-again loop

**What it is:** Put one whole game in a function, like `play_game()`, and call it from a loop that asks "play again?". This is explained with an example in my [Day 11 notes](Day11/Notes.md#putting-the-whole-game-in-a-function).

**Why:** Every game starts fresh automatically (no reset code), and "play again" works however the game ended.

---

## if __name__ == "__main__":

**What it is:** Every Python file has a hidden variable called `__name__`. When you **run** the file, it's `"__main__"`. When another file **imports** it (like my Hangman did with `import words`), it's the file's name instead. So code under this check only runs when you run the file directly.

```python
def main():
    print("Running the program")

if __name__ == "__main__":
    main()
```

Output:

```
Running the program
```

**Why:** It lets a file be both a program you can run **and** a toolbox of functions other files can import, without the game suddenly starting when it gets imported. For small one-file programs it's optional, but you'll see it in a lot of other people's code.

---

## Test small pieces as you go

**What it is:** Check each function on its own with inputs where you already know the right answer.

```python
def calculate_score(hand):
    total = sum(hand)
    aces = hand.count(11)
    while total > 21 and aces > 0:
        total -= 10
        aces -= 1
    return total

print(calculate_score([11, 11]) == 12)
print(calculate_score([11, 10, 10, 5]) == 26)
print(calculate_score([10, 9]) == 19)
```

Output:

```
True
True
True
```

**Why:** It's much faster than playing whole games and hoping the tricky hand comes up. That's how we found the "same Ace dropping twice" bug: specific hands with known answers.

---

## Names that say what they hold

**What it is:** Use names that describe the value (`player_total`, `house_cards`), and don't reuse one name for two different things.

```python
deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
player_hand = [10, 7]

for position in range(len(player_hand)):
    print(position, player_hand[position])

print(len(deck))
```

Output:

```
0 10
1 7
13
```

**Why:** In an early version of my Blackjack, I used `cards` for the deck **and** as a loop variable (`for cards in range(...)`). The loop replaced the deck with a number, and the game crashed the next time it dealt a card.

---

## Checklist

When starting a new program:

1. Write the steps as comments.
2. Imports at the top.
3. Settings and data next, in CAPITALS.
4. One function per job, named with a verb, taking parameters and using `return`.
5. Main program at the bottom (optionally under `if __name__ == "__main__":`).
6. Test each function with inputs you know the answer to.
7. If you've copied code, turn it into a function.
