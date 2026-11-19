# Day 17 Notes: Quiz Game (Making My Own Classes)

> **AI generated.** These notes were written by AI (Claude) to explain the Python stuff I used on Day 17. Every example was run to make sure it works.

Code for this day: [`Assignment17.py`](Assignment17.py), with [`question_model.py`](question_model.py), [`quiz_brain.py`](quiz_brain.py) and [`data.py`](data.py)

---

## Writing my own class

**What it is:** `class` makes a blueprint. `__init__` runs **every time a new object is made**. `self` means "this object", so `self.text = text` saves the value **on the object**.

```python
class Question:
    def __init__(self, text, answer):
        self.text = text
        self.answer = answer

q = Question("The sky is blue.", "True")
print(q.text)
print(q.answer)
```

Output:

```
The sky is blue.
True
```

**Why you'd use it:** Each question keeps its own text and answer together in one object.

**Where I used it:** `class Question` in [`question_model.py`](question_model.py), lines 1 to 4.

---

## Building objects from data in a loop

**What it is:** Loop through the raw data, make one object per item, and add it to a list.

```python
from question_model import Question

question_data = [
    {"text": "2 + 2 = 4", "answer": "True"},
    {"text": "Fish can fly.", "answer": "False"},
]
question_bank = []
for item in question_data:
    new_question = Question(item["text"], item["answer"])
    question_bank.append(new_question)

print(len(question_bank))
print(question_bank[1].text)
```

Output:

```
2
Fish can fly.
```

**Why you'd use it:** It turns a big list of dictionaries into a list of `Question` objects. `for item in question_data` and my `for i in range(len(question_data))` with `question_data[i]` do the same thing.

**Where I used it:** Lines 11 to 16 of [`Assignment17.py`](Assignment17.py).

---

## A class that holds a list of objects

**What it is:** One object can hold a whole **list of other objects** as an attribute. Its methods then work on that list, using attributes like `self.question_number` to remember where it is.

```python
from question_model import Question
from quiz_brain import Brain

bank = [Question("2 + 2 = 4", "True"), Question("Fish can fly.", "False")]
quiz = Brain(bank)
print(quiz.question_number, quiz.score)
print(quiz.remaining_questions())

quiz.question_number = 2
print(quiz.remaining_questions())
```

Output:

```
0 0
True
False
```

**Why you'd use it:** The `Brain` keeps track of the questions, which one is next, and the score, so the main file only needs `while quiz.remaining_questions():`.

**Where I used it:** `class Brain` in [`quiz_brain.py`](quiz_brain.py), lines 3 to 6. `quiz = Brain(question_bank)` on line 19 of [`Assignment17.py`](Assignment17.py).

---

## Returning a comparison

**What it is:** A comparison like `a < b` **already is** `True` or `False`, so you can `return` it directly. No `if` needed.

```python
def remaining(question_number, total):
    return question_number < total

print(remaining(3, 10))
print(remaining(10, 10))
```

Output:

```
True
False
```

**Why you'd use it:** It makes `remaining_questions()` one line long, and it works straight inside a `while`.

**Where I used it:** `return self.question_number < len(self.question_list)` on line 9 of [`quiz_brain.py`](quiz_brain.py).

---

## Comparing answers with .lower()

**What it is:** `"true" == "True"` is `False` because capitals matter. Making **both** sides lowercase first fixes that.

```python
print("true" == "True")
print("true".lower() == "True".lower())
```

Output:

```
False
True
```

**Why you'd use it:** The player can type `true`, `True` or `TRUE` and still get it right.

**Where I used it:** `user_answer.lower() == correct_anwser.lower()` on line 21 of [`quiz_brain.py`](quiz_brain.py).
