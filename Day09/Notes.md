# Day 9 Notes: Dictionaries and the Secret Auction

> **AI generated.** These notes were written by AI (Claude) to explain the Python stuff I used on Day 9. Every example was run to make sure it works.

Code for this day: [`Assignment9.py`](Assignment9.py) (the secret auction) and [`learn_dictionary.py`](learn_dictionary.py) (my practice file)

---

## Dictionaries

**What it is:** A dictionary stores things in **key: value** pairs, inside curly brackets `{ }`. A list finds things by **position** (`my_list[0]`), but a dictionary finds things by **name** (the key). `{}` on its own is an empty dictionary.

```python
bids = {"sam": 100, "alex": 150}
empty = {}

print(bids)
print(empty)
print(len(bids))
```

Output:

```
{'sam': 100, 'alex': 150}
{}
2
```

**Heads up:** Keys have to be unique, but values don't. Two people can bid 100, but there can only be one `"sam"`.

**Why you'd use it:** Whenever things have labels: a name and a bid, a country and its capital, a word and its meaning. They're one of the things coders use most, for example all data from websites (JSON) comes in as dictionaries.

**Where I used it:** `Blind_auction = {}` on line 17 of `Assignment9.py`, and `variable_name` on lines 2 and 3 of `learn_dictionary.py`.

---

## Getting a value with its key

**What it is:** Put the key in square brackets to get its value back.

```python
capitals = {"France": "Paris", "Japan": "Tokyo"}
print(capitals["Japan"])

key = "France"
print(capitals[key])
```

Output:

```
Tokyo
Paris
```

