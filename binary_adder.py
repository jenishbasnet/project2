from gates import *
from conversion import conversion
def binary_adder ():
    num1,num2,a,b = conversion() #storing value returned from binary_adder function
    result = []
    carry_in = 0

    for i in range(7,-1,-1): #electronic 8 bit adder circuit
        c = a[i]
        d = b[i]
        XOR_ = XOR(c,d)
        sum_ = XOR(XOR_,carry_in)
        result.insert(0,sum_) #appening sum of two bits to the result list
        add_1 = AND(c,d)
        add_2 = AND(XOR_,carry_in)
        carry_in = OR(add_1,add_2) #carry in for another two bits
        #indexing each bit in reverse order and passing through the full adder circuit
        
    if (carry_in == 1): #to check if the sum of number is more than 255
        result.insert(0,carry_in)

    return num1,num2,a,b,result
    #returns two number as binary and decimal along with the sum of two number
    
    

