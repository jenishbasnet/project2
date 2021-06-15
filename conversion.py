from input_number import number_input

def conversion():
    a,b,num_type = number_input() #storing value returned from number_input function
    if num_type == 'b':
        first_input = a
        second_input = b
        first_number = 0
        second_number = 0
        first_list = list(str(a))
        second_list = list(str(b))
        a_list = []
        for i in range(8-len(first_list)):
            a_list.append(0) #creating a list with element 0
        a_list.extend(first_list)
        #extending a_list with the input list
        
        for i in range(len(a_list)):
            a_list[i] = int(a_list[i])
        #storing list as in integer data type
        position_a =0
        while first_input>0:
            rem = first_input % 10
            first_number += rem*(2**position_a)
            position_a += 1
            first_input = first_input//10       
            #Converting binary to decimal
        b_list = []
        for i in range(8-len(second_list)):
            b_list.append(0) #creating a list with element 0 
        b_list.extend(second_list)
        #extending b_list with the second input list

        for i in range(len(b_list)):
            b_list[i] = int(b_list[i])
        #storing list as in integer data type
        position_b =0
        while second_input>0:
            rem = second_input % 10
            second_number += rem*(2**position_b)
            position_b += 1
            second_input = second_input//10
            #converting binary to decimal
        return first_number,second_number,a_list, b_list
        
    elif num_type == 'd':
        first_number = a
        second_number = b
        a_list = [0] * 8
        b_list = [0] * 8

        c = first_number
        for i in range(7,-1,-1):
            if (c>0):
                quot = c//2
                rem = c%2
                c = quot
                a_list[i] = rem
            else:
                a_list[i] = 0
        #converting decimal to binary 

        d = second_number        
        for i in range(7,-1,-1):
            if (d>0):
                quot = d//2
                rem = d%2
                d = quot
                b_list[i] = rem
            else:
                b_list[i] = 0
        #converting decimal to binary
        return first_number,second_number,a_list, b_list
    
    


