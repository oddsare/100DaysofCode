import random
print("Welcome to the PyPassword Generator!")
number_of_characters = input("How many letters would you like in your password? \n")
number_symbols = input("How many symbols would you like in your password? \n")
number_of_numbers = input("How many numbers would you like in your password? \n")

password_characters =[]
password_symbols =[]
password_numbers = []

symbols = [
    "!", "@", "#", "$", "%", "^", "&", "*", "(", ")",
    "-", "_", "=", "+",
    "[", "]", "{", "}", "|",
    ";", ":", "'", '"',
    ",", ".", "<", ">", "/", "?",
    "`", "~",
] # 31

numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"] # 10


uppercase = [
    "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
    "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z",
] #26

lowercase = [
    "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
    "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",
] #26 

letters = uppercase +lowercase

while len(password_characters) < int(number_of_characters) :
    letter_choosen=random.randint(0,51)
    password_characters.append(letters[letter_choosen])
    
    
while len(password_symbols) < int(number_symbols) :
    symbols_choosen=random.randint(0,30)
    password_symbols.append(symbols[symbols_choosen])
    
while len(password_numbers) < int(number_of_numbers) :
    numbers_choosen=random.randint(0,9)
    password_numbers.append(numbers[numbers_choosen])
    
    
all_passwords = password_characters +password_symbols +password_numbers

print(all_passwords)
random.shuffle(all_passwords)
print(all_passwords)


print(f"Your password is : {''.join(all_passwords)}")