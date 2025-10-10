# print('hello world')
# print(3)
# print(3+4)
# print("Your name is", input("Your name: "))

# User types its name and returns the length of it
# name = input("Your full name: ")
# print(len(name))

# type two values and return the sum
# first_value = int(input("type first value: "))
# second_value = int(input("type second value: "))
# sum = first_value + second_value
# print(sum)
# print(type(sum))

# Challenge
FIXED_BONUS = 1000
name = input("Your name: ")
salary = float(input("Salary: "))
bonus_pct = float(input("Bonus %: "))
final_bonus = FIXED_BONUS + salary * bonus_pct
print(f"The final bonus for {name} is {final_bonus}")