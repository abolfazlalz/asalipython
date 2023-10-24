# def sum(num1, num2):
#   return num1 + num2

sum = lambda num1, num2: num1 + num2

print(sum(5, 6))

full_name = lambda first_name, last_name: first_name + " " + last_name

pass_lesson = lambda point, money: point > 10 or money > 100

# print(full_name("Fatima", "Torkamani"))

print(pass_lesson(9, 110))
print(pass_lesson(15, 0))
print(pass_lesson(8, 0))
