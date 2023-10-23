# عددی از کاربر دریافت کرده و دو به توان آن عدد را محاسبه کنیم.

# Input => First number
# Input => Second number
# Result = First number ^ Second number
# n^m

# 2 ^ 4 => 1 * 2 * 2 * 2 * 2
first_number = int(input("enter first number:"))
last_number = int(input("enter second number:"))
result = 1
for i in range(last_number):
    result = result * first_number
print(result)
