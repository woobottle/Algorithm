from math import gcd
from itertools import combinations

n = int(input())
for i in range(n) :
  l = list(map(int, input().split()))
  l = l[1:]
  sum = 0
  for i in combinations(l, 2) :
    sum += gcd(i[0], i[1])
  print(sum)