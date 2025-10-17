# USING DEBUG FROM VS CODE
# print("Class 03")
# x = 5
# print("Debug 01")

# print("Debug 02")
# x = 6
# print("Debug 03")

# print("Debug 04")

# # if
# x = 2

# if x > 5:
#     print("x is higher than 5")
# elif x > 2:
#     print("x is higher than 2")
# else:
#     print("x is 2 or smaller")
#     print(f"x is {x}")

# check if value is not negative
# amount = 30
# price = 20
# if amount >= 0 and price >= 0:
#     print("valid values")
# else:
#     print("invalid value")

# for
# numbers = [10, 20, 30, 40, 0, 50,]
# for i in numbers:
#     print(i)

# names = ["Igor", "Lara", "Luciano", "Rafael", "Marco",]
# for name in names:
#     print(name)

# # count words in text
# text = "This is the third class in the course course course"
# words = text.split(" ")
# dictionary = {}
# for item in words:
#     if dictionary.get(item) is None:
#         dictionary[item] = 1
#     else:
#         dictionary[item] += 1


# while
# import time
# condition = True
# i = 1
# while condition:
#     print(f"Execution number: {i}")
#     i += 1
#     time.sleep(1)
#     if i == 4:
#         condition = False

# Challenge
FIXED_BONUS = 1000

valid_name = False
while valid_name is False:
    name = "Igor"
    if name.isdigit():
        print("Name is number.")
    elif len(name.strip()) == 0:
        print("No name was passed.")
    else:
        valid_name = True

valid_salary = False
while valid_salary is False:
    salary = 4000
    try:
        salary = float(salary)
        valid_salary = True
    except Exception:
        print("Salary is not a valid number")

valid_bonus = False
while valid_bonus is False:
    bonus_pct = 0.5
    try:
        bonus_pct = float(bonus_pct)
        valid_bonus = True
    except Exception:
        print("Bonus is not a valid number")

final_bonus = FIXED_BONUS + (salary * bonus_pct)
print(f"The final bonus for {name} is {final_bonus}")
