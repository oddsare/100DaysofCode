#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp




PLACEHOLDER = "[name]"
 
 
       
f = open(r".\Input\Names\invited_names.txt")

for i  in f:
    name = i.strip("\n")
    
  
    with open(r".\Input\Letters\starting_letter.txt", "r") as letter_file:
        letter_contex =letter_file.read()
        
        
    new_letter = letter_contex.replace(PLACEHOLDER,name)


    with open(fr".\Output\ReadyToSend\letter_for_{name}.txt","w") as completed_letter:
        completed_letter.write(new_letter)