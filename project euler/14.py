# Longest Collatz sequence
# https://projecteuler.net/problem=14

def collatz_sequence_size(starting_number, dp):
  has_started = False
  size = 1
  number = starting_number
  
  while not has_started or number != 1:
    has_started = True
    if number % 2 == 0:
      number //= 2
    else:
      number = 3 * number + 1
    
    if number > 1 and number <= len(dp):
      size += dp[number - 1]
      break
    
    size += 1
  
  dp.append(size)
  return size

def longest_collatz_squence(limit):
  max_size = 0
  num_max_size = None
  dp = []
  for num in range(1, limit):
    size = collatz_sequence_size(num, dp)
    if size > max_size:
      num_max_size = num
      max_size = size
  return num_max_size

result = longest_collatz_squence(1000000)
print(result)
