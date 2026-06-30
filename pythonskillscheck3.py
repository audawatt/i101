####Word Guessing Game####
####You certify that the below work is entirely your own without using outside resources####
#### Ana Udawatte ####
#### 10/31/24 ####

iconic_locations = ["samplegates", "showalterfountain", "indianamemorialunion", "hermanbwellslibrary", "bicentennialgrandcarillon"]
import random
sol = random.choice(iconic_locations)
count = 0
guessletter = []
answer = list("_" * len(sol))
print("your word has", len(sol), "letters")
while count < 11:
    word_index = 0
    guess = input("enter a letter: ")
    guessletter.append(guess)
    for letter in sol:
        if guess in letter:
            answer[word_index] = guess
        word_index += 1
    if guess not in sol:
        count += 1
    print("guessed letters:", guessletter) 
    print("Guesses:", count)
    print(answer)
    if guess == "stop":
        break
        
    