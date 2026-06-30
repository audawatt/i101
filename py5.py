####Binary to Decimal Conv####
#initializes required variables and length
num = "101"
sum = 0
index = len(num)
for i in range(1, index+1): #loop through the string
    if num[-i] == "1": #check whether current position is on or off
        sum = sum + (2**(i-1)) #add decimal value of position to sum
    print(sum) #print final decimal number

######################################################

print(4 in [1,2,3,4]) # returns True
print(4 in [1,2,3]) #returns False

fruit = ["apples", "bananas", "oranges", "grapes"]
print("apples" in fruit) 

######################################################

word = "hello"
for letter in word:
    if letter == "e":
        print(letter, sep = "\t", end = " ")
    else:
        print("**", end = "")
        
