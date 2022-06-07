# Largest palindrome product
# https://projecteuler.net/problem=4

def is_product_of_two_numbers_with_required_digits(num, smallest_bound, biggest_bound):
  smallest_num = max(smallest_bound, (num // (biggest_bound + 1)) + 1)
  biggest_num = min(biggest_bound, num // smallest_bound)
  
  for divisor in range(biggest_num, smallest_num - 1, -1):
    if num % divisor == 0:
      return True
  return False

def is_palindrome(num):
  str_num = str(num)
  i = 0
  j = len(str_num) - 1
  
  while i <= j:
    if str_num[i] != str_num[j]:
      return False
    i += 1
    j -= 1
  return True

def find_largest_palindrome_product(digits = 2):
  smallest_num = int("1" + "0" * (digits - 1))
  biggest_num = int("9" * digits)
  
  smallest_prod = smallest_num * smallest_num
  biggest_prod = biggest_num * biggest_num
  
  for num in range(biggest_prod, smallest_prod + 1, -1):
    if is_palindrome(num) and is_product_of_two_numbers_with_required_digits(num, smallest_num, biggest_num):
      return num
    
  return -1

palindrome = find_largest_palindrome_product(3)
print(palindrome)
