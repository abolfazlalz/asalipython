scores = [12, 13, 15, 18, 20, 12, 8, 5, 4]

total = 0
length = 0

for x in scores:
    if x < 10:
        continue
    if x > 15:
        print("Pass")
    else:
        print("Failed")

    # total = total + x
    total += x
    # length = length + 1
    length += 1

# len => length => طول
avg = total / length
print(avg)
