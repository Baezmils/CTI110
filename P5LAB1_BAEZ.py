# CTI 110
# P5LAB2 - Functions
# Baezs
# 11/2/23

# First, print a table of squares

def main():
  print("P5T2 - Squares")
  print("number\tnumber squared")
  # range(1,11) gives numbers 1-10
  for num in range(1, 11):
    num_squared = square(num)
    print_row(num, num_squared)
    
# square() is a value-returning function   
def square(number):
  """input: a number
  output: the square of the number"""""
  square = number * number
  return square

# print_row() is a void function
def print_row(num, num_squared):
  print(num, "\t\t", num_squared)

# START PROGRAM
if __name__ == "__main__":
  main()


