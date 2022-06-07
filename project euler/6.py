# Sum square difference
# https://projecteuler.net/problem=6

def sum_square_difference(n):
  sum_of_squares = (n * (n + 1) * (2*n + 1)) // 6
  square_of_sum = ((n * (n + 1)) // 2) ** 2
  
  return square_of_sum - sum_of_squares

result = sum_square_difference(100)
print(result)
