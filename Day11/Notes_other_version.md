# Day 11 Notes: Another Blackjack Version

> **AI generated.** These notes were written by AI (Claude) to explain the Python stuff used in another version of the Day 11 Blackjack project, one I compared mine against. Every example was run to make sure it works.

The other version's code isn't in this repo. The snippets under "Where it's used" are quoted from it. For how it compares with mine, see the end of these notes.

---

## Putting the whole game in a function

This is the biggest difference from my version, so it has its own section in my [Day 11 notes](Notes.md#putting-the-whole-game-in-a-function). In short: everything for one game lives inside `def play_game():`, and the bottom of the file just keeps calling it while the answer is `y`.

**Where it's used:**

```
def play_game():
    ...
while input(f"do you want to play a game of blackjack? ").lower() == "y":
    print("\n"*20)
    play_game()
```

---

## Functions inside a function

**What it is:** You can write a `def` inside another `def`. The inner function only exists while the outer one is running, and only the outer one can use it.

```python
def play_game():
    def deal_card():
        return 10

    hand = [deal_card(), deal_card()]
    print(hand)

play_game()
```

Output:

```
[10, 10]
```

**Heads up:** Calling `deal_card()` outside `play_game()` gives `NameError: name 'deal_card' is not defined`, because it only exists inside.

**Why you'd use it:** It keeps helper functions next to the only code that uses them. Their downside is that you can't test them on their own.

**Where it's used:** `def deal_card():`, `def calculate_score(cards):` and `def compare(user_total, computer_total):` are all inside `def play_game():`.

---

## The same name inside and outside a function

**What it is:** A function's parameters are its own variables. If a parameter has the same name as a variable outside, then inside the function, the name means the **parameter**. The outside one isn't touched.

```python
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def calculate_score(cards):
    return sum(cards)

print(calculate_score([10, 7]))
print(len(cards))
```

Output:

```
17
13
```

Inside `calculate_score`, `cards` is the hand that got passed in (`[10, 7]`). The 13-card deck outside is still fine.

**Heads up:** Loops don't work like this. In an early version of my game, `for cards in range(len(player)):` **replaced** my deck list with a number, because a loop variable is the same variable as the one outside. Only functions get their own separate names.

**Why you'd use it:** You don't have to worry about a function's variable names clashing with the rest of your program.

**Where it's used:** `def calculate_score(cards):`, where `cards` is the hand, while the deck outside is also called `cards`.

---

## Using a special value to mean something (0 = Blackjack)

**What it is:** A score of 0 can never happen in a real game, so the function returns `0` as a signal that means "this is Blackjack". The rest of the code checks for that 0.

```python
def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    return sum(cards)

print(calculate_score([11, 10]))
print(calculate_score([10, 5, 6]))
```

Output:

```
0
21
```

Both hands add up to 21, but only the 2-card one is Blackjack.

**Heads up:** The 0 shows up when the score is printed, so Blackjack shows as "current score is 0".

**Why you'd use it:** One function can give back the score **and** say "Blackjack" without needing a second return value.

**Where it's used:** `if sum(cards) == 21 and len(cards) == 2: return 0`, and then `user_total == 0` and `computer_total == 0` in the game loop and in `compare`.

---

## Swapping an Ace with .remove() and .append()

**What it is:** `.remove(item)` takes the **first** matching item out of a list, and `.append()` adds one to the end. Together, they swap an 11 for a 1.

```python
hand = [11, 10, 5]
hand.remove(11)
hand.append(1)
print(hand)
print(sum(hand))
```

Output:

```
[10, 5, 1]
16
```

**Heads up:** `.remove()` crashes with a `ValueError` if the item isn't in the list, so it's only done after checking `11 in cards`. It also moves the Ace to the end of the hand. My version used `hand[hand.index(11)] = 1` instead, which keeps the Ace where it was.

**Why you'd use it:** It's a quick way to swap one item for another when the order doesn't matter.

**Where it's used:** `if 11 in cards and sum(cards) > 21: cards.remove(11); cards.append(1)` in `calculate_score`.

---

## A function that returns a message

**What it is:** A function can return a string, not just a number. Then you print whatever comes back.

```python
def compare(user_total, computer_total):
    if user_total > 21:
        return "You went over, You lose"
    elif user_total > computer_total:
        return "You Win!!"
    else:
        return "You lose"

print(compare(19, 18))
print(compare(25, 18))
```

Output:

```
You Win!!
You went over, You lose
```

**Why you'd use it:** All the "who won" logic sits in one place, and as soon as one `return` runs, the rest is skipped. No `elif` chain of prints is needed in the main code.

**Where it's used:** `def compare(user_total, computer_total):` and `print(compare(user_total,computer_total))`.

---

## The order of the checks matters

**What it is:** In an `if`/`elif` chain, the **first** check that's true wins, and the rest are skipped. So which check comes first changes the answer.

```python
def compare_draw_first(user_total, computer_total):
    if user_total == computer_total:
        return "Draw"
    elif user_total > 21:
        return "You went over, You lose"
    return "something else"

def compare_bust_first(user_total, computer_total):
    if user_total > 21:
        return "You went over, You lose"
    elif user_total == computer_total:
        return "Draw"
    return "something else"

print(compare_draw_first(22, 22))
print(compare_bust_first(22, 22))
```

Output:

```
Draw
You went over, You lose
```

**Heads up:** The other version checks for a draw first. So when both players bust on the same total, like 22 and 22, it says "Draw", even though going over 21 should lose. I tested this with the real code.

**Why you'd use it:** Put the checks that should **always** win (like going bust) first.

**Where it's used:** `if user_total == computer_total: return "Draw"` is the first check in `compare`.

---

## A flag that controls a loop: while not

**What it is:** A `True`/`False` variable (a flag) can control a `while` loop. `not` flips it, so `while not is_game_over` means "keep going while the game is **not** over". Setting the flag to `True` ends the loop **after** the current pass, while `break` stops straight away.

```python
is_game_over = False
turns = 0
while not is_game_over:
    turns += 1
    print(f"Turn {turns}")
    if turns == 3:
        is_game_over = True
print("Game over")
```

Output:

```
Turn 1
Turn 2
Turn 3
Game over
```

**Why you'd use it:** The loop reads almost like a sentence, and any part of the loop can end the game by setting one variable.

**Where it's used:** `is_game_over = False` and `while not is_game_over:`, with `is_game_over = True` when the player busts, gets Blackjack, or passes.

---

## input() right inside the while

**What it is:** You can ask the question **in** the `while` line itself. It gets asked again each time round. Adding `.lower()` means `Y` and `y` both work.

```python
games = 0
while input("Play? ").lower() == "y":
    games += 1
    print(f"Game {games}")
print("Bye")
```

Output (if I type `Y`, then `y`, then `n`):

```
Play? Y
Game 1
Play? y
Game 2
Play? n
Bye
```

**Why you'd use it:** You don't need a separate variable for the answer, or a separate check to quit.

**Where it's used:** `while input(f"do you want to play a game of blackjack? ").lower() == "y":`

---

## How it compares with my version

I ran both through the same hands:

- **Both get the scoring right.** Aces, two Aces, and the house standing on 17 all work in both. (Mine had 0 errors in 300 random games.)
- **The other version also has:** Blackjack, play again after a bust, `n` at the first question ending the program, and automatic resetting (from being in a function).
- **The other version gets wrong:** both players busting on the same total shows "Draw", and Blackjack shows "current score is 0".

---

**Also used in this version (explained in my earlier notes):** `random.choice()` ([Day 6](../Day06/Notes.md)), `sum()` and `len()` ([Day 11](Notes.md), [Day 5](../Day05/Notes.md)), `while` with `and` ([Day 6](../Day06/Notes.md)), `return` ([Day 10](../Day10/Notes.md)), `"\n" * 20` ([Day 9](../Day09/Notes.md)), f-strings ([Day 1](../Day01/Notes.md)), raw strings for the logo ([Day 3](../Day03/Notes.md)).
