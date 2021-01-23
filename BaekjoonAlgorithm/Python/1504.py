import heapq

INF = int(1e7)
n,e = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(e) :
  a,b,c = map(int, input().split())
  graph[a].append([b,c])
  graph[b].append([a,c])

def dijkstra(start) :
  distance = [INF] * (n+1)
  distance[start] = 0
  q = []
  heapq.heappush(q, [0, start])
  while q :
    cost, node = heapq.heappop(q)
    for target, weight in graph[node] :
      if distance[target] > cost + weight :
        distance[target] = cost + weight
        heapq.heappush(q, [cost + weight, target])
  return distance 

v1,v2 = map(int, input().split())

answer1 = dijkstra(1)[v1] + dijkstra(v1)[v2] + dijkstra(v2)[n]
answer2 = dijkstra(1)[v2] + dijkstra(v2)[v1] + dijkstra(v1)[n]

if min(answer1, answer2) < INF :
  print(min(answer1, answer2))
else :
  print(-1)