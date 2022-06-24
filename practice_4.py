# Write a Python function called max_num()to find the maximum of three numbers.

import math


def max_num(a,b,c):
    max = 0
    for num in [a,b,c]:
        if num > max:
            max = num
    print(max)
max_num(105,15,27)


# Write a Python function called mult_list() to multiply all the numbers in a list.
def multi_list(*args):
    num_list = [num for num in args]
    prod_all = math.prod(num_list)
    print(prod_all)
multi_list(3,34,5,6,90,76)


# Write a Python function called rev_string() to reverse a string.
def rev_string(x):
   new_string = x[::-1]
   print(new_string)

rev_string("place lorem ipsum here")


# Write a Python function called num_within() to check whether a number falls in a given range.
    # The function accepts the number, beginning of range, and end of range (inclusive) as arguments.
    # Examples: num_within(3,2,4) returns True, num_within(3,1,3) returns True, num_within(10,2,5) returns False.
def num_within(x,a,b):
    if x >= a and x <= b:
        print("True:", x, "is in the range of",a, "and", b)
    else:
       print("False:", x, "is not in the range of",a, "and", b) 
num_within(27,8,99)

# Write a Python function called pascal() that prints out the first n rows of Pascal's triangle.
# The function accepts the number n, the number of rows to print
# Note : Pascal's triangle is an arithmetic and geometric figure first imagined by Blaise Pascal. Each number is the two numbers above it added together.
# Sample Pascal's triangle :cd python_projects

#100% copied from source. I knew i needed an array, but couldnt figure out how to utilize it.
triangle = [[1],[1,1]]
def pascal(n):
  #base case
  if n < 1:
    print("invalid number of rows")
  elif n == 1:
    print(triangle[0])
  else:
    row_number = 2
    #fill up correct number of rows in triangle
    while len(triangle) < n:
      row = []
      row_prev = triangle[row_number - 1]
      #create correct row, then add to triangle (this row will be 1 longer than row before it)
      length = len(row_prev)+1
      for i in range(length):
        #first number is 1
        if i == 0:
          row.append(1)
        #intermediate nunmbers get added from previous rows
        elif i > 0 and i < length-1:
          row.append(triangle[row_number-1][i-1]+triangle[row_number-1][i])
        #last number is 1
        else:
          row.append(1)
      triangle.append(row)
      row_number += 1

    #print triangle
    for row in triangle:
      print(row)
pascal(5)