#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open("./input/Letters/starting_letter.txt", mode='r') as let:
    letter = let.read()
    with open("./input/Names/invited_names.txt", mode='r') as invited_names:
        names = invited_names.readlines()

        for name in names:
            new_name = name.strip()
            new_letter = letter.replace("[name]", new_name)
            
            with open(f"./Output/ReadyToSend/letter_for_{new_name}.docx", mode='w') as readyToSend:
                readyToSend.write(new_letter)

        
    
