logo = r'''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\
                       .-------------.
                      /_______________\
'''
print(logo)

print("Welcome to the secret auction program")
Blind_auction = {}

highets_bid = -1
other_bidders = "yes"
winners = ""
while  other_bidders == "yes":
    name = input("What is your name? ")
    while name in Blind_auction:
        name = input("That name has already been chosen. Pick another: ")
    bid = int(input("How Much would you like to bid? "))
    other_bidders = input("Are there any other bidders? Type 'yes or 'no'.").lower()
    Blind_auction[name] = bid

    for key in Blind_auction:
        if Blind_auction[key] > highets_bid:
            highets_bid = Blind_auction[key]
            winners = key

    if other_bidders == "yes":
        print("\n"*100)
        continue
    elif other_bidders == "no":
        print(f"This is the winner {winners} and their bid is {Blind_auction[winners]}")


        
        
        
    
