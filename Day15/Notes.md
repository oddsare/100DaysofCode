# Day 15 Notes: Coffee Machine

> **AI generated.** These notes were written by AI (Claude) to explain the Python stuff I used on Day 15. Every example was run to make sure it works.

Code for this day: [`Assignment15.py`](Assignment15.py)

---

## Nested dictionaries

**What it is:** A dictionary can hold **another dictionary** as a value. Use one `[ ]` for each level you go down.

```python
MENU = {
    "latte": {
        "ingredients": {"water": 200, "milk": 150, "coffee": 24},
        "cost": 2.5,
    },
}
print(MENU["latte"]["cost"])
print(MENU["latte"]["ingredients"]["milk"])
```

Output:

```
2.5
150
```

**Why you'd use it:** Each drink has a cost **and** a set of ingredients, all under one name.

**Where I used it:** `menu_drinks[order]["ingredients"]["water"]` from line 47 on.

---

## global

**What it is:** A function can **read** a variable from outside, but to **change** it, the function needs `global` first. Without it, `earnings += price` crashes with `UnboundLocalError`.

```python
earnings = 0

def sell(price):
    global earnings
    earnings += price

sell(2.5)
sell(1.5)
print(earnings)
```

Output:

```
4.0
```

**Why you'd use it:** The machine's total money needs to grow every time a drink is sold.

**Where I used it:** `global earnings` on line 15.

---

## `>` vs `>=`

**What it is:** `>` means "more than". `>=` means "more than **or equal to**".

```python
price = 1.5
paid = 1.5
print(paid > price)
print(paid >= price)
```

Output:

```
False
True
```

**Why you'd use it:** Paying the **exact** price should still get you a drink, so it needs `>=`.

**Where I used it:** `if total >= order:` on line 23.

---

## Money with :.2f

**What it is:** Computers can't store some decimals exactly, so money math can give long, messy numbers. `:.2f` in an f-string **shows 2 decimal places**.

```python
total = (3 * 0.25) + (1 * 0.1) + (1 * 0.05)
change = total - 0.7
print(change)
print(f"{change:.2f}")
```

Output:

```
0.20000000000000007
0.20
```

**Why you'd use it:** Change should look like `$0.20`, not `$0.20000000000000007`.

**Where I used it:** `{left_over:.2f}` on lines 104 and 112.

---

## Brackets with and / or

**What it is:** Python does `and` **before** `or`, like times before plus in math. Brackets make it check the part inside first.

```python
is_espresso = True
low_water = False
low_coffee = True
print(is_espresso and (low_water or low_coffee))

is_espresso = False
print(is_espresso and low_water or low_coffee)
print(is_espresso and (low_water or low_coffee))
```

Output:

```
True
True
False
```

**Why you'd use it:** I want "it's an espresso **and** (low on water **or** low on coffee)". Without brackets, any order with low coffee would match.

**Where I used it:** `elif order == "espresso" and (water < ... or coffee < ...)` on line 115.

---

## not in

**What it is:** `in` checks if something is inside a list or dictionary. `not in` checks that it **isn't**. For a dictionary, it checks the **keys**.

```python
menu = {"latte": 2.5, "espresso": 1.5}
print("mocha" not in menu)
print("latte" not in menu)
```

Output:

```
True
False
```

**Why you'd use it:** To catch an order that isn't on the menu.

**Where I used it:** `elif order not in menu_drinks:` on line 85.

---

## exit()

**What it is:** `exit()` **stops the whole program** right there.

```python
print("before")
exit()
print("after")
```

Output:

```
before
```

**Why you'd use it:** Typing `off` turns the machine off.

**Where I used it:** Line 81.
