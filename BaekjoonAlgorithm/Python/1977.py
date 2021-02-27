m = int(input())
n = int(input())
l = []

for i in range(m, n+1) :
  if (i**0.5 % 1) == 0 :
    l.append(i)

if len(l) != 0 :
  print(sum(l))
  print(l[0])
else :
  print(-1)
