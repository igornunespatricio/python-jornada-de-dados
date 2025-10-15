# OPERATIONS

name = "Igor_Nunes"

upper_name = name.upper()
print(upper_name)

lower_name = name.lower()
print(lower_name)

split_name = name.split("_")
print(split_name)

full_name = name + "_Patricio"
print(full_name)

print(True or False)

# user inputs two integers and integer division
# number_1 = int(input("Type first number: "))
# number_2 = int(input("Type second number: "))
# division = number_1 // number_2
# print(division)

# calculate area of circle with radius as input
# import math
# radius = float(input("Type are of circle: "))
# area = math.pi * (radius ** 2)
# print(f"The area of the circle with radius {radius} is {area: .2f}")

# user input a date in format dd/mm/aaaa and print day, month and year separately
# user_date = input("Add date with format dd/mm/aaaa: ")
# date_list = user_date.split('/')
# day = date_list[0]
# month = date_list[1]
# year = date_list[2]
# print(f"Day: {day} \nMonth: {month} \nYear: {year}")

# HANDLING ERRORS

# try:
#     number_1 = 4
#     number_2 = 'five' # to work change to a number like 3
#     int_division = number_1 // number_2
#     print(int_division)
# except TypeError as e:
#     print(e)
# else:
#     print("Worked!!!")
# finally:
#     print("Program finished")

# print(isinstance(full_name, str))
# print(isinstance(3, int))

# var = input("Type a number: ")
# try:
#     var = int(var)
# except ValueError as e:
#     pass

# if isinstance(var, int):
#     print("Variable is integer")
# else:
#     print("Variable is not integer")

# Challenge
FIXED_BONUS = 1000

name = input("Your name: ")
if name.isdigit():
    print("Name is number.")
    exit(0)
elif len(name.strip()) == 0:
    print("No name was passed.")
    exit(0)

salary = input("Salary: ")
try:
    salary = float(salary)
except Exception as e:
    print(e)
    exit(0)

bonus_pct = input("Bonus %: ")
try:
    bonus_pct = float(bonus_pct)
except Exception as e:
    print(e)
    exit(0)

final_bonus = FIXED_BONUS + (salary * bonus_pct)
print(f"The final bonus for {name} is {final_bonus}")
