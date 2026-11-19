# Day 12 Notes: Number Guessing Game

> **AI generated.** These notes were written by AI (Claude) to explain the Python stuff I used on Day 12. Every example was run to make sure it works.

Code for this day: [`Assignment12.py`](Assignment12.py)

---

## Returning two things from a function

**What it is:** A function can `return` two values with a comma between them. You catch them with two variable names on the left of `=`. This is called **unpacking**.

```python
def check(guess, answer):
    if guess > answer:
        return "Too high.", guess
    elif guess < answer:
        return "Too low.", guess
    else:
        return "You got it!", guess

message, number = check(70, 42)
print(message)
print(number)
print(check(42, 42))
```

Output:

```
Too high.
70
('You got it!', 42)
```

**Why you'd use it:** One function can hand back the message **and** the guess at the same time. If you print the result without unpacking, you see both inside brackets (a tuple).

**Where I used it:** `check_guess` returns two things on lines 22, 24 and 26. Line 44 unpacks them: `make_a_guess , guess_number = check_guess(...)`.

---

## random.randint includes both ends

**What it is:** `random.randint(a, b)` picks a whole number from `a` to `b`, and **both `a` and `b` can come up**.

```python
import random

rolls = []
for i in range(10):
    rolls.append(random.randint(1, 3))
print(rolls)
```

Output (random, yours will be different):

```
[2, 3, 1, 1, 3, 2, 3, 1, 2, 3]
```

**Why you'd use it:** To pick the secret number. `randint(0, 100)` can give 0 or 100, so the game really is "between 0 and 100".

**Where I used it:** `return random.randint(0,100)` on line 18.

---

## Two ways out of a while loop

**What it is:** A `while not is_game_over:` loop keeps going until the flag is `True`. There are two ways out:

- **`break`** leaves the loop **right now**.
- **Setting the flag to `True`** lets the rest of the loop finish, then the loop stops when it checks again.

```python
answer = 7
attempts = 3
is_game_over = False

while not is_game_over:
    guess = int(input("Make a guess: "))
    if guess == answer:
        print("You got it!")
        break
    attempts -= 1
    print(f"Wrong. {attempts} attempts left.")
    if attempts == 0:
        print("You lost")
        is_game_over = True
```

Output (if I type `5`, then `9`, then `7`):

```
Make a guess: 5
Wrong. 2 attempts left.
Make a guess: 9
Wrong. 1 attempts left.
Make a guess: 7
You got it!
```

**Why you'd use it:** Winning should stop the game at once (`break`). Running out of guesses sets the flag so the loop ends.

**Where I used it:** `while not is_game_over:` on line 42, `break` on line 51, and `is_game_over = True` on line 54.

---

## 0 counts as False

**What it is:** In Python, `0 == False` is `True` and `1 == True` is `True`. Any other number or any text is **not** equal to `False`. `bool()` shows whether Python treats something as true or false.

```python
print(0 == False)
print(1 == True)
print(5 == False)
print("Too high." == False)
print(bool(0), bool(5), bool(""), bool("hi"))
```

Output:

```
True
True
False
False
False True False True
```

**Why you'd use it:** It explains why `if guess == False:` works when the guesses hit 0. Writing `guess == 0` does the same thing and says what you mean more clearly.

**Where I used it:** `if  guess == False:` on line 52.

---

## A parameter with the same name as a function

**What it is:** Inside a function, a **parameter name wins** over anything outside with the same name. Outside the function, nothing changes.

```python
def random_number():
    return 42

def check_guess(guess, random_number):
    print(random_number)

check_guess(10, 99)
print(random_number())
```

Output:

```
99
42
```

**Why you'd use it:** It's good to know why the code works: inside `check_guess`, `random_number` is the number I passed in, not the function. A different name (like `answer`) would make it easier to read.

**Where I used it:** `def check_guess(make_guess,random_number):` on line 20, with the function `random_number()` on line 17.
