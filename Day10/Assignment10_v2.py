#docstrings
import os 
art =(r''' _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ '.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ '.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   '._____.'  | || ||____|  |____|| || |  |________|  | || |   '._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|''')

print(art)

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def add (n1,n2):
    return n1 +n2

def divide (n1,n2):
    return n1/n2

def mult(n1,n2):
    return n1*n2

def sub (n1,n2):
    return n1-n2

total = 0
operation = {
    "+": add,
    "-":sub,
    "*":mult,
    "/": divide,
}
starting = "starting"
while True:
    if starting == "starting" or starting == "n":
        print(art)
        number = float(input("What's the first number?: ") )# this is never repeated  out of loop 
        starting = ""
    elif starting =="y":
        number = total
    print("+\n-\n*\n/\n")
    operator = input("Pick an operation")
    next_number =float(input("What's the next number?: "))
    
    total = operation[operator](number,next_number)
    print(f"{number} {operator} {next_number} = {total}")
    
    starting = input(f"Type 'y' to continue calculating with {total}, or type 'n' to start a new calculation:")
    if starting == "n":
        clear()
