# Highly divisible triangular number
# https://projecteuler.net/problem=12

import math

def get_number_of_divisors(number):
  divisors = 1 # 1 is always a divisor
  if number > 1:
    divisors += 1 # the same number is also a divisor
  
  # if there is a divisor in the left side of the square root,
  # there is a dividend which is also a divisor in the right side
  for i in range(2, int(math.sqrt(number)) + 1):
    if number % i == 0:
      divisors += 2
  
  return divisors

def get_first_triangular_number_with_n_divisors(n):
  natural_number = 1
  triangular_number = 1
  while True:
    divisors = get_number_of_divisors(triangular_number)
    if divisors >= n:
      return triangular_number
    
    natural_number += 1
    triangular_number += natural_number

triangular_number = get_first_triangular_number_with_n_divisors(500)
print(triangular_number)
