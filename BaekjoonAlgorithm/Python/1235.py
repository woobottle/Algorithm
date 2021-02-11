n = int(input())
l = [] 
for _ in range(n) :
  l.append(input())

ans = 0

for i in range(1, len(l[0])) :
  s = set()
  for j in range(n) :
    s.add(l[j][-i:])
  if(len(s) == n) : 
    ans = i
    break

if ans == 0 :
  ans = len(l[0])
print(ans)
