import sys

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]
rl = sys.stdin.readline

def dfs(x, y, m, n):
  stack = []
  if(visited[x][y] == False) :
    visited[x][y] = True
    stack.append([x,y])
  while(stack) :
    [node_x, node_y] = stack.pop()
    for i in range(4) :
      temp_x = node_x + dx[i]
      temp_y = node_y + dy[i]
      if(0 <= temp_x < m and 0 <= temp_y < n) :
        if(visited[temp_x][temp_y] == False and graph[temp_x][temp_y] == 1) :
          visited[temp_x][temp_y] = True
          stack.append([temp_x, temp_y])

T = int(rl().strip())
for _ in range(T) :
  M, N, K = map(int, rl().strip().split())
  graph = [[0] * (M) for _ in range(N)]
  visited = [[False] * (M) for _ in range(N)]
  count = 0
  for _ in range(K) :
    y, x = map(int, rl().strip().split())
    graph[x][y] = 1
  for i in range(N) :
    for j in range(M) :
      if(visited[i][j] == False and graph[i][j] == 1) :
        dfs(i, j, N, M)
        count += 1
  print(count)
