import sys 

n,m = map(int, sys.stdin.readline().strip().split(" "))
l = list(map(int, sys.stdin.readline().strip().split(" ")))
maxValue = 0

for i in range(0, len(l) - 2) :
  for j in range(i+1, len(l) - 1) :
    for k in range(j+1, len(l)) :
      sumValue = l[i] + l[j] + l[k]
      if(maxValue < sumValue <= m):
        maxValue = sumValue

print(maxValue)
