from itertools import combinations
from itertools import permutations

curr = 100
n = int(input())
m = int(input())
arr = [1] * 10
if m != 0 :
  for i in list(map(int, input().split())) :
    arr[i] = 0
count = 0

s = []
for i in range(len(arr)) : 
  if(arr[i] != 0) : s.append(i)

arr = list(permutations(s, len(str(n))))