**Heads up:** Asking for a key that isn't there crashes with a `KeyError`. Also, a dictionary has no positions, so `capitals[0]` doesn't work (that's a `KeyError` too).

**Why you'd use it:** It's the main reason dictionaries exist: jump straight to the thing you want by its name.

**Where I used it:** `print(variable_name["Variable_key"])` on line 5 of `learn_dictionary.py`, and `Blind_auction[winners]` on line 39 of `Assignment9.py`.

---

## Adding or changing an entry

**What it is:** `dictionary[key] = value` adds a new entry. If the key is **already there**, it replaces the old value instead.

```python
bids = {"sam": 100}

bids["alex"] = 150      # new key, so it's added
print(bids)

bids["sam"] = 50        # sam already exists, so 100 gets replaced
print(bids)
```

Output:

```
{'sam': 100, 'alex': 150}
{'sam': 50, 'alex': 150}
```

**Heads up:** This is why my auction gave the wrong winner when the same name bid twice. The second bid quietly replaced the first one.

**Why you'd use it:** To build up a dictionary as you go, like adding each bidder after they type their bid.

**Where I used it:** `Blind_auction[name] = bid` on line 28 of `Assignment9.py`, and `variable_name["variable3"]= "value 3"` on line 8 of `learn_dictionary.py`.

---

## Checking if a key exists with in

**What it is:** `in` works on dictionaries too. It checks the **keys** (not the values).

```python
bids = {"sam": 100, "alex": 150}
print("sam" in bids)
print("kim" in bids)
print(100 in bids)      # False, because 100 is a value, not a key
```

Output:

```
True
False
False
```

**Why you'd use it:** To check before adding something, so you don't replace an entry by accident.

**Where I used it:** `while name in Blind_auction:` on line 24 of `Assignment9.py`.

---

## A while loop that keeps asking until the answer is OK

**What it is:** Put the question once, then use a `while` loop to keep asking again for as long as the answer is no good. When the answer is OK, the loop's check is false and the program moves on.

```python
taken = {"sam": 100}
answers = ["sam", "sam", "jo"]      # pretend these were typed in, one at a time
turn = 0

name = answers[turn]
while name in taken:
    print(f"{name} is taken, pick another")
    turn += 1
    name = answers[turn]

print(f"Welcome, {name}")
```

Output:

```
sam is taken, pick another
sam is taken, pick another
Welcome, jo
```

In my real code, `input()` goes where `answers[turn]` is.

**Why you'd use it:** To stop bad answers before they cause problems later, like duplicate names.

**Where I used it:** Lines 23 to 25 of `Assignment9.py`.

---

## Looping through a dictionary

**What it is:** `for key in my_dict:` goes through the **keys** one at a time. Use the key to get the value. If you want both at once, use `.items()`.

```python
bids = {"sam": 100, "alex": 150}

for key in bids:
    print(key, bids[key])

for name, bid in bids.items():
    print(f"{name} bid {bid}")
```

Output:

```
sam 100
alex 150
sam bid 100
alex bid 150
```

**Tip:** You can use this to find a key when you only know its value:

```python
capitals = {"France": "Paris", "Japan": "Tokyo"}
for country, city in capitals.items():
    if city == "Tokyo":
        print(country)
```

Output:

```
Japan
```

**Why you'd use it:** To check every entry, like going through every bid to find the highest one. (`for i in range(len())` doesn't work here, because dictionaries don't have positions.)

**Where I used it:** `for key in Blind_auction:` on line 30 of `Assignment9.py`.

---

## Finding the highest value

**What it is:** Keep a "best so far" variable. Go through everything, and whenever something beats it, update it (and remember who it belonged to).

```python
bids = {"sam": 100, "alex": 150, "kim": 120}
highest_bid = -1
winner = ""

for name in bids:
    if bids[name] > highest_bid:
        highest_bid = bids[name]
        winner = name

print(f"The winner is {winner} with ${highest_bid}")
```

Output:

```
The winner is alex with $150
```

**Heads up:** The starting value matters. If `highest_bid` started at `0`, a bid of `0` would never beat it and `winner` would never get set. Starting at `-1` means any bid of 0 or more counts. Also, because the check is `>` (not `>=`), the first person wins a tie.

**Why you'd use it:** Highest score, cheapest price, longest word: it's the same pattern every time.

**Where I used it:** Lines 19, 21 and 30 to 33 of `Assignment9.py`.

---

## continue

**What it is:** `continue` skips the rest of the code in the loop and jumps straight back to the top for the next go.

```python
for number in [1, 2, 3, 4]:
    if number == 2:
        continue
    print(number)
```

Output:

```
1
3
4
```

**Why you'd use it:** To skip the rest of a loop when there's nothing more to do this time round.

**Where I used it:** Line 37 of `Assignment9.py`, after clearing the screen for the next bidder.

---

## Clearing the screen with "\n" * 100

**What it is:** Multiplying a string repeats it (like `['_'] * 5` from Day 7). `"\n" * 100` is 100 new lines, which pushes the old text off the top of the screen.

```python
print("ab" * 3)
print(len("\n" * 100))
```

Output:

```
ababab
100
```

**Why you'd use it:** So the next bidder can't see what the last person bid. It's not a real "clear", you could scroll up, but it's simple and works everywhere.

**Where I used it:** `print("\n"*100)` on line 36 of `Assignment9.py`.

---

## Lists inside dictionaries

**What it is:** A value in a dictionary can be anything, including a whole list. Use two sets of square brackets: the first gets the list by its key, the second gets an item out of that list by its position.

```python
travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Stuttgart", "Berlin"]
}

print(travel_log["France"])
print(travel_log["France"][1])
```

Output:

```
['Paris', 'Lille', 'Dijon']
Lille
```

**Why you'd use it:** When one thing has several values, like a country with lots of cities.

**Where I used it:** Lines 13 to 18 of `learn_dictionary.py`.

---

## Lists inside lists

**What it is:** A list can hold another list as one of its items. Again, use two sets of square brackets: first the outer position, then the inner one.

```python
nested_list = ["A", "B", ["C", "D"]]
print(nested_list[2])
print(nested_list[2][1])
```

Output:

```
['C', 'D']
D
```

`["C", "D"]` counts as **one** item (position 2) in the outer list.

**Why you'd use it:** For grids, like a game board or a spreadsheet (a list of rows, where each row is a list).

**Where I used it:** Lines 21 and 22 of `learn_dictionary.py`.

---

## Dictionaries inside dictionaries

**What it is:** A dictionary's value can also be another dictionary. Then the second set of brackets needs a **key**, not a number.

```python
travel_log = {
    "France": {"cities_visited": ["Paris", "Lille", "Dijon"], "total_visits": 12},
    "Germany": {"cities_visited": ["Berlin", "Hamburg", "Stuttgart"], "total_visits": 5}
}

print(travel_log["Germany"]["total_visits"])
print(travel_log["Germany"]["cities_visited"])
print(travel_log["Germany"]["cities_visited"][2])
```

Output:

```
5
['Berlin', 'Hamburg', 'Stuttgart']
Stuttgart
```

**Heads up:** Line 25 of my `learn_dictionary.py` does `travel_log["Germany"]["cities_visited"][2]`, but my `travel_log` has a **list** for Germany, not a dictionary. So `["cities_visited"]` tries to use a word as a list position, and it crashes with `TypeError: list indices must be integers or slices, not str`. That line needs the dictionary version of `travel_log` above. (Even then, `[2]` needs at least 3 cities in the list.)

**Why you'd use it:** For more detailed data, like each country having a list of cities **and** a number of visits. Data from websites is often built like this.

**Where I used it:** Line 25 of `learn_dictionary.py`.

---

**Also used today (explained in earlier notes):** `while` loops ([Day 5](../Day05/Notes.md)), `int(input())` ([Day 4](../Day04/Notes.md)), `.lower()` ([Day 6](../Day06/Notes.md)), f-strings ([Day 1](../Day01/Notes.md)), raw strings for the gavel logo ([Day 3](../Day03/Notes.md)).
