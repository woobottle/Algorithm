from itertools import combinations
import math

n = int(input())
for _ in range(n) :
  n,m = map(int, input().split())
  print(int(math.factorial(m)/(math.factorial(n)*math.factorial(m-n))))
