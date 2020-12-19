l = [0] * 10002
l[0] = 1
l[1] = 1

for i in range(2, 101) : 
  for j in range(i*2, 10001, i) :
    if(l[j] == 0) : l[j] = 1


m = int(input())
n = int(input())

s = []
for i in range(m, n+1) :
  if(l[i] == 0) : s.append(i)

if(len(s) == 0) : 
  print("-1")
else :
  print(sum(s))
  print(min(s))