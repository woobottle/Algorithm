l = [0] * 101
for i in range(100) :
  if(i%2 == 1) : l[i] = i

n = int(input())
for _ in range(n) :
  s = int(input())
  print(sum(l[0:s+1]))