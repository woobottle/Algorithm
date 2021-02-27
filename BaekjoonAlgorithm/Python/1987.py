import sys 
dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]
answer = 1

def dfs(c_x, c_y, visited_list, cnt) :
  global answer
  for i in range(4) :
    n_x = c_x + dx[i]
    n_y = c_y + dy[i]

    if(cnt == 26) :
      return 26

    if n_x < 0 or n_y < 0 or n_x >= r or n_y >= c :
      continue
    
    # if (graph[n_x][n_y] not in visited_list) :
    #   visited_list.add(graph[n_x][n_y])
    #   dfs(n_x, n_y, visited_list, cnt + 1)
    #   visited_list.remove(graph[n_x][n_y])
    if(visited_list[ord(graph[n_x][n_y]) - 65] == False) :
      visited_list[ord(graph[n_x][n_y]) - 65] = True
      dfs(n_x, n_y, visited_list, cnt+1)
      answer = max(answer, cnt+1)
      visited_list[ord(graph[n_x][n_y]) - 65] = False

# r, c = map(int, input().split())
r, c = map(int, sys.stdin.readline().strip().split())
graph = []
# visited = set()
visited = [False] * 26

for _ in range(r) :
  graph.append(list(sys.stdin.readline().strip()))

# visited.add(graph[0][0])
visited[ord(graph[0][0]) - 65] = True
dfs(0, 0, visited, 1)
print(answer)
