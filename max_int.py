numt_int = int()
max_int = int()
stop = False
while stop != True : 
    num_int = int(input("Input a number: "))    # Do not change this line
    if num_int > max_int : 
        max_int = num_int
    elif num_int < 0 : 
        stop = True
print("The maximum is", max_int)    # Do not change this line
