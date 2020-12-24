n, x, k = map(int, input().split())
l = [0] * (n+1)
l[x] = 1
for i in range(k) :
  a,b = map(int, input().split())
  l[a], l[b] = l[b], l[a]

print(l.index(1))