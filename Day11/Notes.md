# Day 11 Notes: Blackjack

> **AI generated.** These notes were written by AI (Claude) to explain the Python stuff I used on Day 11. Every example was run to make sure it works.

Code for this day: [`Assignment11.py`](Assignment11.py)

---

## sum() (adding up a list)

**What it is:** `sum()` adds up every number in a list and gives back the total.

```python
hand = [10, 7, 2]
print(sum(hand))
print(sum([]))
```

Output:

```
19
0
```

**Why you'd use it:** It's quicker than writing a loop to add things up, like a hand of cards or a list of prices.

**Where I used it:** `player_total = sum(player)` and `house_total =sum(house)` on lines 41 and 43, and again on lines 125 and 127.

---

## Passing a list into a function (and changing it)

**What it is:** When you pass a **list** into a function and the function changes it (like with `.append()`), the change sticks to the original list outside the function. That's different from a number: changing a number inside a function only changes the function's own copy (Day 8).

```python
def give_card(hand, card):
    hand.append(card)

player = [10]
give_card(player, 7)
give_card(player, 2)
print(player)


def add_ten(number):
    number = number + 10

score = 5
add_ten(score)
print(score)
```

Output:

```
[10, 7, 2]
5
```

**Why you'd use it:** One function can deal cards to **any** hand. I pass in `player` or `house`, and that hand gets the cards, with no `return` needed.

**Where I used it:** `def draw_cards(user_cards,number)` on lines 21 to 25, used for the player and the house on lines 35, 36, 64, 91, 119 and 120.

---

## Counting things in a list

**What it is:** Loop through the list, add 1 to a counter for each match, and `return` the count at the end. Lists also have `.count()`, which does the same thing in one step.

```python
def count_aces(hand):
    aces = 0
    for card in hand:
        if card == 11:
            aces += 1
    return aces

print(count_aces([11, 5, 11]))
print([11, 5, 11].count(11))
```

Output:

```
2
2
```

**Heads up:** My `check_for_ll` starts counting from the number I pass in, not from 0. So when I pass in the old count, every Ace gets counted again and the number keeps growing. My game still works, because I only use that number as "how many times to try", and the `11 in player` check stops it from doing anything extra.

**Why you'd use it:** To know how many of something you have, like how many Aces could still drop to 1.

**Where I used it:** `def check_for_ll` on lines 28 to 32, used on lines 38, 39, 68 and 93.

---

## Finding an item and replacing it

**What it is:** `.index()` finds the position of an item (Day 8), and `list[position] = new_value` replaces it (Day 6). Put them together and you can find something and change it in one line.

```python
hand = [11, 10, 11]
position = hand.index(11)
print(position)

hand[position] = 1
print(hand)

hand[hand.index(11)] = 1
print(hand)
```

Output:

```
0
[1, 10, 11]
[1, 10, 1]
```

**Heads up:** `.index()` crashes with a `ValueError` if the item isn't in the list at all. That's why I always check `11 in player` first.

**Why you'd use it:** To change a specific item when you know what it is but not where it is.

**Where I used it:** `player[player.index(11)] = 1` on line 54, and the same for the house on lines 85 and 97.

---

## The Ace rule

**What it is:** An Ace is worth 11, unless that would put the hand over 21; then it's worth 1. When an Ace drops, I take 10 off the total **and** change that 11 into a 1 in the list, so the same Ace can never drop twice.

```python
def ace_check(hand):
    total = sum(hand)
    for i in range(hand.count(11)):
        if total > 21 and 11 in hand:
            hand[hand.index(11)] = 1
            total -= 10
    return total

print(ace_check([11, 5, 10]))
print(ace_check([11, 11, 10]))
print(ace_check([11, 10, 10, 5]))
print(ace_check([11, 9]))
```

Output:

```
16
12
26
20
```

- `[11, 5, 10]` is 26, so the Ace drops: **16**.
- `[11, 11, 10]` is 32, so one Ace drops (22), then the other (12).
- `[11, 10, 10, 5]` is 36, so the Ace drops to 26. There are no Aces left, so it's a real bust.
- `[11, 9]` is 20, so nothing needs to drop.

**Heads up:** Taking 10 off without changing the 11 to a 1 lets the same Ace drop again later. That was my "same Ace dropping twice" bug.

**Why you'd use it:** It's how Blackjack scoring actually works.

**Where I used it:** Lines 52 to 55 for the player, and lines 83 to 86 and 95 to 98 for the house.

---

## Using a counter to find the newest card

**What it is:** Every time a card is drawn, add 1 to a counter. Then the counter tells you the position of the newest card. `list[-1]` does the same thing without a counter, because `-1` is always the last item (Day 5).

```python
hand = [10, 2]
number_of_cards = 0

hand.append(5)
number_of_cards += 1
newest = 1 + number_of_cards

print(hand[newest])
print(hand[-1])
```

Output:

