# Day 13 Notes: Debugging

> **AI generated.** These notes were written by AI (Claude) to explain the Python stuff I used on Day 13. Every example was run to make sure it works.

Code for this day: [`Assignment13.py`](Assignment13.py)

---

## `=` vs `==`

**What it is:** `=` **puts a value into a variable**. `==` **checks if two things are equal** and gives `True` or `False`. Using `=` inside an `if` is an error.

```python
number = 4
print(number % 2 == 0)
number = 7
print(number % 2 == 0)
```

Output:

```
True
False
```

This is what Python 3.13 says if you use `=` by mistake:

```py
if number % 2 = 0:
# SyntaxError: cannot assign to expression here. Maybe you meant '==' instead of '='?
```

**Why you'd use it:** Every `if` that compares two things needs `==`.

**Where I used it:** The bug is on line 3 and the fix is on line 9.

---

## Test with answers you already know

**What it is:** A typo in a number (like `4000` instead of `400`) doesn't cause an error. The code just gives wrong answers. The way to catch it is to **test with inputs where you already know the answer**.

```python
def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

print(is_leap(2000))
print(is_leap(1900))
print(is_leap(2024))
print(is_leap(2023))
```

Output:

```
True
False
True
False
```

**Why you'd use it:** 2000 **is** a leap year. With `4000` in the code, `is_leap(2000)` gave `False`, which shows the bug right away.

**Where I used it:** The bug is on line 18 and the fix is on line 31.

---

## `and` vs `or`

**What it is:** `or` is `True` if **either** side is true. `and` is `True` only if **both** sides are true.

```python
number = 6
print(number % 3 == 0 or number % 5 == 0)
print(number % 3 == 0 and number % 5 == 0)

number = 15
print(number % 3 == 0 and number % 5 == 0)
```

Output:

```
True
False
True
```

**Why you'd use it:** FizzBuzz is for numbers divisible by 3 **and** 5. With `or`, 6 printed "FizzBuzz" too.

**Where I used it:** The bug is on line 45 and the fix is on line 59.

---

## Separate `if`s vs `elif`

**What it is:** Separate `if`s are **all** checked, so more than one can run. With `elif`, Python **stops at the first one that's true**.

```python
number = 15

print("With separate ifs:")
if number % 3 == 0 and number % 5 == 0:
    print("FizzBuzz")
if number % 3 == 0:
    print("Fizz")
if number % 5 == 0:
    print("Buzz")

print("With elif:")
if number % 3 == 0 and number % 5 == 0:
    print("FizzBuzz")
elif number % 3 == 0:
    print("Fizz")
elif number % 5 == 0:
    print("Buzz")
```

Output:

```
With separate ifs:
FizzBuzz
Fizz
Buzz
With elif:
FizzBuzz
```

**Why you'd use it:** Each number should print **one** thing. Also, an `else` only belongs to the `if` right above it. In the broken version, 3 printed "FizzBuzz", "Fizz" and "[3]": the `or` matched, then the `if % 3` matched, then the `else` ran because it only checks `% 5`.

**Where I used it:** The broken version is on lines 45 to 52 and the fixed version is on lines 59 to 66.

---

## print([x]) vs print(x)

**What it is:** Square brackets around a value make it a **list**, so `print([number])` shows the brackets too.

```python
number = 7
print([number])
print(number)
```

Output:

```
[7]
7
```

**Why you'd use it:** To print just the number, leave the brackets off.

**Where I used it:** The bug is on line 52 and the fix is on line 66.
