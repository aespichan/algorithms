# Even Fibonacci numbers
# https://projecteuler.net/problem=2

def sum_even_fibonacci_numbers(limit):
  first = second = 1
  result = 0
  while second <= limit:
    if second % 2 == 0:
      result += second
    first, second = second, first + second

  return result

result = sum_even_fibonacci_numbers(4000000)
print(result)
