INF = 10000001
n = int(input())
m = int(input())
graph = [[INF] * (n+1) for _ in range(n+1)]

for i in range(m) :
  a,b,c = map(int, input().split())
  if graph[a][b] == 0 :
    graph[a][b] = c
  elif graph[a][b] > c :
    graph[a][b] = c 

for i in range(1, n+1) :
  for j in range(1, n+1) :
    if i == j :
      graph[i][j] = 0 

# 기준이 되는 거쳐가는 노드 i
for i in range(1, n+1) :
  # 출발하는 노드 j
  for j in range(1, n+1) :
    # 도착하는 노드 k
    for k in range(1, n+1) :
      graph[j][k] = min(graph[j][k], graph[j][i] + graph[i][k])

for i in range(1, n+1) :
  for j in range(1, n+1) :
    if graph[i][j] == INF :
      print(0, end= " ")
    else :
      print(graph[i][j], end = " ")
  print()
