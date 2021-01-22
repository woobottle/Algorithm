import heapq

INF = int(1e9)
n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
distance = [INF] * (n+1)

for _ in range(m) :
  start, end, cost = map(int, input().split())
  graph[start].append((end, cost))

a,b = map(int,input().split())

def dijkstra(start) :
  distance[start] = 0
  q = []
  heapq.heappush(q, [0, start])
  while q :
    cost, n = heapq.heappop(q)
    for target, weight in graph[n] :
      if distance[target] > cost + weight :
        distance[target] = cost + weight
        heapq.heappush(q, (cost+weight, target))


dijkstra(a)

print(distance[b])
