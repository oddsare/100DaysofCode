# Day 2 Notes: Tip Calculator

> **AI generated.** These notes were written by AI (Claude) to explain the Python stuff I used on Day 2. Every example was run to make sure it works.

Code for this day: [`Assignment2.py`](Assignment2.py)

---

## Data types: str, int, float

**What it is:** Every value in Python has a type. The three I used today:

- `str` (string): text, like `"hello"` or `"100"`. Note `"100"` in quotes is still text!
- `int` (integer): whole numbers, like `10` or `-3`.
- `float`: numbers with a decimal point, like `12.5` or `100.0`.

You can ask Python what type something is with `type()`:

```python
print(type("100"))
print(type(100))
print(type(100.5))
```

Output:

```
<class 'str'>
<class 'int'>
<class 'float'>
```

**Why you'd use it:** Python treats each type differently. `"10" + "5"` gives `"105"` (glued text), but `10 + 5` gives `15`. Knowing the type tells you what will happen.

**Where I used it:** `tip_amount1 = 10` on line 1 is an `int`. The bill the user types on line 6 is a `str`.

---

## Type conversion: float(), int(), str()

**What it is:** Since `input()` always gives back a string, you have to convert it before doing math. `float()` turns it into a decimal number, `int()` turns it into a whole number, and `str()` turns a number back into text.

```python
bill = "150.50"          # this is what input() would give me
print(bill + bill)       # glues the text together

bill = float(bill)
print(bill + bill)       # actually adds them

people = int("3")
print(people * 2)

print("People: " + str(people))
```

Output:

```
150.50150.50
301.0
6
People: 3
```

**Heads up:** `int("150.50")` crashes because `int()` can't handle a decimal point in text. Use `float()` for money.

**Why you'd use it:** Any time the user types a number and you want to do math with it.

**Where I used it:** `float(Bill_price)`, `float(Choosen_tip)` and `float(splitting)` on lines 8, 9 and 11.

---

## Math operators

**What it is:** The symbols Python uses for math.

| Symbol | What it does | Example | Answer |
|---|---|---|---|
| `+` | add | `7 + 2` | `9` |
| `-` | subtract | `7 - 2` | `5` |
| `*` | multiply | `7 * 2` | `14` |
| `/` | divide (always gives a float) | `7 / 2` | `3.5` |
| `//` | divide and drop the decimal | `7 // 2` | `3` |
| `%` | remainder after dividing | `7 % 2` | `1` |
| `**` | to the power of | `7 ** 2` | `49` |

```python
bill = 100
tip_percent = 12
tip = bill * tip_percent / 100
print(tip)
print(bill + tip)
print((bill + tip) / 3)
```

Output:

```
12.0
112.0
37.333333333333336
```

**Why you'd use it:** Pretty much every program needs math somewhere: prices, scores, lives left, and so on.

**Where I used it:** Lines 8, 9 and 11 of `Assignment2.py`.

---

## Order of operations and brackets

**What it is:** Python follows the same order as school math (PEMDAS / BODMAS): brackets first, then powers, then `*` and `/`, then `+` and `-`. If you want something done first, wrap it in brackets.

```python
print(2 + 3 * 4)
print((2 + 3) * 4)

bill = 100
tip = 12
print(bill / (100 / tip))   # how I wrote it on line 8
print(bill * tip / 100)     # same answer, a bit easier to read
```

Output:

```
14
20
12.0
12.0
```

**Why you'd use it:** So the math happens in the order you meant. Without the brackets on line 8, `bill / 100 / tip` would give a totally different (wrong) number.

**Where I used it:** `float(Bill_price) /(100/float(Choosen_tip))` on line 8.

---

## Rounding with :.2f in f-strings

**What it is:** Inside an f-string, you can put `:.2f` after a variable to show it with exactly 2 decimal places. The `2` is how many decimals, the `f` means "fixed point" (treat it like a decimal number).

```python
price = 37.333333333333336
print(f"Each person should pay: ${price:.2f}")
print(f"Rounded to 1 place: {price:.1f}")
print(f"No decimals: {price:.0f}")

print(round(price, 2))   # round() does the same thing but gives back a number
```

Output:

```
Each person should pay: $37.33
Rounded to 1 place: 37.3
No decimals: 37
37.33
```

**Heads up:** `:.2` (without the `f`) means 2 *significant digits*, not 2 decimals. That's why my first version printed `$37` instead of `$37.33`.

**Why you'd use it:** Money should always show 2 decimal places. Nobody wants to see `$37.333333333333336`.

**Where I used it:** `{split_price:.2f}` on line 12.
