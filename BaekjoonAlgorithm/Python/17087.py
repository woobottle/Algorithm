from math import gcd
from itertools import combinations

n, s = map(int, input().split())
l = list(map(int, input().split()))
t = []

for i in l :
  t.append(abs(i - s))

maxNum = t[0]
for i in t :
  maxNum = gcd(maxNum, i)

print(maxNum)