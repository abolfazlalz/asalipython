math = int(input("Enter point in math:"))
science = int(input("Enter pint in science: "))

sum = math + science
avg = sum / 2

print(avg)

if avg > 10:
  print("Pass")
else:
  print("Fail")