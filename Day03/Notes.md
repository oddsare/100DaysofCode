# Day 3 Notes: Treasure Island

> **AI generated.** These notes were written by AI (Claude) to explain the Python stuff I used on Day 3. Every example was run to make sure it works.

Code for this day: [`Assignment3.py`](Assignment3.py)

---

## Multi-line strings (triple quotes)

**What it is:** Normal strings have to stay on one line. If you use three quotes (`'''` or `"""`) instead of one, the string can go over as many lines as you want, and it keeps all the line breaks and spaces exactly how you typed them.

```python
boat = """
   |\\
   | \\
   |__\\
 \\------/
~~~~~~~~~~
"""
print(boat)
```

Output:

```

   |\
   | \
   |__\
 \------/
~~~~~~~~~~

```

**Why you'd use it:** ASCII art, long instructions, or any text that needs to keep its shape.

**Where I used it:** The treasure chest picture on lines 1 to 21 of `Assignment3.py`.

---

## Raw strings (r in front)

**What it is:** A backslash `\` normally means "something special is coming" (like `\n` for a new line). Putting an `r` in front of the string tells Python to ignore that and treat every backslash as a plain backslash. That's why the boat above needed `\\` everywhere, but with `r` it doesn't:

```python
boat = r"""
   |\
   | \
   |__\
 \------/
~~~~~~~~~~
"""
print(boat)

print("C:\new_folder")    # \n turns into a new line by accident
print(r"C:\new_folder")   # r keeps it as typed
```

Output:

```

   |\
   | \
   |__\
 \------/
~~~~~~~~~~

C:
ew_folder
C:\new_folder
```

**Why you'd use it:** ASCII art (it's full of backslashes) and Windows file paths. I also used this to fix the warnings in my Day 6 hangman pictures.

**Where I used it:** `chest= (r'''...''')` on line 1.

---

## Escaping quotes with \"

**What it is:** If your string is inside double quotes and you want a double quote *in* the text, Python thinks the string ended early. Putting a backslash in front (`\"`) tells Python "this quote is part of the text".

```python
print("Type \"left\" or \"right\"")
print('Type "left" or "right"')    # another way: use single quotes on the outside
```

Output:

```
Type "left" or "right"
Type "left" or "right"
```

**Why you'd use it:** To show quotes around words in a message, like the choices the player can type.

**Where I used it:** `Type \"Left\" or \"right\"` on line 26, and the door colors on line 32.

---

## if / elif / else

**What it is:** This is how the program makes decisions.

- `if` checks something. If it's true, the indented code underneath runs.
- `elif` (short for "else if") only gets checked if everything above it was false.
- `else` runs if *nothing* above was true.

Only **one** of the blocks runs, then Python skips the rest.

```python
door = "yellow"

if door == "red":
    print("It's a room full of fire. Game Over.")
elif door == "yellow":
    print("You found the treasure! You Win!")
else:
    print("You enter a room of beasts. Game Over.")
```

Output:

```
You found the treasure! You Win!
```

**Why you'd use it:** Any time the program should do different things depending on what happened, like what the player picked.

**Where I used it:** All over `Assignment3.py`, for example the door choice on lines 34 to 39.

---

## Comparison operators

**What it is:** These compare two things and give back `True` or `False`.

| Symbol | Means |
|---|---|
| `==` | equal to (two equals signs! one `=` is for making variables) |
| `!=` | not equal to |
| `>` | greater than |
| `<` | less than |
| `>=` | greater than or equal to |
| `<=` | less than or equal to |

```python
choice = "left"
print(choice == "left")
print(choice == "Left")    # capitals matter!
print(choice != "right")
print(5 > 3)
print(5 <= 3)
```

Output:

```
True
False
True
True
False
```

**Why you'd use it:** These are what go after `if` and `while` to check things.

**Where I used it:** `start_Treasure_hunt == "Left"` on line 28 and every other `if` in the file.

---

## Logical operators: and, or, not

**What it is:** These let you combine checks.

- `or`: true if **at least one** side is true.
- `and`: true only if **both** sides are true.
- `not`: flips true to false and false to true.

```python
choice = "left"
print(choice == "Left" or choice == "left")

lives = 3
has_key = True
print(lives > 0 and has_key)
print(not has_key)
```

Output:

```
True
True
False
```

**Heads up:** You have to write the full check on both sides. `choice == "Left" or "left"` looks right but is always `True`, because `"left"` on its own counts as true.

**Tip:** Instead of checking both `"Left"` and `"left"`, you can use `.lower()` to make the answer lowercase first (I did this on Day 6):

```python
choice = "LEFT"
if choice.lower() == "left":
    print("You went left")
```

Output:

```
You went left
```

**Why you'd use it:** When a decision depends on more than one thing.

**Where I used it:** `start_Treasure_hunt == "Left" or start_Treasure_hunt == "left"` on line 28.

---

## Nested if statements

**What it is:** Putting an `if` inside another `if`. The inside one only gets checked if the outside one was true. You can tell what's inside what by the indentation.

```python
direction = "left"
action = "wait"

if direction == "left":
    print("You come to a lake.")
    if action == "wait":
        print("A boat arrives.")
    else:
        print("You get attacked by an angry trout. Game Over.")
else:
    print("You fell into a hole. Game Over.")
```

Output:

```
You come to a lake.
A boat arrives.
```

**Why you'd use it:** For choices that lead to more choices, like a choose-your-own-adventure story.

**Where I used it:** The whole game is nested: the lake question (line 29) only happens if you went left, and the door question (line 32) only happens if you waited.

---

## Indentation

**What it is:** Python uses the spaces at the start of a line to know which code belongs to which `if`, `while`, or `for`. Everything indented under an `if` is "inside" it. The usual amount is 4 spaces.

```python
lives = 0
if lives == 0:
    print("Game Over")      # inside the if
    print("Try again?")     # also inside the if
print("Thanks for playing") # not inside, always runs
```

Output:

```
Game Over
Try again?
Thanks for playing
```

**Why you'd use it:** You don't have a choice, Python needs it. Messing up the indentation either crashes with an `IndentationError` or quietly runs the wrong code.

**Where I used it:** Every `if` block in `Assignment3.py`.

---

## Splitting a long line with \

**What it is:** A backslash at the very end of a line tells Python "this line keeps going on the next one". Also, two strings sitting next to each other get joined into one automatically.

```python
message = "You come to a lake. " \
    "There is an island in the middle."
print(message)
```

Output:

```
You come to a lake. There is an island in the middle.
```

**Why you'd use it:** To keep really long lines readable without scrolling sideways.

**Where I used it:** The lake question on lines 29 and 30, and the door question on lines 32 and 33.
