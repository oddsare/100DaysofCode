# Day 4 Notes: Rock Paper Scissors

> **AI generated.** These notes were written by AI (Claude) to explain the Python stuff I used on Day 4. Every example was run to make sure it works.

Code for this day: [`Assignment4.py`](Assignment4.py)

---

## import and modules

**What it is:** A module is a file full of code someone already wrote. `import` lets you use it in your program. Python comes with lots of built-in ones, like `random` (random numbers) and `math` (math stuff). After importing, you use what's inside with a dot: `module.thing`.

```python
import math

print(math.sqrt(49))
print(math.pi)
```

Output:

```
7.0
3.141592653589793
```

**Why you'd use it:** So you don't have to write everything yourself. Someone already figured out how to make random numbers, so I just borrow it.

**Where I used it:** `import random` on line 1 of `Assignment4.py`.

---

## random.randint()

**What it is:** `random.randint(a, b)` picks a random whole number from `a` to `b`. Both ends are included, so `randint(1, 3)` can give `1`, `2` or `3`.

```python
import random

dice = random.randint(1, 6)
print(f"You rolled a {dice}")

computer = random.randint(1, 3)
print(computer)
```

Output (it's random, so yours will be different):

```
You rolled a 4
2
```

**Why you'd use it:** Games! Dice rolls, the computer's move, random enemies, anything that shouldn't be the same every time.

**Where I used it:** `ai_choice = random.randint(1,3)` on line 9 picks the computer's move.

---

## Comments with #

**What it is:** Anything after a `#` on a line is ignored by Python. It's a note for humans (including future me).

```python
# This whole line is a comment, Python skips it
lives = 3  # a comment can go after code too
print(lives)
```

Output:

```
3
```

**Why you'd use it:** To explain *why* the code does something, leave reminders or to-dos, or quickly switch a line off while testing without deleting it.

**Where I used it:** Line 5 of `Assignment4.py`, where I left myself a note about making a `def` block (that's a function, which I haven't learned yet).

---

## Converting input straight away: int(input())

**What it is:** You can wrap `input()` inside `int()` so the answer gets turned into a number in one line. Python runs the inside first (`input()`), then `int()` converts what was typed.

```python
choice = int(input("What do you choose? Rock(1), Paper(2) or Scissors(3) "))
print(choice + 1)
```

Output (if I type `2`):

```
What do you choose? Rock(1), Paper(2) or Scissors(3) 2
3
```

**Heads up:** If the user types something that isn't a whole number (like `rock` or `2.5`), `int()` crashes with a `ValueError`.

**Why you'd use it:** It saves a line compared to storing the text first and converting it after.

**Where I used it:** `player_choice = int(input(...))` on line 7.

---

## Using numbers to stand for choices

**What it is:** Instead of comparing words like `"rock"`, I gave each choice a number (Rock = 1, Paper = 2, Scissors = 3). Then the computer can use `randint(1, 3)` to pick, and comparing is easy.

```python
player = 1     # rock
computer = 3   # scissors

if player == computer:
    print("DRAW")
elif player == 1 and computer == 3:
    print("Player Wins")
else:
    print("Not this one")
```

Output:

```
Player Wins
```

**Why you'd use it:** Numbers are easier to generate randomly and there's no problem with typos or capital letters.

**Where I used it:** The winner check on lines 77 to 93, which compares `ai_choice` and `player_choice`.

---

**Also used today (explained in earlier notes):** multi-line strings for the hand pictures, if / elif / else, nested ifs ([Day 3](../Day03/Notes.md)).
