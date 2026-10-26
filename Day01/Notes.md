# Day 1 Notes: Band Name Generator

> **AI generated.** These notes were written by AI (Claude) to explain the Python stuff I used on Day 1. Every example was run to make sure it works.

Code for this day: [`Assignment1.py`](Assignment1.py)

---

## print()

**What it is:** `print()` shows stuff on the screen. Whatever you put inside the brackets gets shown when the program runs. If you give it a few things separated by commas, it puts a space between them.

```python
print("Welcome to the Band Name Generator.")
print(42)
print("Hello", "there")
```

Output:

```
Welcome to the Band Name Generator.
42
Hello there
```

**Why you'd use it:** It's the main way the program talks to the person using it. It's also handy for checking what's inside a variable when something isn't working.

**Where I used it:** `Assignment1.py` lines 1, 4 and 6.

---

## Strings

**What it is:** A string is just text. You put it inside quotes so Python knows it's text and not code. Single quotes `'like this'` and double quotes `"like this"` both work. If your text has an apostrophe in it (like `What's`), use double quotes on the outside so the apostrophe doesn't end the string early.

```python
band = "The Rolling Stones"
question = "What's your pet's name?"
print(band)
print(question)
```

Output:

```
The Rolling Stones
What's your pet's name?
```

**Why you'd use it:** Any time you want to store or show words, names, messages, or anything the user types.

**Where I used it:** Every message in `Assignment1.py`.

---

## input()

**What it is:** `input()` asks the user a question, waits for them to type something and press Enter, then hands back what they typed. Whatever they type always comes back as a **string**, even if they type a number (that matters on Day 2).

```python
name = input("What is your name? ")
print("Nice to meet you, " + name)
```

Output (if I type `Sam`):

```
What is your name? Sam
Nice to meet you, Sam
```

**Why you'd use it:** It lets the person using the program give it information, so the program can do something different for each person.

**Where I used it:** `Assignment1.py` lines 2, 3 and 6.

---

## Variables

**What it is:** A variable is a name that holds a value, like a labeled box. You make one with `=`. The name goes on the left, the value goes on the right. Later you can use the name instead of the value, and you can put something new in the box whenever you want.

```python
city = "London"
pet = "Rex"
print(city)
print(pet)

pet = "Biscuit"
print(pet)
```

Output:

```
London
Rex
Biscuit
```

Rules for names: no spaces (use `_` instead), can't start with a number, and capitals matter (`city` and `City` are two different variables).

**Why you'd use it:** So you can save something (like what the user typed) and use it again later without asking twice.

**Where I used it:** `city` and `pet` in `Assignment1.py` lines 2 and 3.

---

## f-strings

**What it is:** An f-string is a string with an `f` in front of the quotes. Inside it, anything in curly brackets `{ }` gets swapped out for its value. It's the easiest way to mix variables into a sentence.

```python
city = "London"
pet = "Rex"
print(f"Your band name could be {city} {pet}")
```

Output:

```
Your band name could be London Rex
```

**Why you'd use it:** It's cleaner than gluing strings together with `+`, and it works with numbers too without having to convert them first.

**Where I used it:** `Assignment1.py` line 4.

---

## Joining strings with + (concatenation)

**What it is:** You can stick strings together with `+`. Python doesn't add spaces for you, so you have to put them in yourself.

```python
first = "Hello"
second = "World"
print(first + second)
print(first + " " + second + "!")
```

Output:

```
HelloWorld
Hello World!
```

You can even put `input()` straight inside, like I did on line 6. Python runs the `input()` first, then glues the answer in:

```python
print("hello " + input("What is your name? ") + "!")
```

Output (if I type `Sam`):

```
What is your name? Sam
hello Sam!
```

**Heads up:** `+` only joins strings to strings. `"Age: " + 25` crashes. You'd need `"Age: " + str(25)` or an f-string instead.

**Why you'd use it:** Quick way to build a message out of a few pieces.

**Where I used it:** `Assignment1.py` line 6.

---

## \n (new line)

**What it is:** `\n` inside a string means "go to the next line". The backslash tells Python the next letter is special and not just a normal `n`.

```python
print("Line one\nLine two")
```

Output:

```
Line one
Line two
```

**Why you'd use it:** I put `\n` at the end of my `input()` questions so the user types their answer on the line underneath instead of right next to the question.

**Where I used it:** `Assignment1.py` lines 2, 3 and 6.
