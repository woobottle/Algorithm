n = int(input())
l = list(map(int, input().split()))
s = []
for i in l :
  s.append(l.count(i))
k = []
for i in range(len(s)) :
  j = 1
  if(s[i] == max(s)) : j = -1
  else :
    for p in s[i:-1] :
      if(p > s[i]) : j += 1
  k.append(j)

print(" ".join(str(i) for i in k))