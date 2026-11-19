# Day 18 Notes: Spot Painting (Turtle)

> **AI generated.** These notes were written by AI (Claude) to explain the Python stuff I used on Day 18. Every example without a turtle window was run to make sure it works.

Code for this day: [`Assignment18.py`](Assignment18.py), with [`image.jpg`](image.jpg)

---

## Installing a package with pip

**What it is:** `colorgram` isn't built into Python, so it has to be installed first. In the terminal:

```text
pip install colorgram.py
```

(The install name is `colorgram.py`, but in the code it's just `import colorgram`.)

**Why you'd use it:** `colorgram.extract('image.jpg', 30)` pulls the 30 main colors out of a picture, so the painting uses real colors from it.

**Where I used it:** `import colorgram` on line 6 and `colorgram.extract('image.jpg', 30)` on line 20.

---

## RGB colors as tuples

**What it is:** A color can be 3 numbers from 0 to 255: **red, green, blue**. Putting them in round brackets makes a **tuple**. It works like a list, but it can't be changed.

```python
r = 232
g = 12
b = 50
new_color = (r, g, b)
print(new_color)
print(new_color[0])
```

Output:

```
(232, 12, 50)
232
```

Turtle only accepts 0 to 255 numbers after `colormode(255)`:

```py
import turtle
turtle.colormode(255)
tim.dot(20, (232, 12, 50))
```

**Why you'd use it:** colorgram gives each color's `r`, `g` and `b`, and the tuple turns them into one color turtle can use.

**Where I used it:** `turtle.colormode(255)` on line 7, and building the tuples on lines 21 to 27.

---

## Picking a random item by its position

**What it is:** `random.randint(2, len(colors) - 1)` picks a random **position**, then `colors[position]` gets that item. Starting at 2 skips the first two items.

```python
import random

colors = ["white", "beige", "red", "blue", "green"]
index = random.randint(2, len(colors) - 1)
print(colors[index])
```

Output (random, yours will be different):

```
blue
```

**Why you'd use it:** colorgram lists the most common colors first, which in a painting photo is usually the background. Skipping them keeps the dots colorful.

**Where I used it:** `random.randint(2,(len(color)-1))` on line 13.

---

## A loop inside a loop (making a grid)

**What it is:** The **inner** loop makes one row. The **outer** loop moves up and runs the inner loop again. The x value has to be **reset** at the start of each row.

```python
long = 0
for i in range(3):
    row = []
    lat = 0
    for j in range(3):
        row.append((lat, long))
        lat += 50
    print(row)
    long += 50
```

Output:

```
[(0, 0), (50, 0), (100, 0)]
[(0, 50), (50, 50), (100, 50)]
[(0, 100), (50, 100), (100, 100)]
```

**Why you'd use it:** It makes a 10 by 10 grid of dots. Without `lat= -225` at the start of each row, every new row would keep going further right.

**Where I used it:** Lines 29 to 37.

---

## teleport and dot

**What it is:** `teleport(x, y)` jumps the turtle to a spot **without drawing a line**. `dot(size, color)` draws a filled circle where the turtle is.

```py
tim.teleport(-225, -225)
tim.dot(20, (232, 12, 50))
```

**Why you'd use it:** Each dot goes in its own spot with no lines between them. (`teleport` needs Python 3.12 or newer. On older versions, use `penup()` then `goto()`.)

**Where I used it:** Lines 15 and 16.
