# Day 25 Notes: Pandas (U.S. States Game)

> **AI generated.** These notes were written by AI (Claude) to explain the Python stuff I used on Day 25. Every example without a turtle window was run to make sure it works (with pandas 3).

Code for this day: [`US_States_Game/main.py`](US_States_Game/main.py), with [`50_states.csv`](US_States_Game/50_states.csv)

---

## Reading a CSV with pandas

**What it is:** `pandas.read_csv()` opens a CSV file and turns it into a **table** (a DataFrame). The first line of the file becomes the column names.

```python
import pandas

data = pandas.read_csv("US_States_Game/50_states.csv")
print(data.head(3))
print(len(data))
```

Output:

```
     state    x    y
0  Alabama  139  -77
1   Alaska -204 -170
2  Arizona -203  -40
50
```

**Why you'd use it:** One line gets all 50 states and their x and y spots on the map. `.head(3)` shows just the first 3 rows. The numbers on the left are the row numbers (the **index**).

**Where I used it:** `state_answer = pandas.read_csv("50_states.csv")` on line 27.

---

## DataFrame vs Series

**What it is:** A **DataFrame** is the whole table. A **Series** is **one column** of it. You get a column with a dot (`data.state`) or with square brackets (`data["state"]`).

```python
import pandas

data = pandas.read_csv("US_States_Game/50_states.csv")
print(type(data))
print(type(data.state))
print(type(data["state"]))
```

Output:

```
<class 'pandas.DataFrame'>
<class 'pandas.Series'>
<class 'pandas.Series'>
```

**Why you'd use it:** It tells you what you're holding. A lot of errors come from having a Series when you wanted a single value. (Older pandas versions print longer names, like `pandas.core.series.Series`.)

**Where I used it:** `state_answer.state` on lines 19, 42 and 47.

---

## Picking a row with a condition

**What it is:** `data[data.state == "Ohio"]` keeps only the rows where the check is `True`. You get back a smaller table.

```python
import pandas

data = pandas.read_csv("US_States_Game/50_states.csv")
row = data[data.state == "Ohio"]
print(row)
```

Output:

```
   state    x   y
34  Ohio  176  52
```

**Why you'd use it:** It finds the one state the player guessed, with its x and y.

**Where I used it:** `state_row = state_answer[state_answer.state == user_guess]` on line 19.

---

## Getting one value with .item()

**What it is:** Even with only one row, `row.y` is still a **Series** (it shows the row number and the value). `.item()` takes the single value out.

```python
import pandas

data = pandas.read_csv("US_States_Game/50_states.csv")
row = data[data.state == "Ohio"]
print(row.y)
print(row.y.item())
```

Output:

```
34    52
Name: y, dtype: int64
52
```

**Why you'd use it:** `goto()` needs plain numbers, not a Series. Don't use `row.y[0]`: `[0]` looks for row **number 0**, and this row is number 34.

**Where I used it:** `x = state_row.x.item()` and `y = state_row.y.item()` on lines 21 and 22.

---

## Looping over a column vs `in`

**What it is:** A `for` loop over a column gives the **values** (the state names). But `in` on a column checks the **row numbers**, not the names. Add `.values` to check the names.

```python
import pandas

data = pandas.read_csv("US_States_Game/50_states.csv")
for name in data.state.head(2):
    print(name)

print("Ohio" in data.state)
print("Ohio" in data.state.values)
```

Output:

```
Alabama
Alaska
False
True
```

**Why you'd use it:** It's an easy mistake: `"Ohio" in data.state` says `False` even though Ohio is there.

**Where I used it:** `for state in state_answer.state:` on line 47.

---

## Removing rows that are in a list: .isin() and ~

**What it is:** `.isin(my_list)` gives `True` for each row whose value **is** in the list. `~` flips every `True` and `False`, so you keep the rows that **aren't** in the list.

```python
import pandas

data = pandas.read_csv("US_States_Game/50_states.csv")
guessed_states = ["Ohio", "Utah", "Vermont"]
missing = data[~data.state.isin(guessed_states)]
print(len(missing))
print("Ohio" in missing.state.values)
```

Output:

```
47
False
```

**Why you'd use it:** When the player types Exit, it gives the states they didn't get.

**Where I used it:** `missing = state_answer[~state_answer.state.isin(guessed_states)]` on line 42.

---

## Saving a table with .to_csv()

**What it is:** `.to_csv(name)` saves a DataFrame as a CSV file. By default it also saves the row numbers as the first column. `index=False` leaves them out.

```python
import os
import pandas

data = pandas.read_csv("US_States_Game/50_states.csv")
small = data.head(2)

small.to_csv("test.csv")
with open("test.csv") as file:
    print(file.read().strip())

small.to_csv("test.csv", index=False)
with open("test.csv") as file:
    print(file.read().strip())

os.remove("test.csv")  # delete the test file
```

Output:

```
,state,x,y
0,Alabama,139,-77
1,Alaska,-204,-170
state,x,y
Alabama,139,-77
Alaska,-204,-170
```

**Why you'd use it:** The missing states get saved so I can study them. Ending the name with `.csv` (like `Missing_States.csv`) lets Excel open it with a double-click.

**Where I used it:** `missing_questions.to_csv("Missing_States")` on line 44. The result is [`Missing_States`](US_States_Game/Missing_States).

---

## Showing the score in the popup title

**What it is:** The title of `textinput` can be an f-string, so it changes every time the box pops up. `len(guessed_states)` is how many states are right so far.

```py
answer_state = screen.textinput(f"{len(guessed_states)}/50 States Correct", "Whats another state's name? ").title()
```

**Why you'd use it:** The player can see their score, like `3/50 States Correct`.

**Where I used it:** Line 38.
