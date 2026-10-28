# Day 8 Notes: Caesar Cipher

> **AI generated.** These notes were written by AI (Claude) to explain the Python stuff I used on Day 8. Every example was run to make sure it works.

Code for this day: [`Assignment8.py`](Assignment8.py) (separate `encode` and `decode` functions) and [`TogetherAssignment8.py`](TogetherAssignment8.py) (one `encryption` function that does both)

---

## Functions: def

**What it is:** A function is a block of code with a name. You write it once with `def`, and then you can run it whenever you want by "calling" it: writing its name with brackets after it. The code inside only runs when you call it, not when Python first reads the `def`.

```python
def greet():
    print("Hello!")
    print("Welcome to the cipher.")

greet()
greet()
```

Output:

```
Hello!
Welcome to the cipher.
Hello!
Welcome to the cipher.
```

**Heads up:** You have to `def` the function **before** the line that calls it, or Python says `NameError` because it doesn't know that name yet.

**Why you'd use it:** So you don't copy and paste the same code. If something needs fixing, you fix it in one place. It also gives a chunk of code a name that says what it does, like `encode`.

**Where I used it:** `def encode` (line 21) and `def decode` (line 34) in `Assignment8.py`.

---

## Parameters and arguments (giving a function inputs)

**What it is:** The names in the brackets of a `def` are **parameters**. They're like empty variables waiting for a value. When you call the function, the values you pass in are **arguments**, and they get put into the parameters in order.

```python
def encode(message, shift_amount):
    print(f"Encoding '{message}' with a shift of {shift_amount}")

encode("hello", 5)
encode("abc", 3)
```

Output:

```
Encoding 'hello' with a shift of 5
Encoding 'abc' with a shift of 3
```

**Heads up:** The order matters. `encode(5, "hello")` would put `5` into `message` and `"hello"` into `shift_amount`.

**Tip:** You can also name the arguments when you call the function. Then the order doesn't matter (these are called keyword arguments):

```python
def encode(message, shift_amount):
    print(f"Encoding '{message}' with a shift of {shift_amount}")

encode(shift_amount=2, message="zebra")
```

Output:

```
Encoding 'zebra' with a shift of 2
```

**Why you'd use it:** So one function can work on different data every time, like any message with any shift.

**Where I used it:** `encode(text,shift)` and `decode(text,shift)` on lines 52 and 54 of `Assignment8.py`, and `encryption(direction,text,shift)` on line 72 of `TogetherAssignment8.py`.

---

## Using a parameter to decide what to do

**What it is:** A parameter can hold a choice, not just data. Inside the function, an `if` checks it and does different things.

```python
def encryption(direction, shift_amount):
    if direction == "encode":
        print(f"Shifting forward {shift_amount}")
    else:
        print(f"Shifting back {shift_amount}")

encryption("encode", 5)
encryption("decode", 5)
```

Output:

```
Shifting forward 5
Shifting back 5
```

**Why you'd use it:** Encoding and decoding are almost the same steps, just in opposite directions. One function with a `direction` parameter means no copied code. That's the whole point of `TogetherAssignment8.py`.

**Where I used it:** `if direction == "encode":` on line 23 of `TogetherAssignment8.py`.

---

## Turning a number negative with * -1

**What it is:** Multiplying by `-1` flips a number's sign: positive becomes negative and negative becomes positive.

```python
shift = 5
print(shift * -1)

shift = shift * -1
print(shift)
print(shift * -1)
```

Output:

```
-5
-5
5
```

**Why you'd use it:** Decoding is just encoding backwards. If I flip the shift to negative, the same `+ shift_amount` math moves the letters back instead of forward.

**Where I used it:** `shift_amount = shift_amount * -1` on line 28 and `26*-1` on line 25 of `TogetherAssignment8.py`.

---

## .index() (finding where something is in a list)

**What it is:** `.index()` tells you the position of an item in a list. It's the opposite of `alphabet[2]`: instead of "what's at position 2?", it asks "what position is `"c"` at?"

```python
alphabet = ["a", "b", "c", "d", "e"]
print(alphabet.index("c"))
print(alphabet.index("a"))

letter = "e"
position = alphabet.index(letter)
print(alphabet[position])
```

Output:

```
2
0
e
```

**Heads up:** If the item isn't in the list, `.index()` crashes with a `ValueError`. That's why my code checks `if message[i] in alphabet:` first, so spaces and numbers get skipped instead of crashing.

**Why you'd use it:** To turn a letter into a number so I can do math on it (add the shift), then turn it back into a letter.

**Where I used it:** `alphabet.index(message[i])` on line 25 of `Assignment8.py`.

---

## Wrapping around the alphabet

**What it is:** The alphabet list only has positions 0 to 25. If a shift goes past `z` (position 25), I take 26 away to start again from `a`. If it goes below `a` (position 0), I add 26 to come back round from `z`.

```python
alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
            "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

position = alphabet.index("y") + 5   # 29, too big
if position >= 26:
    position = position - 26
print(alphabet[position])

position = alphabet.index("b") - 5   # -4, too small
if position < 0:
    position = position + 26
print(alphabet[position])
```

Output:

```
d
w
```

**Tip:** The `%` (remainder) operator from Day 2 does both in one step, and even works for shifts bigger than 26:

```python
print((24 + 5) % 26)
print((1 - 5) % 26)
print((25 + 30) % 26)
```

Output:

```
3
22
3
```

**Heads up:** The check has to be `>= 26`, not `>= 25`. Position 25 is `z`, which is a real letter. My first version of `TogetherAssignment8.py` had `>= 25` and crashed on a shift of 0.

**Why you'd use it:** So `z` shifted by 1 becomes `a` instead of crashing with an `IndexError`.

**Where I used it:** Lines 28 to 29 and 39 to 40 of `Assignment8.py`, and lines 35 to 36 of `TogetherAssignment8.py`.

---

## Variables inside and outside a function

**What it is:** A variable made **inside** a function (including its parameters) only exists inside that function. Changing it there doesn't change anything outside. A list made **outside** a function can still be added to from inside with `.append()`.

```python
results = []          # made outside the function

def add_letter(letter, shift):
    shift = shift * -1           # only changes the function's own copy
    results.append(letter)       # changes the list outside

my_shift = 5
add_letter("a", my_shift)
add_letter("b", my_shift)

print(my_shift)
print(results)
```

Output:

```
5
['a', 'b']
```

**Heads up:** Because my `encoded_message` list lives outside the functions, calling `encode` twice in one run would keep adding to the same list. My program only calls it once, so that's fine, but it's something to watch out for.

**Why you'd use it:** It's how Python keeps functions from messing up each other's variables by accident.

**Where I used it:** `encoded_message =[]` on line 46 of `Assignment8.py` is outside the functions, and `encoded_message.append(...)` inside them adds to it. `shift_amount = shift_amount * -1` on line 28 of `TogetherAssignment8.py` only changes the function's copy.

---

**Also used today (explained in earlier notes):** lists and `.append()` ([Day 5](../Day05/Notes.md)), `for` + `range(len())`, `in`, `.lower()` and `print(*list)` ([Day 6](../Day06/Notes.md)), `"".join()` ([Day 5](../Day05/Notes.md)), `int(input())` ([Day 4](../Day04/Notes.md)), raw strings for the logo ([Day 3](../Day03/Notes.md)).
