tip_amount1 = 10
tip_amount2 = 12 
tip_amount3 = 15

print("Welcome to the tip calculator!")
Bill_price = input("What was the total bill? \n")
Choosen_tip = input(f"How much or a tip would you want to give? {tip_amount1} {tip_amount2} {tip_amount3}\n")
amount_tip = float(Bill_price) /(100/float(Choosen_tip))
Bill_and_tip = amount_tip + float(Bill_price)
splitting= input("How many people are splitting the bill? \n")
split_price = Bill_and_tip/float(splitting)
print(f"Each person should pay: ${split_price:.2f}")