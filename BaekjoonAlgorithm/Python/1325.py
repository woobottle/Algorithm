from collections import deque

# def bfs(v, length, l) :
#   answer = [0] * (length+1)
#   visited = [False] * (length+1)
#   q = deque([v])
#   answer[v] = 1
#   visited[v] = True
#   while q :
#     node = q.popleft()
#     for dot in l[node] :
#       if not visited[dot] :
#         q.append(dot)
#         visited[dot] = True
#         answer[dot] = 1
#   return answer

def dfs(v, start, l) :
  answer[start] += 1
  l[v] = True
  for dot in arr[v] :
    if not l[dot] :
      l[dot] = True
      dfs(dot, start, l)

n,m = map(int, input().split())
arr = [[] for _ in range(n+1)]
answer = [0] * (n+1)

for _ in range(m) :
  a,b = map(int, input().split())
  arr[b].append(a)
  
for i in range(1, (n+1)) :
  visited = [False] * (n+1)
  dfs(i, i, visited)
  # answer[i] = sum(bfs(i, n, arr))

# print(answer)
max_value = max(answer)
for i in range(len(answer)) :
  if(max_value == answer[i]) : print(i, end=" ")
