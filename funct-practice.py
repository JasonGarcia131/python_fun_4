# 1----------Both functions below do the same thing-------------
# def max_num(a,b,c):
#     print(max(a,b,c))
# max_num(1,2,3)

def max_num(*nums):
    print(max(nums))
max_num(1,2,3)

# 2----------Both functions below do the same thing-------------

# def multi_list(*my_list):
#     i=1
#     for item in my_list:
#         i=i*item
#     return i
# print(multi_list(1,2,3,4))

import math
def multi_list(*my_list):
    return math.prod(my_list)
print(multi_list(1,2,3,4))

# 3---------------------------------------
def rev_string(my_str):
    print(my_str[::-1])
rev_string('hello')

# 4----------------------------------------
def num_within(a,b,c):
    if(a > b and a <= c):
        return True
    else:
        return False
print(num_within(3,2,4))
print(num_within(3,1,3))
print(num_within(2,5,10))

def pascal(n):
   for i in range(n+1):
      for j in range(n-i):
         print(' ', end='')

      C = 1
      for j in range(1, i+1):
         print(C, ' ', sep='', end='')
         C = C * (i - j) // j
      print()

n = 5
pascal(n)