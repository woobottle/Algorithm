# 1753번 우선순위 큐 사용
import heapq
import sys 

INF = int(1e9)
v,e = map(int, sys.stdin.readline().split())
k = int(sys.stdin.readline())
graph = [[] for _ in range(v+1)]
distance = [INF] * (v+1)

for _ in range(e) :
  u,v,w = map(int,sys.stdin.readline().split())
  graph[u].append([v,w])
  
def dijkstra(start) :
  q = []
  heapq.heappush(q, [0, start])
  distance[start] = 0
  while q :
    dist, now = heapq.heappop(q)
    if distance[now] < dist :
      continue
    for target, weight in graph[now] :
      cost = dist + weight
      if cost < distance[target] :
        distance[target] = cost
        heapq.heappush(q, (cost, target))


dijkstra(k)

for i in distance[1:] :
  print(i if i != INF else "INF")