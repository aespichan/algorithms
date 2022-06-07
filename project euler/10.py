# Summation of primes
# https://projecteuler.net/problem=10
import math

def is_prime(num, primes):
  limit = int(math.sqrt(num)) + 1
  
  for prime in primes:
    if prime > limit:
      break
    if num % prime == 0:
      return False
  return True

def summation_of_primes(limit):
  primes = [2]
  result = 2
  
  for num in range(3, limit, 2):
    if is_prime(num, primes):
      primes.append(num)
      result += num
  return result

result = summation_of_primes(2000000)
print(result)
