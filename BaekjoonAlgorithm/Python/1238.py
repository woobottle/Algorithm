import heapq

INF = int(1e7)
n,m,x = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m) :
  start, end, cost = map(int, input().split())
  graph[start].append([end, cost])


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
        heapq.heappush(q, [cost+weight, target])
  return distance

distance_max = 0
for i in range(1, n+1) :
  if(i != x) :
    cost = dijkstra(x)[i] + dijkstra(i)[x] 
    if(distance_max <= cost) :
      distance_max = cost

print(distance_max)
