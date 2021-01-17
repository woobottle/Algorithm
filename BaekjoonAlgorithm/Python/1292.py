a,b = map(int, input().split())

l = []

for i in range(0,1000) :
  for j in range(i) :
    l.append(i)

print(sum(l[a-1:b]))