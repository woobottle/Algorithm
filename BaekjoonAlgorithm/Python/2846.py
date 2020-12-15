import sys

n = int(input())
m = list(map(int, sys.stdin.readline().split()))

maxV = 0
tempV = 0

for i in range(len(m)-1) :
  subV = m[i+1] - m[i]
  if(subV > 0) :
    tempV += subV
    if maxV < tempV :
      maxV = tempV
    i += 1
  else :
    tempV = 0

print(maxV)