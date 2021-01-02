from collections import deque

n,m = list(map(int, input().split()))

queue = deque()
for i in range(1, n+1) : queue.append(i)
index = 0
answer = "<"

while queue :
  index += (m-1)
  index %= len(queue)
  temp = queue[index]
  del queue[index]
  if queue : 
    answer += f"{temp}, "
  else :
    answer += f"{temp}>"

print(answer)