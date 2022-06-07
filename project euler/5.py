# Smallest multiple
# https://projecteuler.net/problem=5

def find_smallest_multiple(limit):
  numbers = [n for n in range(2, limit + 1)]
  multiple = 1
  for i in range(len(numbers)):
    num = numbers[i]
    multiple *= num
    for j in range(i + 1, len(numbers)):
      if numbers[j] % num == 0:
        numbers[j] //= num
  
  return multiple
  
result = find_smallest_multiple(20)
print(result)
