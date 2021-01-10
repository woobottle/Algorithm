import math

length = 1000003
l = [0] * length
for i in range(2, int(length**0.5)):
  for j in range(i*2, length-1, i):
    if(l[j] == 0): l[j] = 1

n = int(input())
for _ in range(n) :
  case = int(input())
  count = 0
  for i in range(2, int(case/2) + 1):
    if(l[i] == 0 and l[case-i] == 0):
      count += 1
  print(count)

