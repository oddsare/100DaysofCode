# Day 23 Notes: Turtle Crossing

> **AI generated.** These notes were written by AI (Claude) to explain the Python stuff I used on Day 23. Every example without a turtle window was run to make sure it works.

Code for this day: [`Assignment23.py`](Assignment23.py), with [`player.py`](player.py), [`car_manager.py`](car_manager.py) and [`scoreboard.py`](scoreboard.py)

---

## Is a Turtle vs has Turtles

**What it is:** There are two ways to use another class:

- **Inheritance** (`class Player(Turtle):`): the player **is** a turtle.
- **Holding them in a list**: the `CarManager` isn't a turtle. It **has** a list of car turtles.

```python
class Car:
    def __init__(self, color):
        self.color = color

class CarManager:
    def __init__(self):
        self.group_cars = []

    def add_car(self, color):
        self.group_cars.append(Car(color))

manager = CarManager()
manager.add_car("red")
manager.add_car("blue")
print(len(manager.group_cars))
print(manager.group_cars[0].color)
```

Output:

```
2
red
```

**Why you'd use it:** When `CarManager` inherited from `Turtle`, the manager itself was a turtle, so an extra arrow showed up in the middle of the screen. The manager only needs to **hold** cars, not **be** one.

**Where I used it:** `class Player(Turtle):` on line 9 of [`player.py`](player.py). `class CarManager():` and `self.group_cars = []` on lines 11 to 14 of [`car_manager.py`](car_manager.py).

---

## Doing something only sometimes

**What it is:** `random.randint(1, 6) == 1` is `True` about **1 time in 6**.

```python
import random

cars_made = 0
for frame in range(600):
    if random.randint(1, 6) == 1:
        cars_made += 1
print(cars_made)
```

Output (random, it's usually close to 100):

```
97
```

**Why you'd use it:** A new car every frame would fill the road. One in 6 frames spaces them out.

**Where I used it:** Lines 19 and 20 of [`car_manager.py`](car_manager.py).

---

## A method that answers True or False

**What it is:** A method can do some work **and** return `True` or `False`, so the main loop knows what happened.

```python
FINISH_LINE_Y = 280

class Player:
    def __init__(self):
        self.y = -280
        self.level = 1

    def reached_finish(self):
        if self.y > FINISH_LINE_Y:
            self.y = -280
            self.level += 1
            return True
        return False

player = Player()
speed = 10
player.y = 290
if player.reached_finish():
    speed += 10
print(player.level, speed, player.y)
```

Output:

```
2 20 -280
```

**Why you'd use it:** The player class sends the player back to the start and goes up a level, and the main loop uses the `True` to speed up the cars.

**Where I used it:** `player_check_distance` on lines 28 to 39 of [`player.py`](player.py), used on lines 31 to 35 of [`Assignment23.py`](Assignment23.py).

---

## Looping through every car

**What it is:** A `for` loop over the list touches **every** car, so one check covers them all.

```python
import math

cars = [(100, 50), (5, 3), (-200, 0)]
player = (0, 0)
for car in cars:
    if math.dist(player, car) < 20:
        print("Hit at", car)
```

Output:

```
Hit at (5, 3)
```

**Why you'd use it:** Every car needs to move, and every car needs a crash check.

**Where I used it:** `for a_car in (self.group_cars):` on line 35 of [`car_manager.py`](car_manager.py), and the crash check on lines 37 to 41 of [`Assignment23.py`](Assignment23.py).

---

## onkeypress vs onkey

**What it is:** `onkeypress` runs the method **the moment the key goes down**. `onkey` waits until the key is **let go**.

```py
screen.onkeypress(player.moving_forward, "Up")
```

**Why you'd use it:** The turtle moves as soon as you press Up.

**Where I used it:** Line 15.
