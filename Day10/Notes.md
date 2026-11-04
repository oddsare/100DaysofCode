# Day 10 Notes: Calculator

> **AI generated.** These notes were written by AI (Claude) to explain the Python stuff I used on Day 10. Every example was run to make sure it works.

Code for this day: [`Assignment10.py`](Assignment10.py) (version 1, with `if`/`elif` and error checks) and [`Assignment10_v2.py`](Assignment10_v2.py) (version 2, with a dictionary of functions)

---

## return (functions that give an answer back)

**What it is:** On Day 8 my functions just printed things. `return` sends a value **back out** of the function, so the code that called it can save it or use it. The function stops as soon as it hits `return`.

```python
def add(n1, n2):
    return n1 + n2

answer = add(2, 3)
print(answer)
print(add(10, 5) * 2)
```

Output:

```
5
30
```

**Heads up:** If a function has no `return`, it gives back `None`, Python's word for "nothing":

```python
def add_no_return(n1, n2):
    n1 + n2

print(add_no_return(2, 3))
```

Output:

```
None
```

**Why you'd use it:** So a function can work something out and hand you the answer, instead of only printing it. You can't do math with something that was only printed.

**Where I used it:** `add`, `divide`, `mult` and `sub` on lines 23 to 33 of `Assignment10.py`.

---

## Storing a function in a variable

**What it is:** A function is a value, just like a number or a string. Write its name **without brackets** and you can put it in a variable. Then the variable works like the function: put brackets after it to run it.

```python
def add(n1, n2):
    return n1 + n2

def mult(n1, n2):
    return n1 * n2

current_function = add
print(current_function(3, 4))

current_function = mult
print(current_function(3, 4))
```

Output:

```
7
12
```

**Heads up:** No brackets when you store it. `current_function = add()` would try to **run** `add` right there, with no numbers, and crash.

**Why you'd use it:** You pick the function once (from what the user typed), and then one line does the math, whichever operation it is.

**Where I used it:** `Current_function =add` on line 43, choosing it on lines 61 to 68, and running it with `Current_function(number,next_number)` on line 76 of `Assignment10.py`.

---

## Comparing functions with ==

**What it is:** Since a function is a value, you can check which one a variable is holding.

```python
def add(n1, n2):
    return n1 + n2

def divide(n1, n2):
    return n1 / n2

current_function = divide
print(current_function == divide)
print(current_function == add)
```

Output:

```
True
False
```

**Why you'd use it:** To only do something for one operation, like blocking division by 0.

**Where I used it:** `while Current_function == divide and next_number == 0:` on line 72 of `Assignment10.py`.

---

## A dictionary of functions

**What it is:** Dictionary values can be functions too (Day 9 dictionaries + Day 10 functions). Look up the function by its key, then put brackets after it to run it.

```python
def add(n1, n2):
    return n1 + n2

def sub(n1, n2):
    return n1 - n2

operations = {"+": add, "-": sub}

symbol = "-"
print(operations[symbol](10, 3))
```

Output:

```
7
```

`operations[symbol]` gets the `sub` function, and `(10, 3)` runs it.

**Why you'd use it:** It replaces a whole `if`/`elif` chain with one line. To add a new operation, you just add one entry to the dictionary.

**Where I used it:** `operation = {...}` on lines 36 to 41 and `operation[operator](number,next_number)` on line 54 of `Assignment10_v2.py`.

---

## try / except (catching an error instead of crashing)

**What it is:** Put code that might crash inside `try`. If it crashes with the error named after `except`, Python runs the `except` part instead of stopping the whole program.

```python
for answer in ["12", "abc", "3.5"]:
    try:
        number = float(answer)
        print(f"Got {number}")
    except ValueError:
        print(f"'{answer}' is not a number")
```

Output:

```
Got 12.0
'abc' is not a number
Got 3.5
```

**Why you'd use it:** Users type all sorts of things. Without this, typing a letter where a number should go ends the program with a `ValueError`. (The course covers this properly around Day 30, so this is a sneak peek.)

**Where I used it:** Lines 37 to 40 of `Assignment10.py`.

---

## A function that keeps asking until the answer is OK

**What it is:** Put the `try` inside a `while True` loop. If the answer works, `return` hands it back and ends the loop (and the function). If not, the `except` prints a message and the loop asks again.

```python
def get_number(question):
    while True:
        try:
            return float(input(question))
        except ValueError:
            print("That's not a number, try again.")

age = get_number("How old are you? ")
print(age)
```

Output (if I type `abc`, then `12`):

```
How old are you? abc
That's not a number, try again.
How old are you? 12
12.0
```

**Why you'd use it:** You write the "keep asking" part once and use it for every number question.

**Where I used it:** `def get_number` on lines 35 to 40, used on lines 52 and 71 of `Assignment10.py`.

---

## while True (a loop that runs forever)

**What it is:** `while True:` never stops on its own, because `True` is always true. The only ways out are `break`, `return` (inside a function), `exit()`, or pressing `Ctrl + C`.

```python
count = 0
while True:
    count += 1
    print(count)
    if count == 3:
        break
print("out of the loop")
```

Output:

```
1
2
3
out of the loop
```

**Heads up:** My calculator's main loop has no `break`, so it goes on until I press `Ctrl + C`. That also means lines 84 and 85, which come after the loop, never run.

**Why you'd use it:** When something should keep going until something happens inside it, like a program that keeps calculating until the user quits.

**Where I used it:** Line 49 of `Assignment10.py` (and in `get_number` on line 36).

---

## One-line if / else

**What it is:** `value_1 if check else value_2` picks one of two values in a single line. It's like a mini `if`/`else` that gives back a value.

```python
score = 85
result = "pass" if score >= 50 else "fail"
print(result)

score = 30
print("pass" if score >= 50 else "fail")
```

Output:

```
pass
fail
```

**Why you'd use it:** To choose between two values without writing four lines of `if`/`else`.

**Where I used it:** `'cls' if os.name == 'nt' else 'clear'` on line 21 of `Assignment10.py`.

---

## Clearing the screen with os

**What it is:** `import os` gives you tools for talking to the computer's operating system. `os.system()` runs a terminal command. The clear-screen command is `cls` on Windows and `clear` on Mac and Linux, and `os.name` is `'nt'` on Windows, so the one-line `if` picks the right one.

```python
import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

clear()
```

This one clears the screen, so there's no output to show.

**Heads up:** Some code editors' output panels (like IDLE, or VS Code's Output tab) aren't real terminals, so it may do nothing there, or print odd symbols. It works in a normal terminal or Command Prompt.

**Why you'd use it:** A real clear instead of the `"\n" * 100` trick from Day 9.

**Where I used it:** `import os` on line 1, `def clear()` on lines 20 and 21, and `clear()` on line 81 of `Assignment10.py`.

---

**Also used today (explained in earlier notes):** `def` and parameters ([Day 8](../Day08/Notes.md)), `float(input())` ([Day 2](../Day02/Notes.md)), `if`/`elif`, `and`, `or` ([Day 3](../Day03/Notes.md)), dictionaries ([Day 9](../Day09/Notes.md)), f-strings ([Day 1](../Day01/Notes.md)), raw strings for the logo ([Day 3](../Day03/Notes.md)).
