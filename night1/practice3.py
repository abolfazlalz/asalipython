# repeat for 3 times
# repeat while condition is true

# 3! = 1 * 2 * 3 = 6

num = int(input("Enter number: "))

fact = 1

for i in range(num):
    fact = fact * (i + 1)

print(fact)
