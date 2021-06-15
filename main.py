from binary_adder import binary_adder
print("----------------------------------------------------------------------------")
print("     ╔╦═╦╗─────────────╔╗───╔╗──╔╗───────╔╗╔╗")
print("     ║║║║╠═╦╗╔═╦═╦══╦═╗║╚╦═╗║╚╦╦╣╚╦═╗╔═╗╔╝╠╝╠═╦╦╗")
print("     ║║║║║╩╣╚╣═╣╬║║║║╩╣║╔╣╬║║╬║║║╔╣╩╣║╬╚╣╬║╬║╩╣╔╝")
print("     ╚═╩═╩═╩═╩═╩═╩╩╩╩═╝╚═╩═╝╚═╬╗╠═╩═╝╚══╩═╩═╩═╩╝")
print("     ─────────────────────────╚═╝")
print("         dͩeͤvͮeͤloͦрⷬeͤdͩ вⷡy Jeͤniͥs͛hͪ")
print(" ")
print("-----------------------------------------------------------------------------")
# Welcome screen of the program
user = input("WELCOME!!! Please enter your name to continue:")
print("* The given numbers can not be in alphabets.")
print("* The sum of given numbers can not be more than 255 or 11111111.")
print("* The sum of given numbers can not be less than 0 or 00000000.")
print("* There can not be any space between the numbers.")
print("\n---------------------------------------------------------------------------------------------")
#Guidelines of the program

continue_status = True
while (continue_status == True): #To never end the program untill user wish
    print("\n","****Welcome to the binary addition program****")
    dec1,dec2,i,j,addition = binary_adder() #storing value returned from binary adder module
    first_number = ''
    second_number = ''
    result = ''     #empty string to store 
    for a in i:
        first_number += str(a)
    for b in j:
        second_number += str(b)
    for c in addition:      #storing result to string
        result += str(c)
    if len(addition)>8:  #If sum is more than 255 shows error
        print("⚠️ERROR!!!Please enter the decimal number whose sum is between 00000000 to 11111111")
        
    else:
        print("---------------------------------------------------------------------------------------------")
        print("*********Binary Addition*************               ************Decimal Addition********")
        print("Given first number in binary is  :",first_number,"             Given Number in decimal is :",dec1)
        print("Given second number in binary is :",second_number,"             Given number in decimal is :",dec2)
        print("---------------------------------------------------------------------------------------------")
        print("Sum of the given binary number is:",result,"          Sum of given decimal number is:",dec1+dec2)
        print("---------------------------------------------------------------------------------------------")
        #Displaying the sum of two number 
        ask_user = True
        while ask_user:     #To ask user if wish to quit
            a = input("\nDo you want to exit? (y for yes / n for no) ")
            if a.lower() == 'y':
                print("Good Bye",user,"!!!!","\n---------------------------------------------------------------------------------------------")
                continue_status = False #Stops while loop and the program
                ask_user = False #Stops asking the user for an input to quit
                
            elif a.lower() == 'n':
                print("---------------------------------------------------------------------------------------------\n")
                continue_status = True  #Iniializes true and goes back to first while loop to run the program
                ask_user = False  #Stops asking the user for an input as valid input given
            else:
                print("⚠️ERROR!!!Please enter y to contune and n to exit the programme")
                continue_status = True
                ask_user = True  #Invalid input for y or n asks the user again to enter y or n
            

        
