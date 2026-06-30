my_number = 1
print(my_number + 100)
print(my_number- -100)
print(my_number*101)
print(101/my_number) #division in python always creates a float
####################################################################
credits_to_graduate = 120
current_credits = 30
years_til_graduation = credits_to_graduate // current_credits #floor div gets rid of float
print("I have", years_til_graduation, "years until I graduate") #can't add int to str
####################################################################
info_courses = ["INFO-I 210", "INFO-I 211", "INFO-I 308", "INFO-I 422"]
course_digits =[]
i0 = info_courses[0][7:10]
i1 = info_courses[1][7:10]
i2 = info_courses[2][7:10]
i3 = info_courses[3][-3:]
course_digits.append(i0)
course_digits.append(i1)
course_digits.append(i2)
course_digits.append(i3)
print(course_digits)

