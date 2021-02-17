from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def check(l) :
  for i in range(3) :
    for j in range(3) :
      if(i == 2 and j == 2) : continue
      if(l[i][j] == ((j+1) + ((i) * 3))) : 
        continue
      else : 
        return False
  return True

def graph_check(x, y, l) :
  q = deque()
  q.append([x,y])
  while q :
    c_x, c_y = q.popleft()
    for i in range(4) :
      n_x = c_x + dx[i]
      n_y = c_y + dy[i]
      if(0<=n_x<3 and 0<=n_y<3) :
        q.append([n_x, n_y])

arr = []
for _ in range(3) : 
  arr.append(list(map(int, input().split())))

count = 0

if not check(arr) :
  for i in range(3) :
    for j in range(3) :
      if(arr[i][j] == 0) : 
        graph_check(i, j, arr)

if check(arr) :
  print(count)
else :
  print(-1)
