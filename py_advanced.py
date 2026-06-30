#### Task 1 ####
i = 1
factorial = 1
num = int(input("Enter a number: "))
while i <= num:
    factorial =  factorial * i
    i = i + 1
print(factorial)

#### Task 2 ####
num = ""
i = 1
factorial = 1
while num != "stop":
    num = input("Enter a number: ")
    try:
        num = int(num)
        while i <= num:
            factorial = factorial * i
            i = i + 1
        print(factorial)
    except:
        if num == "stop":
            break
        num = input("Enter a number: ")

#### Task 3 ####
luddy_courses = ["INFO-I 101", "INFO-I 210", "INFO-I 308", "INFO-I 360", "INFO-I -453","STAT-S 350","CSCI-C 211","CSCI-B 365", "CSCI-C 311","CSCI-C 343","CSCI-B 405","ENGR-E 313", "LLLC-Y 101"]
info_courses = []
cs_courses = []
other_courses = []
for course in luddy_courses:
    if course[0] == "I":
        info_courses.append(course)
    elif course[0] == "C":
        cs_courses.append(course)
    else:
        other_courses.append(course)
print(info_courses, "contains", len(info_courses), "info courses")
print(cs_courses, "contains", len(cs_courses), "cs courses")
print(other_courses, "contains", len(other_courses), "other courses")