```
5
5
```

**Heads up:** My house code first had `house_number_of_cards += 0`. Adding 0 never changes anything, so it kept adding the house's **second** card every time instead of the new one. A house that really had 38 showed 20 and "won". It's now `+= 1`.

**Why you'd use it:** To add just the new card to the total, instead of adding up the whole hand again.

**Where I used it:** Lines 62, 63 and 67 for the player, and lines 89, 90 and 92 for the house.

---

## Making if / elif cover every number

**What it is:** When an `if` and an `elif` split numbers into groups, check that every number lands somewhere. `< 17` and `>= 17` cover everything. But `< 17` and `> 17` both skip **exactly 17**:

```python
for total in [16, 17, 18]:
    if total < 17:
        print(total, "draw")
    elif total >= 17:
        print(total, "stand")

print("---")

for total in [16, 17, 18]:
    if total < 17:
        print(total, "draw")
    elif total > 17:
        print(total, "stand")
```

Output:

```
16 draw
17 stand
18 stand
---
16 draw
18 stand
```

In the second loop, 17 matches nothing, so nothing happens. In my house's `while True` loop, that meant nothing happened **forever**, and the game froze (about 1 game in 7).

**Why you'd use it:** The house has to stand on 17 or more and draw on 16 or less, with no gaps.

**Where I used it:** `if house_total < 17:` on line 88, and `>= 17` on lines 94 and 99.

---

## break only leaves one loop

**What it is:** `break` only leaves the loop it's **directly inside**. If loops are inside loops, the outer ones keep going.

```python
while True:
    print("game loop")
    while True:
        print("  house loop")
        break
    print("back in the game loop")
    break
```

Output:

```
game loop
  house loop
back in the game loop
```

**Why you'd use it:** To end just one part of the program, like the house's turn, while the game carries on.

**Where I used it:** `break` on line 100 ends the house's turn and goes on to who won. `break` on line 74 leaves the main game loop when the player busts, which ends the program.

---

## exit()

**What it is:** `exit()` stops the whole program straight away, wherever you are, even inside loops.

```python
print("before")
exit()
print("never printed")
```

Output:

```
before
```

**Why you'd use it:** When the user says they don't want to play anymore.

**Where I used it:** Line 133, when the answer to "play again?" isn't `y`.

---

## Resetting everything for a new game

**What it is:** Variables keep their values until you change them. For a fresh game, put every hand, total and counter back to how it was at the start.

```python
player = [10, 9, 8]
player_total = 27
number_of_cards = 1

player = []
player_total = 0
number_of_cards = 0
print(player, player_total, number_of_cards)
```

Output:

```
[] 0 0
```

**Heads up:** Forgetting even one causes weird bugs. For example, if `number_of_cards` wasn't reset, the counter would point at the wrong card in the new game.

**Why you'd use it:** So one game's cards and scores don't leak into the next.

**Where I used it:** Lines 117 to 130.

---

## Putting the whole game in a function

**What it is:** Put everything for one game inside a function, like `def play_game():`, and call it from a loop that asks "play again?". Each call runs one whole game from the start.

```python
def play_game():
    hand = []          # a fresh, empty hand every game
    hand.append(10)
    hand.append(7)
    print(f"Your hand: {hand}, score: {sum(hand)}")

while input("Do you want to play? Type 'y' or 'n': ") == "y":
    play_game()

print("Thanks for playing")
```

Output (if I type `y`, then `y`, then `n`):

```
Do you want to play? Type 'y' or 'n': y
Your hand: [10, 7], score: 17
Do you want to play? Type 'y' or 'n': y
Your hand: [10, 7], score: 17
Do you want to play? Type 'y' or 'n': n
Thanks for playing
```

**Why you'd use it:**

- **No reset code.** Variables made inside a function start fresh every time it's called, so each game automatically gets empty hands and new totals. My version needs lines 117 to 130 to reset everything by hand.
- **Ending a game is easy.** A `return` (or just reaching the end of the function) finishes the game from anywhere, even inside loops, and drops you back at the "play again?" question. That works after a bust too, which my version doesn't do.
- **It's easier to read.** The bottom of the file is just "keep playing while the answer is y".

**Where I used it:** Not in my version. This is how another version of the Blackjack project that I compared mine against works: it has `def play_game():` with smaller functions for dealing, scoring and comparing inside it, and `while input(...) == "y": play_game()` at the bottom.

---

**Also used today (explained in earlier notes):** `random.choice()`, `for` + `range()`, `in` / `not in`, `+=` and `-=` ([Day 6](../Day06/Notes.md)), `while True` ([Day 10](../Day10/Notes.md)), functions with `return` ([Day 10](../Day10/Notes.md)), `if` / `elif` and `and` ([Day 3](../Day03/Notes.md)), f-strings ([Day 1](../Day01/Notes.md)), raw strings for the logo ([Day 3](../Day03/Notes.md)).
