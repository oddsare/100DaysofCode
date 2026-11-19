# Day 22 Notes: Pong

> **AI generated.** These notes were written by AI (Claude) to explain the Python stuff I used on Day 22. Every example without a turtle window was run to make sure it works.

Code for this day: [`Assignment22.py`](Assignment22.py), with [`paddle.py`](paddle.py), [`ball.py`](ball.py) and [`scoreboard.py`](scoreboard.py)

---

## Giving a class values when you make it

**What it is:** `__init__` can take **parameters**, just like a function. The values go in the brackets when you make the object.

```python
class Paddle:
    def __init__(self, x, y):
        self.x = x
        self.y = y

l_paddle = Paddle(-350, 0)
r_paddle = Paddle(350, 0)
print(l_paddle.x, r_paddle.x)
```

Output:

```
-350 350
```

**Why you'd use it:** One `Paddle` class makes both paddles, each in its own spot.

**Where I used it:** `def __init__(self,paddle_x,paddle_y):` on line 4 of [`paddle.py`](paddle.py), and `Paddle(-350,0)` and `Paddle(350,0)` on lines 9 and 10.

---

## Bouncing with *= -1

**What it is:** `y_move *= -1` means `y_move = y_move * -1`. It **flips the sign**, so the ball goes the other way.

```python
y_move = 10
y_move *= -1
print(y_move)
y_move *= -1
print(y_move)
```

Output:

```
-10
10
```

**Why you'd use it:** Flip `y_move` to bounce off the top or bottom. Flip `x_move` to bounce off a paddle.

**Where I used it:** `bounce_wall` and `bounce_paddle` on lines 18 to 21 of [`ball.py`](ball.py).

---

## Moving by adding to x and y

**What it is:** Each frame, add the move amounts to the ball's current spot, then go there.

```python
x, y = 0, 0
x_move, y_move = 10, 10
for frame in range(3):
    x = x + x_move
    y = y + y_move
    print(x, y)
```

Output:

```
10 10
20 20
30 30
```

**Why you'd use it:** It moves the ball diagonally, and the bounce methods only have to flip one number.

**Where I used it:** `move` on lines 13 to 16 of [`ball.py`](ball.py).

---

## Speeding up with max() and round()

**What it is:** `round(n, 4)` cleans up messy decimals. `max(0.0, n)` picks the **bigger** number, so `n` can never go below 0.

```python
n = 0.1 - 0.01 - 0.01 - 0.01
print(n)

n = 0.1
for point in range(3):
    n = max(0.0, round(n - 0.01, 4))
print(n)

for point in range(12):
    n = max(0.0, round(n - 0.01, 4))
print(n)
```

Output:

```
0.07000000000000002
0.07
0.0
```

**Why you'd use it:** Each point makes `time.sleep(n)` shorter, so the game gets faster. `time.sleep()` crashes on a negative number, and `max` stops that.

**Where I used it:** Lines 75 and 81.

---

## Drawing a dashed line

**What it is:** Lift the pen, move, put it down, move, and repeat. That makes gaps between the dashes.

```py
for i in range(19):
    turtle.penup()
    turtle.forward(20)
    turtle.pendown()
    turtle.forward(10)
```

**Why you'd use it:** It draws the net down the middle of the court.

**Where I used it:** Lines 46 to 51.
