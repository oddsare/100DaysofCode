# Day 21 Notes: Snake Game (Part 2)

> **AI generated.** These notes were written by AI (Claude) to explain the Python stuff I used on Day 21. Every example without a turtle window was run to make sure it works.

Code for this day: [`Assignment21.py`](Assignment21.py), with [`snake.py`](snake.py), [`food.py`](food.py) and [`scoreboard.py`](scoreboard.py)

---

## Inheritance with super().__init__()

**What it is:** `class Food(Turtle):` makes `Food` a **kind of Turtle**, so it gets everything a Turtle can do. `super().__init__()` runs the Turtle's own setup first, then I add my own.

```python
class Animal:
    def __init__(self):
        self.legs = 4

    def speak(self):
        print("...")

class Dog(Animal):
    def __init__(self):
        super().__init__()
        self.name = "Rex"

dog = Dog()
print(dog.legs, dog.name)
dog.speak()
```

Output:

```
4 Rex
...
```

**Why you'd use it:** The food and scoreboard **are** turtles with a few extras. Inheriting means I can call `self.goto()`, `self.color()` and `self.write()` without making a separate turtle.

**Where I used it:** Lines 4 to 7 of [`food.py`](food.py) and lines 8 to 11 of [`scoreboard.py`](scoreboard.py).

---

## Collisions with distance()

**What it is:** `distance()` gives how far apart two things are. If it's small enough, they're touching.

```python
import math

head = (0, 0)
food = (9, 12)
print(math.dist(head, food))
print(math.dist(head, food) < 15)
```

Output:

```
15.0
False
```

**Why you'd use it:** Turtle's `snake.head.distance(food)` does the same math. Under 15 means the snake ate the food. Under 10 from its own body means it crashed.

**Where I used it:** Line 32 for the food and line 43 for the tail.

---

## Skipping the head with [1::]

**What it is:** `[1::]` gives everything **from position 1 to the end**, the same as `[1:]`.

```python
segments = ["head", "body1", "body2"]
print(segments[1::])
print(segments[1:])
```

Output:

```
['body1', 'body2']
['body1', 'body2']
```

**Why you'd use it:** The head is always 0 away from itself, so it has to be skipped when checking if the head hit the tail.

**Where I used it:** `for part_of_snake in snake.snake[1::]:` on line 41.

---

## Growing at the tail with [-1]

**What it is:** `[-1]` gives the **last** item in a list.

```python
segments = ["head", "body1", "body2"]
tail = segments[-1]
segments.append("body3")
print(tail)
print(segments)
```

Output:

```
body2
['head', 'body1', 'body2', 'body3']
```

**Why you'd use it:** A new square goes where the tail is, then follows along on the next move.

**Where I used it:** `tail =self.snake[-1]` on line 50 of [`snake.py`](snake.py), and `add_snanke` on lines 52 to 57.

---

## Hitting the wall with or

**What it is:** Joining checks with `or` means **any one** being true is enough.

```python
x = 300
y = 0
print(x > 290 or x < -290 or y < -290 or y > 290)
```

Output:

```
True
```

**Why you'd use it:** The snake hits a wall if it goes past **any** of the 4 edges.

**Where I used it:** Line 38.

---

## Updating the score with clear() and write()

**What it is:** `write()` puts text on the screen, but it doesn't remove old text. `clear()` wipes what this turtle wrote, then `write()` puts the new score.

```py
def increase_score(self):
    self.clear()
    self.score += 1
    self.update_scoreboard()
```

**Why you'd use it:** Without `clear()`, the new score would be written right on top of the old one.

**Where I used it:** Lines 23 to 27 of [`scoreboard.py`](scoreboard.py).
