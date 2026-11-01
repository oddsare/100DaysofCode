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

def get_number(question):
    while True:
        try:
            return float(input(question))
        except ValueError:
            print("That's not a number, try again.")

total = 0
Current_function =add



#number = input("What's the first number?: ") # this is never repeated  out of loop 
starting = "starting"
while True:
    if starting == "starting" or starting == "n":
        print(art)
        number = get_number("What's the first number?: ")# this is never repeated  out of loop
        starting = ""
    elif starting =="y":
        number = total

    print("+\n-\n*\n/\n") #this is repeated 


    operator = input("Pick an operation") # This is repeated 
    if operator == "*":
        Current_function = mult
    elif operator == "-":
        Current_function = sub
    elif operator == "/":
        Current_function = divide
    elif operator == "+":
        Current_function = add
        

    next_number = get_number("What's the next number?: ") #this is repeated
    while Current_function == divide and next_number == 0:
        print("You can't divide by 0, try again.")
        next_number = get_number("What's the next number?: ")
    
    total = Current_function(number,next_number)
    print(total)
    
    starting = input(f"Type 'y' to continue calculating with {total}, or type 'n' to start a new calculation:")
    if starting == "n":
        clear()

#next thing I need to do is if they input something that is not what they should 
total = float(number) + operator + float(next_number)
print(total)