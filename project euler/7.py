# 10001st prime
# https://projecteuler.net/problem=7

import math

def is_prime(num, primes):
  for prime in primes:
    if prime > math.sqrt(num):
      break
    if num % prime == 0:
      return False
  return True

def get_kth_prime(k):
  primes = [2]
  num = 3
  while len(primes) < k:
    if is_prime(num, primes):
      primes.append(num)
    num += 2
  
  return primes[k - 1]

prime = get_kth_prime(10001)
print(prime)
