from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(x,y) :
  count = 1
  q = deque()
  q.append([x, y])
  while q :
    c_x, c_y = q.popleft()
    for i in range(4) :
      n_x = c_x + dx[i]
      n_y = c_y + dy[i]
      if(0 <= n_x < n and 0 <= n_y < m and visited[n_x][n_y] == False and arr[n_x][n_y] == 1) :
        visited[n_x][n_y] = True
        q.append([n_x, n_y])
        count += 1
  return count 

n, m, k = map(int, input().split())
arr = [[0] * (m) for _ in range(n)]
visited = [[False] * (m) for _ in range(n)]
for _ in range(k) :
  r,c = map(int, input().split())
  arr[r-1][c-1] = 1

ans = 0
for i in range(n) :
  for j in range(m) :
    if(arr[i][j] == 1 and visited[i][j] == False) :
      visited[i][j] = True
      ans = max(ans, bfs(i,j))

print(ans)
