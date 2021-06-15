def number_input():
    status = 'available'
    while status == 'available': #while loop to continue if wrong input given
        addition_type = input("\nEnter b for binary addition and d for decimal addition")
        if addition_type.lower() == 'b': #chck if the input for choice is b
            print("\n**Binay addition has been choosed.**")
            status = 'not available' #stops asking the user to enter addition choice
            while True: 
                try: 
                    a1 = (input("Enter first binary number:"))
                    a = int(a1)
                    al = list(a1)
                    a2 = ''
                    for i in al:
                            if i== '1' or i == '0':
                                a2 += i 
                    if a2 != a1: #comparing if the integer value are in form or 1 and 0
                        print("\n⚠️ERROR!!! Please enter number as 10011111. \nNumber can't be negative or in alphabet.\nThere can not be any space between the numbers.\n")
                        continue
                    if (len(a1)>8 or len(a1)<0): #To show error message if the input is more than 255
                        print ("⚠️ERROR!!! Please enter binary number between 00000000 and 11111111")
                        continue
                        #goes back to while loop and ask user to enter first number again
                    else:
                        a1 = int(a1) #Initialize the value as int in variable a1
                    while True:
                        try:
                            b1 = input("Enter second binary number:")
                            b = int(b1)
                            bl = list(b1)
                            b2 = ''
                            for i in b1:
                                    if i== '1' or i == '0':
                                        b2 += i
                            if b2 != b1:  #comparing if the integer value are in form or 1 and 0
                                print("\n⚠️ERROR!!! Please enter number as 10011111. \nNumber can't be negative or in alphabet\nThere can not be any space between the numbers.\n")
                                continue
                            if (len(b1)>8 or len(b1)<0): #To show error message if the input is more than 255
                                print ("⚠️ERROR!!! Please enter binary number between 00000000 and 11111111")
                                continue
                                #goes back to while loop and ask user to enter second number again
                            else:
                                b1 = int(b1) #Initialize the value as int in variable b1
                        except:
                            print("\n⚠️ERROR!!! Please enter binary number as","10101000 \nBinary number cant be negative and can not be in alphabets.")
                            print("There can not be any space between the numbers.\n")
                            continue
                            #Exception if string data type is passed 
                        else:
                            break
                            #breaks the while loop if all the inputs are valid
                    
                    return a1,b1,addition_type
                except:
                    print("\n⚠️ERROR!!!Please enter binary number as","10101000 \nBinary number cant be negative and can not be in alphabets.")
                    print("There can not be any space between the numbers.\n")
                    continue
                    #Exception if string data type is passed
                else:
                    break
                    #breaks the while loop of all the inputs are valid
                
        elif addition_type.lower() == 'd': #To check if the input for choice is d
            print("\n**Decimal addition has been choosed.**")
            while True: #while loop continues if wrong input is given
                try:
                    a1 = int(input("Enter first decimal number:"))
                    if (a1>255) or (a1<0): #comparing if the first number is more than 255 or less than 0
                        print("\n⚠️ERROR!!!Please enter number between 0 to 255\n")
                        continue
                        #shows an error message and goes back to while loop and asks for input again
                    while True: #while loop continues if wrong input is given
                        try:
                            b1 = int(input("Enter second decimal number:"))
                            if (b1>255) or (b1<0): #comparing if the second number is more than 255 or less than 0
                                print("\n⚠️ERROR!!!Please enter number between 0 to 255 \n")
                                continue
                                #shows an error message and goes back to while loop and asks for input again
                            if (a1+b1 > 255) or (a1+b1 <0): #comparing if the sum of two number is more than 255 or less than 0
                                print("⚠ERROR!!!Please enter the numbers whose sum is between 0 to 255 \n")
                                continue
                                #shows an error message and goes back to while loop and asks for input again
                            else:
                                return a1, b1,addition_type
                        except:
                            print("\n⚠️Error!! Please enter the number as 25 or any integer number: \nNumber can't be negative or more than 255 \nNumber can't be in alphabets.""")
                            print("There can not be any space between the numbers.\n")
                            continue
                            #Exception if string data type is passed
                        else:
                            break
                            #breaks the while loop if all the inputs are valid
                except:
                    print("\n⚠️Error!! Please enter the number as 25 or any integer number: \nNumber can't be negative or more than 255 \nNumber can't be in alphabets.")
                    print("There can not be any space between the numbers.\n")
                    continue
                    #Exception if string data type is passed
                else:
                    break
                    #breaks the while loop if all the inputs are valid
        else:
             print("⚠️Error!! Please enter the b or B for binary calculation and d or D for decimal calculation.")
             status = 'available'
            #Goes back to the first while loop and ask the user again to enter addition choice
  


