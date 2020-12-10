import sys

n =  int(sys.stdin.readline())

a = 1
b = 0

while n >= 0 :
  if(a > n) :
    a = 1
  n -= a
  a += 1
  b += 1


print(b-1)