#total attempts
import itertools
from itertools import permutations

attempts = [
  319,
  680,
  180,
  690,
  129,
  620,
  762,
  689,
  762,
  318,
  368,
  710,
  720,
  710,
  629,
  168,
  160,
  689,
  716,
  731,
  736,
  729,
  316,
  729,
  729,
  710,
  769,
  290,
  719,
  680,
  318,
  389,
  162,
  289,
  162,
  718,
  729,
  319,
  790,
  680,
  890,
  362,
  319,
  760,
  316,
  729,
  380,
  319,
  728,
  716,
]

#compiling digits
digits = set()
for attempt in attempts:
  for digit in str(attempt):
    digits.add(int(digit))

#putting every attempt in its own list
array = []
for attempt in attempts:
  ans = []
  for digit in str(attempt):
    ans.append(int(digit))
  array.append(ans)
print(array)
print(digits)


#brute force
#30109
def deriv(list, num):
  if len(list) > 3:
    return None

  num1 = list[0]
  num2 = list[1]
  num3 = list[2]

  number = [int(i) for i in str(num)]

  if number.index(num2) < number.index(num1) or number.index(
      num3) < number.index(num2):
    return False
  else:
    return True


#print(deriv([3, 1, 9], 30109))

perms = list((itertools.permutations("12367890")))
print(perms[0])
index = 0
for password in perms:
  string = ""
  for digit in password:
    string += digit
  perms[index] = int(string)
  index += 1
"""
for password in perms:
  for attempt in array:
    if deriv(attempt, password):
      1+1
"""

print(deriv(array[1], ))
