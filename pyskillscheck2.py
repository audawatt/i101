print (" Welcome to the Simple Calculator !")

while True: #loops until input is satisfactory
    num1 = (input(" Enter the first number : ")) #obtain input 1
    try: #checks if input is satisfactory
        num1 = int(num1) #checks if input is int
        break #if it is, breaks loop
    except: #if input is not int
       print("invalid statement") #then tell user invalid input
while True: #loops until input is satisfactory
    num2 = (input(" Enter the second number : ")) #obtain input 2
    try:  #checks if input is satisfactory
        num2 = int(num2) #checks if input is int
        break #if it is, breaks loop
    except: #if input is not int
        print("invalid statement") #then tell user invalid input

print (" Select an operation :") 
print ("1) Addition (+)")
print ("2) Subtraction ( -)")
print ("3) Multiplication (*)")
print ("4) Division (/)")
operation = input(" Enter the operation (1 , 2 , 3 , or 4): ") #obtain operation
if operation == "1":
    result = num1 + num2
    print (" The result of ",num1, "+",num2 ," is:", result ) #if input = 1, return input 1 + input 2
elif operation == "2":
    result = num1 - num2
    print (" The result of ",num1,"-",num2," is:", result ) #if input = 2, return input 1 - input 2
elif operation == "3":
    result = num1 * num2
    print (" The result of ",num1,"*",num2," is:",result ) #if input = 3 is chosen, return input 1 * input 2
elif operation == "4":
    if num2 == 0:
        result = num1 / num2
        print (" The result of ",num1 + "/",num2," is:",result ) #if input = 4, return input 1 / input 2
    else:
        print (" Error : Cannot divide by zero .") #unless input 2 = 0, then return invalid input
else:
    print (" Invalid operation selected .") #if input is not an operation, return invalid input
