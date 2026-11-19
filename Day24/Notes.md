# Day 24 Notes: Files (Snake High Score and Mail Merge)

> **AI generated.** These notes were written by AI (Claude) to explain the Python stuff I used on Day 24. Every example without a turtle window was run to make sure it works.

Code for this day:

- Snake with a high score: [`Assignment24.py`](Assignment24.py), with [`snake.py`](snake.py), [`food.py`](food.py), [`scoreboard.py`](scoreboard.py) and [`data.txt`](data.txt)
- Mail Merge: [`Mail_Merge/main.py`](Mail_Merge/main.py) (see the [Mail Merge README](Mail_Merge/README.md) for the folders)

---

## Reading a file with `with open`

**What it is:** `open()` opens a file. `with` **closes it for you** when the indented block ends. `.read()` gives the whole file as **text**.

```python
with open("data.txt") as file:
    high_score = file.read()

print(high_score)
print(int(high_score) + 1)
```

Output (when `data.txt` has `7` in it):

```
7
8
```

**Why you'd use it:** The high score is saved in a file, so it's still there next time the game starts. It comes back as text, so `int()` turns it into a number.

**Where I used it:** Lines 14 to 17 of [`scoreboard.py`](scoreboard.py).

---

## Writing a file with "w"

**What it is:** `open(name, "w")` opens a file **for writing**. It **wipes the old contents** first (and makes the file if it doesn't exist). `write()` only takes **text**, so numbers need `str()`.

```python
import os

with open("test_score.txt", "w") as file:
    file.write(str(5))

with open("test_score.txt", "w") as file:
    file.write(str(12))

with open("test_score.txt") as file:
    print(file.read())

os.remove("test_score.txt")  # delete the test file
```

Output:

```
12
```

Without `str()`:

```py
file.write(12)
# TypeError: write() argument must be str, not int
```

**Why you'd use it:** The new high score replaces the old one.

**Where I used it:** Lines 38 and 39 of [`scoreboard.py`](scoreboard.py).

---

## Keeping the high score

**What it is:** Before the score goes back to 0, check if it beat the high score.

```python
score = 9
high_score = 7

if score > high_score:
    high_score = score
score = 0
print(score, high_score)
```

Output:

```
0 9
```

**Why you'd use it:** The game keeps going after a crash, and the best score stays on screen.

**Where I used it:** `reset` on lines 35 to 41 of [`scoreboard.py`](scoreboard.py).

---

## Resetting the snake

**What it is:** `.clear()` empties a list. Then the starting squares are made again.

```python
segments = ["head", "body1", "body2", "body3", "body4"]
segments.clear()
print(segments)

for i in range(3):
    segments.append(f"part{i}")
print(segments)
```

Output:

```
[]
['part0', 'part1', 'part2']
```

**Why you'd use it:** Emptying the list doesn't remove the old squares from the screen, so `seg.goto(1000,1000)` moves them out of sight first. Then `self.head` has to point at the new first square.

**Where I used it:** `reset` on lines 61 to 66 of [`snake.py`](snake.py), called on lines 40 and 47 of [`Assignment24.py`](Assignment24.py).

---

## Looping through a file line by line

**What it is:** A `for` loop over an open file gives **one line at a time**. Each line still has its `\n` (new line) on the end.

```python
with open("Mail_Merge/Input/Names/invited_names.txt") as names:
    for line in names:
        print(repr(line))
```

Output:

```
'Aang\n'
'Zuko\n'
'Appa\n'
'Katara\n'
'Sokka\n'
'Momo\n'
'Uncle Iroh\n'
'Toph'
```

(`repr()` shows the hidden `\n`. The last line has none.)

**Why you'd use it:** One letter per name, one name per line.

**Where I used it:** `for i  in f:` on line 19 of [`main.py`](Mail_Merge/main.py).

---

## .strip() and .replace()

**What it is:** `.strip("\n")` removes the new line from the **ends** of the text. `.replace(old, new)` swaps **every** `old` for `new`.

```python
line = "Aang\n"
name = line.strip("\n")
print(name)

letter = "Dear [name],\nYou are invited!"
print(letter.replace("[name]", name))
```

Output:

```
Aang
Dear Aang,
You are invited!
```

**Why you'd use it:** Without `.strip`, the name would carry a new line into the letter and the file name. `.replace` puts each name where `[name]` is.

**Where I used it:** Line 20 and line 27 of [`main.py`](Mail_Merge/main.py).

---

## Paths, r"" and fr""

**What it is:** In normal text, `\` starts a special code, like `\n` for a new line. An **`r` in front** (raw string) makes `\` just a normal character. **`fr`** does that **and** lets you use `{ }` like an f-string.

```python
print("C:\new_folder")
print(r"C:\new_folder")

name = "Aang"
print(fr".\Output\ReadyToSend\letter_for_{name}.txt")
```

Output:

```
C:
ew_folder
C:\new_folder
.\Output\ReadyToSend\letter_for_Aang.txt
```

**Why you'd use it:** Windows paths are full of `\`. `.\` means "start in the folder the program is run from". (On Mac or Linux, use `/` instead of `\`. Windows accepts `/` too.)

**Where I used it:** Lines 17, 23 and 30 of [`main.py`](Mail_Merge/main.py).
