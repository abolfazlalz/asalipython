# factorial: 5! = 1 * 2 * 3 * 4 * 5 = 120

def fact_recursive(num):
  if num == 1:
    return 1
  return fact_recursive(num - 1) * num

def fact_loop(num):
  result = 1
  for i in range(num + 1):
    result * i
  return result

# result = fact(3)
# print(result)
# print(fact(5))
print(fact_recursive(1000))
# print(fact_loop(900))