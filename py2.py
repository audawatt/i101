#day = "thursday"
# print(len("katie"))
# print(len("katie chase logan"))
# print(len(day))
# print("CHasE"[0])

l = "( ͡° ͜ʖ ͡°)"
i = "informatics!"
info = "INFO-I 101"

# print(i[0])
# print(i[4])
# print(i[11])

####################################################

#find last term
# print(i[11])
# print(i[len(i)-1])
# print(i[-1])

####################################################

#slicing
#start, stop, step 
#[2:8:2] means start @ second index, end @ eigth index and skip every other index

# print(info[0:4:1])
# print(info[0:4])
# print(info[2:8:2])

####################################################

#lists

list =["hello", "world", 3.14159, 48]
prof = ["logan", "chase", "katie"]

# print(prof[2], l)

#updating value
# print(prof)
# prof[0] = "ashley"
# print(prof)

# #add to list
# prof.append("ashley")
# print(prof)

# #remove from list
# prof.remove("katie")
# print(prof)

heroes = ["Joker", "Penguin", "Riddler", "Clayface"]
# print(heroes)
# heroes[0] = "Calculator"
# print(heroes)
# heroes.append("Half-Face")
# print(heroes)
# heroes.remove("Penguin")
# print(heroes)

####################################################

#boolean
#true/false questions

# print(heroes[0] == "Batman")

####################################################

#if/elif/else

# if len(heroes) == 3:
#     print("There's", len(heroes), " villains at large")
#     print(heroes)
# elif len(heroes) > 3:
#     print(heroes)
#     print("There's too many villains at large! Terminating a villain..." )
#     heroes.remove("Penguin")
#     print(heroes)
# else:
#     print(heroes)
#     print("There's not enough villains at large. Releasing a villain...")
#     heroes.append("Poison Ivy")
#     print(heroes)

name = "AnaUdawatte"

if len(name) <= 20:
    print("less than 20 characters!")
elif len(name) > 20 and len(name) < 30:
    print("between 20 and 30 characters")
else:
    print("greater than or equal to 30 characters")
