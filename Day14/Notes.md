# Day 14 Notes: Higher Lower

> **AI generated.** These notes were written by AI (Claude) to explain the Python stuff I used on Day 14. Every example was run to make sure it works.

Code for this day: [`Assignment14.py`](Assignment14.py) and [`game_data.py`](game_data.py)

---

## Importing my own file with a nickname

**What it is:** `import game_data as gd` loads my other file `game_data.py` and lets me call it **`gd`** for short. Everything in that file is then reached with `gd.` in front.

```python
import game_data as gd

print(len(gd.data))
print(gd.data[0]["name"])
```

Output:

```
50
Instagram
```

**Why you'd use it:** It keeps the big list of people in its own file, so the game code stays short.

**Where I used it:** `import game_data as gd` on line 2.

---

## A list of dictionaries

**What it is:** `gd.data` is a **list**, and each item in it is a **dictionary**. First pick the item by its position, then pick the value by its key.

```python
data = [
    {"name": "Ann", "follower_count": 300},
    {"name": "Bob", "follower_count": 120},
]
person = data[0]
print(person["name"])
print(data[1]["follower_count"])
```

Output:

```
Ann
120
```

**Why you'd use it:** Each person has a name, description, country and follower count. A dictionary keeps them together, and the list holds all the people.

**Where I used it:** `person1["follower_count"] > person2["follower_count"]` on line 31.

---

## Slicing a list with [1:]

**What it is:** `[1:]` gives a copy of the list **starting at position 1**, so it skips the first item. `[:2]` gives the first two. `[-1]` gives the last one.

```python
letters = ["a", "b", "c", "d"]
print(letters[1:])
print(letters[:2])
print(letters[-1])
```

Output:

```
['b', 'c', 'd']
['a', 'b']
d
```

**Why you'd use it:** `random.choice(gd.data[1:])` picks a random person but never picks the first one (Instagram).

**Where I used it:** `return random.choice(gd.data[1:])` on line 27.

---

## Moving B into A's spot

**What it is:** `person1 = person2` copies B into A. Then `person2` gets a new random person, so one person stays for the next round.

```python
person1 = "Ann"
person2 = "Bob"

person1 = person2
person2 = "Cat"
print(person1, person2)
```

Output:

```
Bob Cat
```

**Why you'd use it:** It keeps one of the two people on screen each round instead of picking two new ones.

**Where I used it:** Lines 47 to 53.

---

## A while True loop that re-picks

**What it is:** `while True:` loops forever until it hits `break`. Inside, keep picking a new person until the two are different.

```python
import random

people = ["Ann", "Bob", "Cat"]
person1 = "Ann"
person2 = "Ann"

while True:
    if person1 == person2:
        person2 = random.choice(people)
    else:
        break

print(person1 != person2)
```

Output:

```
True
```

**Why you'd use it:** It stops the same person (or two people with the same follower count) showing up as A and B.

**Where I used it:** Lines 55 to 61.

---

## .capitalize()

**What it is:** `.capitalize()` makes the **first letter uppercase** and the rest lowercase.

```python
print("a".capitalize())
print("hELLO".capitalize())
print("B".capitalize())
```

Output:

```
A
Hello
B
```

**Why you'd use it:** The player can type `a` or `A` and it still matches `"A"`.

**Where I used it:** `input(...).capitalize()` on line 71.

---

## Quotes inside an f-string

**What it is:** Inside an f-string, a dictionary key needs quotes too. Using **single quotes inside double quotes** works in every Python version. Using the **same** quotes inside only works in **Python 3.12 or newer**.

```python
person = {"name": "Ann"}
print(f"Name: {person['name']}")
print(f"Name: {person["name"]}")
```

Output:

```
Name: Ann
Name: Ann
```

**Why you'd use it:** If the game crashes with a `SyntaxError` on an older Python, switching to single quotes inside fixes it.

**Where I used it:** `{person1["name"]}` on lines 64 and 66.

---

## A one-line if (and clearing the screen)

**What it is:** `A if condition else B` picks between two values in one line.

```python
score = 7
result = "win" if score > 5 else "lose"
print(result)
```

Output:

```
win
```

**Why you'd use it:** My `clear()` function uses it to pick the right command: `cls` on Windows, `clear` on Mac and Linux. `os.system()` runs that command in the terminal.

```py
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
```

**Where I used it:** Lines 23 and 24.
