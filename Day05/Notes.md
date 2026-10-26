# Day 5 Notes: Password Generator

> **AI generated.** These notes were written by AI (Claude) to explain the Python stuff I used on Day 5. Every example was run to make sure it works.

Code for this day: [`Assignment5.py`](Assignment5.py)

---

## Lists

**What it is:** A list holds a bunch of values in one variable, in order. You make one with square brackets `[ ]` and put commas between the items. `[]` on its own is an empty list, ready to be filled up.

```python
numbers = ["0", "1", "2", "3"]
fruits = ["apple", "banana", "cherry"]
password = []

print(numbers)
print(fruits)
print(password)
```

Output:

```
['0', '1', '2', '3']
['apple', 'banana', 'cherry']
[]
```

**Why you'd use it:** When you have lots of related things (all the symbols, all the letters, all the words for hangman). Way better than making 26 separate variables.

**Where I used it:** `symbols`, `numbers`, `uppercase` and `lowercase` on lines 11 to 31, and the empty lists on lines 7 to 9.

---

## Indexing: getting one item out of a list

**What it is:** Each item in a list has a position number called an **index**. Counting starts at **0**, not 1! So the first item is `[0]`. Negative numbers count from the end, so `[-1]` is the last item.

```python
letters = ["a", "b", "c", "d", "e"]
print(letters[0])
print(letters[2])
print(letters[-1])
```

Output:

```
a
c
e
```

**Heads up:** Asking for an index that doesn't exist (like `letters[5]` above) crashes with an `IndexError`. That's why my code uses `randint(0, 51)` for 52 letters, not `randint(0, 52)`.

**Why you'd use it:** To grab a specific item, or a random one by picking a random index.

**Where I used it:** `letters[letter_choosen]` on line 37.

---

## len()

**What it is:** `len()` tells you how many items are in a list, or how many characters are in a string.

```python
letters = ["a", "b", "c"]
print(len(letters))
print(len("hangman"))
print(len([]))
```

Output:

```
3
7
0
```

**Why you'd use it:** To know how big something is, for example to keep looping until the password has enough letters.

**Where I used it:** `len(password_characters)` on line 35.

---

## .append()

**What it is:** `.append()` adds one item to the **end** of a list.

```python
password = []
password.append("a")
password.append("7")
password.append("!")
print(password)
```

Output:

```
['a', '7', '!']
```

**Why you'd use it:** To build up a list one piece at a time, like adding a random character each time round a loop.

**Where I used it:** `password_characters.append(...)` on line 37, and the same for symbols and numbers on lines 42 and 46.

---

## Adding lists together with +

**What it is:** `+` on two lists makes one new list with everything from the first, then everything from the second.

```python
uppercase = ["A", "B", "C"]
lowercase = ["a", "b", "c"]
letters = uppercase + lowercase
print(letters)
print(len(letters))
```

Output:

```
['A', 'B', 'C', 'a', 'b', 'c']
6
```

**Why you'd use it:** To combine lists so you can pick from all of them at once.

**Where I used it:** `letters = uppercase + lowercase` on line 33, and putting the password pieces together on line 49.

---

## while loops

**What it is:** A `while` loop keeps running the indented code over and over **as long as** its check is true. Once the check is false, it stops and the program carries on.

```python
count = 0
while count < 3:
    print(f"Loop number {count}")
    count = count + 1
print("Done")
```

Output:

```
Loop number 0
Loop number 1
Loop number 2
Done
```

**Heads up:** Make sure something inside the loop eventually makes the check false. If not, it loops forever (press `Ctrl + C` to stop it).

**Why you'd use it:** When you don't know exactly how many times something should repeat, just *when* it should stop. Like "keep adding letters until there are enough" or "keep the game going until you run out of lives".

**Where I used it:** Lines 35, 40 and 44, which keep adding characters until each list is long enough.

---

## random.shuffle()

**What it is:** `random.shuffle()` mixes up the order of a list randomly. It changes the list itself and doesn't give anything back, so you don't write `x = random.shuffle(x)`.

```python
import random

cards = ["A", "K", "Q", "J"]
random.shuffle(cards)
print(cards)
```

Output (it's random, so yours will be different):

```
['Q', 'A', 'J', 'K']
```

**Why you'd use it:** Shuffling cards, or mixing up a password so it isn't all letters first, then symbols, then numbers.

**Where I used it:** `random.shuffle(all_passwords)` on line 52.

---

## "".join()

**What it is:** `.join()` glues all the items in a list into one string. The string before `.join` is what goes **between** each item. An empty string `""` means nothing goes between them.

```python
pieces = ["p", "a", "s", "s"]
print("".join(pieces))
print("-".join(pieces))
print(" ".join(["Hello", "there"]))
```

Output:

```
pass
p-a-s-s
Hello there
```

**Why you'd use it:** To turn a list of characters back into a normal word or password.

**Where I used it:** `''.join(all_passwords)` on line 56. I used it again on Day 6 to show the hangman word at the end.

---

**Also used today (explained in earlier notes):** `import random` and `random.randint()` ([Day 4](../Day04/Notes.md)), `int()` to convert the answers ([Day 2](../Day02/Notes.md)).
