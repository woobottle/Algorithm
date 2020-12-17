import sys
n = int(input())

b = list(map(int, sys.stdin.readline().split()))
l = []
for i in range(len(b)) :
  if(i == 0) : 
    l.append(b[i])
  else :
    l.append(b[i]*(i+1) - b[i-1] * i)
print("".join(str(i) + " " for i in l))