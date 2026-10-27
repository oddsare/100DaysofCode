alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
            "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

print(r''' ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     'Y8 a8P_____88 I8[    "" ""     'Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  '"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 '"Ybbd8"' '"8bbdP"Y8  '"Ybbd8"' '"YbbdP"' '"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 '"Ybbd8"' 88 88'YbbdP"'  88       88  '"Ybbd8"' 88          
              88                                             
              88           ''')



def encryption (direction,message,shift_amount):
    if direction == "encode":
        shift_amount = shift_amount
        positive_negitive_abc = 26*-1
        
    else:
        shift_amount = shift_amount * -1
        positive_negitive_abc = 26

    for i in range(len(message)):
        if message[i] in alphabet:
            index_of_letter=alphabet.index(message[i])
            index_of_letter = index_of_letter +shift_amount
            if index_of_letter >=  25 or index_of_letter <0 :
                index_of_letter = index_of_letter  + positive_negitive_abc

            encoded_message.append(alphabet[index_of_letter])
    print("".join(encoded_message))


def encode(message,shift_amount):
    
    for i in range(len(message)):
        if message[i] in alphabet:
            index_of_letter=alphabet.index(message[i])
            index_of_letter = index_of_letter +shift_amount
            
            if index_of_letter >= len(alphabet):
                index_of_letter = index_of_letter -26

            encoded_message.append(alphabet[index_of_letter])
    print(*encoded_message)
    
def decode (message,shift_amount):
    for i in range(len(message)):
        if message[i] in alphabet:
            index_of_letter=alphabet.index(message[i])
            index_of_letter = index_of_letter - shift_amount         
            if index_of_letter < 0:
                index_of_letter = index_of_letter +26
            
                
            encoded_message.append(alphabet[index_of_letter])
    print(*encoded_message)

encoded_message =[]
direction =input("Type 'encode' to encrypt, type 'decode' to decrypt: \n").lower()
text = input("Type your message: \n").lower()
shift = int(input("Type the shift number: \n"))

encryption(direction,text,shift)