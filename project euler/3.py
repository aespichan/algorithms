# Largest prime factor
# https://projecteuler.net/problem=3

import math

def is_prime(num):
  if num % 2 == 0:
    return False
  for n in range(3, int(math.sqrt(num)) + 1, 2):
    if num % n == 0:
      return False
  return True

def get_largest_prime_factor(target):
  middle = (target // 2) + 1
  
  for divisor in range(2, middle):
    if target % divisor == 0:
      num = target // divisor
      if is_prime(num):
        return num
  
  return -1
  
factor = get_largest_prime_factor(600851475143)
print(factor)
