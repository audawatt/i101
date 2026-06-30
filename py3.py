# name = input("What's your name?")
# print("Hi" + " " + name + "!")

############################################
# birth_year = input("enter your birth year:")
# age = 2024 - int(birth_year)
# print("You are", age,"years old.")

# birth_year = input("enter your year of birth:")
# try:
#     print(2024 - int(birth_year))
# except:
#     print(birth_year, "is not a year")
############################################
#while loops loop until a condition is satisfied; then it runs

# current_time = int(input("What is the time?"))
# while current_time < 11:
#     print("Procrastinate!")
#     current_time = int(input("What time is it?"))
# print("Do your homework")

# num = int(input("Enter a number:"))
# try:
#     while num > 10:
#         print(num, "is greater than 10")
#         break
# except:
#     input("Enter a number:")

#number guessing game

import random
answer = random.randint(1,100)
guess = 0

while guess < 10:
    user = input("Enter a number: ")
    try:
        user = int(user)
        if user > answer:
            print("Guess too high")
            guess += 1
        elif user < answer:
            print("Guess too low")
            guess += 1
        else:
            print("Correct")
            print("You answered in", guess, "guesses")
            break
    except:
        user = input("Enter a number: ")
############################################
# #choosing a random choice from a list
# animals = ["dog", "cat", "fish", "bird"]
# print(random.choice(animals))
############################################
# chores = ["homework", "laundry", "dishes", "grocery", "vaccuming", "pay rent"]
# print("chores to do:", chores)
# while len(chores) != 0:
#     current_chore = random.choice(chores)
#     print("current chore:", current_chore)
#     chores.remove(current_chore)
#     print("remaining chore/s:", chores)
    







