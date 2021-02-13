import sys
INF = 10*(1e7)
n,m = map(int, sys.stdin.readline().strip().split())
l = [[INF] * (n + 1) for _ in range(n+1)]
visited = [[False] * (n + 1) for _ in range(n+1)]
for _ in range(m) :
  a, b = map(int, sys.stdin.readline().strip().split())
  l[a][b] = 1
  l[b][a] = 1

for i in range(1,n + 1) : # 경유
  for j in range(1,n + 1) : # 시작
    for k in range(1,n + 1) : # 끝
      if(j == k) : continue
      l[j][k] = min(l[j][k], l[j][i] + l[i][k])

for i in range(n+1) :
  for j in range(n+1) :
    if(l[i][j] == INF) : l[i][j] = 0

arr = []
for i in l :
  arr.append(sum(i))

min_value = min(arr[1:])
for i in range(len(arr)) :
  if(arr[i] == min_value) : 
    print(i)
    exit()