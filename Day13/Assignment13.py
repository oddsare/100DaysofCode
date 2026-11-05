#debugging 
def odd_or_even(number):
    if number % 2 = 0: 
        return "This is an even number."
    else:
        return "This is an odd number."
    
def odd_or_even(number):
    if number % 2 == 0: ## this is the fix to check something you need to == sign, = is assignment which does not work here 
        return "This is an even number."
    else:
        return "This is an odd number."
    
    ####################################################
def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 4000 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
    
    
def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0: # this is the fix the number should be 400 to find the leep year not 4k
                return True
            else:
                return False
        else:
            return True
    else:
        return False
    
    
    ###################################
# Target is the number up to which we count
def fizz_buzz(target):
    for number in range(1, target + 1):
        if number % 3 == 0 or number % 5 == 0:
            print("FizzBuzz")
        if number % 3 == 0:
            print("Fizz")
        if number % 5 == 0:
            print("Buzz")
        else:
            print([number])

      
    
# Target is the number up to which we count
def fizz_buzz(target):
    for number in range(1, target + 1):
        if number % 3 == 0 and number % 5 == 0: # we need and to have both conditions met 
            print("FizzBuzz")
        elif number % 3 == 0: # these need to be elif statements to not over write each other or print something that should not be printed
            print("Fizz")
        elif number % 5 == 0:# these need to be elif statements to not over write each other or print something that should not be printed
            print("Buzz")
        else:
            print(number) # # [number] number just gives us the number we do not need to put it into a [] this does not work
