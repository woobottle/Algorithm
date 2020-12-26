n = int(input())
for i in range(n) :
  l = list(input().split())
  rl = []
  s = " "
  for j in l :
    rl.append(j[::-1])
  print(s.join(rl))