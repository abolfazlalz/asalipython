names = []

# for: تعداد مشخصه
# while: شرط مشخص

while True:
    name = input("Enter your friend name:")
    if name == "exit":
        break
    names.append(name)

print(names)
