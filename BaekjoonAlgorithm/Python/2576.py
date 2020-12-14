l = []
for i in range(7) :
  a = int(input())
  if a % 2 == 1 :
    l.append(a)

if len(l) == 0 :
  print(-1)
else :
  print(sum(l))
  print(min(l))