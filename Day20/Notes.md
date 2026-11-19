# Day 20 Notes: Snake Game (Part 1)

> **AI generated.** These notes were written by AI (Claude) to explain the Python stuff I used on Day 20. Every example without a turtle window was run to make sure it works.

Code for this day: [`Assignment20.py`](Assignment20.py), with [`snake.py`](snake.py)

---

## tracer(0) and update()

**What it is:** `screen.tracer(0)` **turns off auto drawing**. Nothing shows on screen until `screen.update()` is called, then everything moves at once.

```py
screen.tracer(0)
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.snake_move()
```

**Why you'd use it:** Without it, you'd see each square move one by one, and the snake would look like it's breaking apart.

**Where I used it:** `screen.tracer(0)` on line 10 and `screen.update()` on line 21.

---

## A game loop with time.sleep

**What it is:** A game is a `while` loop that runs over and over. Each time round is one **frame**. `time.sleep(0.1)` pauses for 0.1 seconds, so the game runs at a steady speed.

```python
import time

for frame in range(3):
    print("frame", frame)
    time.sleep(0.1)
```

Output:

```
frame 0
frame 1
frame 2
```

**Why you'd use it:** Without the pause, the snake would move as fast as the computer can go.

**Where I used it:** Lines 20 to 24.

---

## Moving the snake from the back

**What it is:** `range(start, stop, -1)` **counts backwards**. Each part of the snake moves to where the part **in front of it** was. Then the head moves forward.

```python
print(list(range(2, 0, -1)))

snake = [(0, 0), (-20, 0), (-40, 0)]
for seg in range(len(snake) - 1, 0, -1):
    snake[seg] = snake[seg - 1]
snake[0] = (20, 0)
print(snake)
```

Output:

```
[2, 1]
[(20, 0), (0, 0), (-20, 0)]
```

**Why you'd use it:** It has to go back to front. If the front moved first, the part behind it would copy the **new** spot and the snake would bunch up.

**Where I used it:** `for seg in range(len(self.snake)-1,0,-1):` on line 29 of [`snake.py`](snake.py).

---

## Passing a function without brackets

**What it is:** `snake.up` (no brackets) is **the method itself**. `snake.up()` (with brackets) **runs it now**. `onkey` needs the method itself so it can run it later, when the key is pressed.

```python
def up():
    print("going up")

def press(key_function):
    key_function()

press(up)
```

Output:

```
going up
```

**Why you'd use it:** It hooks each arrow key to the right method.

**Where I used it:** `screen.onkey(snake.up,"Up")` and the other arrow keys on lines 13 to 16.

---

## Constants and the no-reverse rule

**What it is:** A **constant** is a variable in ALL CAPS at the top of a file that never changes. It gives a number a name, like `UP = 90`.

```python
UP = 90
DOWN = 270

heading = DOWN
if heading != DOWN:
    heading = UP
print(heading)
```

Output:

```
270
```

**Why you'd use it:** `UP` is easier to read than `90`. The `if` stops the snake turning straight back into itself: if it's going down, pressing up does nothing.

**Where I used it:** Constants on lines 2 to 6 of [`snake.py`](snake.py), and the `up`, `down`, `left` and `right` methods on lines 37 to 50.

---

## A class that holds the snake's parts

**What it is:** The `Snake` class keeps a **list of square turtles** in `self.snake`. The first one, `self.snake[0]`, is the head.

```py
class Snake:
    def __init__(self):
        self.snake = []
        self.make_square()
        self.head = self.snake[0]
```

**Why you'd use it:** The main file just says `snake.snake_move()`, and the class handles all the squares.

**Where I used it:** Lines 9 to 25 of [`snake.py`](snake.py).
