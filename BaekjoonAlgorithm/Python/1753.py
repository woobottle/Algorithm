# O(V^2)
# 거리 비교하는 로직, 가장 작은 거리값 가진 애 가져오는 로직
# def 

# def daijkstra(n):


# INF = int(1e9)
# v,e = map(int, input().split())
# k = int(input())
# l = [[INF] * (v+1) for i in range(v+1)]
# visited = [0] * (v+1)

# for _ in range(e) :
#   u,v,w = map(int, input().split())
#   l[u][v] = w

INF = int(1e9)

v,e = map(int, input().split())
k = int(input())
graph = [[] for i in range(v+1)]
visited = [False] * (v+1)
distance = [INF] * (v+1)

for _ in range(e) :
  u,v,w = map(int, input().split())
  graph[u].append((v,w))

def get_smallest_node():
  min_value = INF
  index = 0
  for i in range(1, v+1) :
    if distance[i] < min_value and not visited[i] :
      min_value = distance[i]
      index = i
  return index

def dijkstra(k) :
  # 초기화
  distance[k] = 0
  visited[k] = True
  for j in graph[k] :
    distance[j[0]] = j[1]
  for i in range(v-1) :
    now = get_smallest_node()
    visited[now] = True
    # 현재 노드와 연결된 다른 노드를 확인
    for j in graph[now] :
      cost = distance[now] + j[1]
      # 현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
      if cost < distance[j[0]] :
        distance[j[0]] = cost

dijkstra(k)

# print(distance)
for i in range(1, v+2) :
  if distance[i] == INF :
    print("INF")
  else :
    print(distance[i])