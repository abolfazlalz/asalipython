# array in python
# list of names
# list of colors
# list of task

names = ["Fatima", "Armin"]
numbers = [12, 10, 24]
any_types = ["Fatima", 12, 3.14]

# append: یک مقدار اضافه میکند.
# remove: یک مقدار حذف میکند (مقداری که بهش میدی)

names.append("Arian")
names.remove("Armin")
print(names)
# Output: ["Fatima", "Arian"]

# array in all programming language starts with 0/zero
# index یا اندیس

# ["Fatima" => 0, "Arian" => 1]

print(names[0])
# OUTPUT: Fatima

# Some other methods
# pop: یک مقدار را با استفاده از اندیس پاک میکند
names.pop(1)
print(names)
# OUTPUT: ['Fatima']

# Extend: add a list to other list
numbers1 = [12, 24, 48]
numbers2 = [1, 2, 3]
numbers1.extend(numbers2)
print(numbers1)
# Output: [12, 24, 48, 1, 2, 3]

# clear: clear all items
numbers.clear()
print(numbers)
# Output: []

# reverse: reverse the list معکوس کردن لیست
numbers1.reverse()
print(numbers1)
