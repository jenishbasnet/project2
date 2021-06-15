def AND (a, b): #Electronic AND gate
    if a == 1 and b == 1: 
        return 1
    #returns 1 if both the variable is 1
    else: 
        return 0 
def OR (a,b): #Electronic OR gate
    if a ==1:
        return 1
    elif b == 1:
        return 1
    #returns 1 if any of the variable is 1
    else:
        return 0

def XOR (a,b): #Electronic XOR gates
    if a != b:
        return 1
    #returns 1 if both the variables are different
    else:
        return 0


    
    
