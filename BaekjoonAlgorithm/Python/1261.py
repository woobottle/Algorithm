import heapq

INF = int(1e7)
m, n = map(int, input().split())
graph = []
distance = [[INF] * m for _ in range(n)]
visited = [[False] * m for _ in range(n)]

for _ in range(n) :
  graph.append(list(input()))

# 이동할수 있는 방향들
direction_x = [1, -1, 0, 0]
direction_y = [0, 0, 1, -1]

def dijkstra(x, y) :
  visited[x][y] = True
  distance[x][y] = 0
  q = []
  heapq.heappush(q, [0, x, y])
  while q :
    cost, node_x, node_y = heapq.heappop(q)
    for i in range(len(direction_x)) :
      next_x = node_x + direction_x[i] 
      next_y = node_y + direction_y[i]
      if(next_x < 0 or next_x >= n or next_y < 0 or next_y >= m) :
        continue
      if(visited[next_x][next_y] == False) :
        if(graph[next_x][next_y] == "0") : 
          visited[next_x][next_y] = True
          distance[next_x][next_y] = distance[node_x][node_y]
          heapq.heappush(q, [distance[next_x][next_y], next_x, next_y])
        else : 
          visited[next_x][next_y] = True
          if(distance[next_x][next_y] > cost + 1) :
            distance[next_x][next_y] = cost + 1
            heapq.heappush(q, [distance[next_x][next_y], next_x, next_y])
      
dijkstra(0,0)

print(distance[n-1][m-1])
