t = int(input())

for _ in range(t) :
  n = int(input())
  l = [0] * (n+1)
  for i in range(1, n+1):
    for j in range(i, n+1, i) :
      if(l[j] == 0) : l[j] = 1
      else : l[j] = 0
  print(sum(l))