# 플로이드 워셜은 사이클까지 알려준다
INF = int(1e7)
v,e = map(int, input().split())
graph = [[INF] * (v+1) for i in range(v+1)]
visited = [[False] * (v+1) for i in range(v+1)]

for _ in range(e) :
  a,b,c = map(int, input().split())
  graph[a][b] = c 

# 거치는 노드
for i in range(1, v+1) :
  # 시작 노드
  for j in range(1, v+1) :
    # 끝 노드
    for k in range(1, v+1) :
      graph[j][k] = min(graph[j][k], graph[j][i] + graph[i][k])

result = INF
for i in range(1, v+1) :
  if(graph[i][i] <= result) :
    result = graph[i][i]

if(result == INF) :
  print(-1)
else :
  print(result)
