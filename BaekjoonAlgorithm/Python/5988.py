import sys

n = int(input())
for i in range(n) :
  s = list(input())
  c = int(s[-1])
  if(c%2 == 0) : print("even")
  else : print("odd")