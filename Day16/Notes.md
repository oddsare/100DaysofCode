# Day 16 Notes: Coffee Machine with Objects

> **AI generated.** These notes were written by AI (Claude) to explain the Python stuff I used on Day 16. Every example was run to make sure it works.

Code for this day: [`Assignment16.py`](Assignment16.py), with [`menu.py`](menu.py), [`coffee_maker.py`](coffee_maker.py) and [`money_machine.py`](money_machine.py)

---

## Importing a class from another file

**What it is:** `from menu import Menu` means: open `menu.py` and bring in the class called `Menu`. Then I can use `Menu` as if it were written in my file.

```python
from menu import Menu
from coffee_maker import CoffeeMaker

print(Menu)
print(CoffeeMaker)
```

Output:

```
<class 'menu.Menu'>
<class 'coffee_maker.CoffeeMaker'>
```

**Why you'd use it:** Each part of the machine lives in its own file, and the main file just puts them together.

**Where I used it:** Lines 1 to 3.

---

## Class vs object

**What it is:** A **class** is the blueprint. An **object** is one thing built from it. You make an object by calling the class with brackets: `Menu()`. Methods are then called on the **object**, not the class.

```python
from menu import Menu

menu = Menu()
print(menu.get_items())
```

Output:

```
latte/espresso/cappuccino/
```

Calling a method on the class instead of the object gives this error:

```py
Menu.find_drink("latte")
# TypeError: Menu.find_drink() missing 1 required positional argument: 'name'
```

**Why you'd use it:** The object (`menu`) is what holds the actual drinks. The class is just the plan for making one.

**Where I used it:** `menu = Menu()`, `coffee_maker = CoffeeMaker()` and `money_machine = MoneyMachine()` on lines 6 to 8.

---

## Attributes (values stored on an object)

**What it is:** An **attribute** is a variable that belongs to an object. You reach it with a dot: `drink.cost`. No brackets, because it's a value, not a method.

```python
from menu import Menu

menu = Menu()
drink = menu.find_drink("latte")
print(drink.name)
print(drink.cost)
print(menu.find_drink("tea"))
```

Output:

```
latte
2.5
Sorry that item is not available.
None
```

**Why you'd use it:** `find_drink` hands back the whole drink, and I pull out just the price with `.cost`.

**Where I used it:** `drink =menu.find_drink(order)` on line 23 and `drink.cost` on line 28.

---

## Methods that answer True or False

**What it is:** A **method** is a function that belongs to an object. You call it with a dot and brackets. Some methods **do** something (like `report()`), and some **answer a question** with `True` or `False`.

```python
from menu import Menu
from coffee_maker import CoffeeMaker

menu = Menu()
coffee_maker = CoffeeMaker()
drink = menu.find_drink("latte")

coffee_maker.report()
print(coffee_maker.is_resource_sufficient(drink))
```

Output:

```
Water: 300ml
Milk: 200ml
Coffee: 100g
True
```

**Why you'd use it:** I can put the answer straight into an `if` to decide whether to take payment and make the drink.

**Where I used it:** `coffee_maker.report()` on line 20, `is_resource_sufficient(drink)` on line 24, and `make_payment(drink.cost)` on line 28.
