# # user_input=input("Please enter a compliment: ")
# # user_input=user_input.split() #turn input into string
# # print(user_input)
# # #print(user_input[3]) #print 3rd index
# # user_input[3] = "beautiful"
# # print(user_input) #replace 3rd index w/ beautiful

###################################################################
# #for loop
# # for word in ['info', 'is', 'cool']:
# #     print(word)
###################################################################
# #compliment generator
# import random
# current_index = 0
# user_input = input('enter a compliment: ')
# user_input = user_input.split()
# for word in user_input:
#     if word == "adj":
#         adjective = random.choice(['smart', 'cool', 'funny', 'nice', 'pretty'])
#         user_input[current_index] = adjective
#     current_index += 1
# user_input =  " ".join(user_input) #add list to string
# print(user_input)

# #another way to add list items to string
# # string = ""
# # for word in user_input:
# #     string += word + " "
# # print(string)
###################################################################
user_input = input('enter a compliment: ')
user_input =  user_input.split()
user_len =  len(user_input)
for user_ind in range(user_len):
    print(str(user_ind)+ " " + user_input[user_ind])

