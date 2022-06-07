# Multiples of 3 or 5
# https://projecteuler.net/problem=1

def sum_multiples_3_or_5(limit = 1000):
  result = 0
  for num in range(limit):
    if num % 3 == 0 or num % 5 == 0:
      result += num
  return result

result = sum_multiples_3_or_5(1000)
print(result)
