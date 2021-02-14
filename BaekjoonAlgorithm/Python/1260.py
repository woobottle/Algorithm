from collections import deque 

def dfs(array, start, size, visited) :
  visited[start] = True
  dfs_arr.append(start)
  for i in range(len(array[start])) :
    if(array[start][i] == 1 and visited[i] == False) :
      dfs(array, i, size, visited)
  
  
def bfs(array, start, size):
  answer = []
  visited = [False] * (size + 1)
  q = deque()
  visited[start] = True
  q.append(start)
  while q:
    node = q.popleft()
    answer.append(node)
    for i in range(len(array[node])):
      if(visited[i] == False and array[node][i] == 1):
        q.append(i)
        visited[i] = True
  return answer

def write_ans(array) :
  print("".join(str(i) + " " for i in array))

INF = int(1e7)
n,m,v = map(int, input().split())
arr = [[INF] * (n+1) for _ in range(n+1)]
visited = [False] * (n+1)

for _ in range(m) :
  a, b = map(int, input().split())
  arr[a][b] = 1
  arr[b][a] = 1

dfs_arr = []
dfs(arr, v, n, visited)
write_ans(dfs_arr)
write_ans(bfs(arr, v, n))
