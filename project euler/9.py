# Special Pythagorean triplet
# https://projecteuler.net/problem=9

import math

def special_pythagorean_triplet():
  target_sum = 1000
  
  for a in range(target_sum // 2 - 1, -1, -1):
    dividend = target_sum * ((target_sum // 2) - a)
    divisor = target_sum - a
    if dividend % divisor == 0:
      b = dividend // divisor
      c = int(math.sqrt(a**2 + b**2))
      if (a + b + c) == target_sum:
        print(a, b, c)
        return a * b * c
    
result = special_pythagorean_triplet()
print(result)
