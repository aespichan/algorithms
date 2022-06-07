# Smallest multiple
# https://projecteuler.net/problem=5

def find_smallest_multiple(limit):
  factors = []
  multiple = 1
  for num in range(2, limit + 1):
    for factor in factors:
      if num % factor == 0:
        num //= factor
    if num > 1:
      factors.append(num)
    multiple *= num
  
  return multiple
  
result = find_smallest_multiple(20)
print(result)
