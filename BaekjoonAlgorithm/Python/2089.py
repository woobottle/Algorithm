import math
n = int(input())
s = ""

if(n == 0) : print(0)
else :
  while n != 0 :
    s += str(abs(n%-2))
    n = math.ceil(n/-2)

  print(s[::-1])