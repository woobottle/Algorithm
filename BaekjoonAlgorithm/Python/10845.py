from collections import deque
import sys 

queue = deque()
n = int(sys.stdin.readline().strip())

for i in range(n) :
  l = list(sys.stdin.readline().strip().split())
  if(l[0] == "push") :
    queue.append(l[1])
  elif(l[0] == "pop") :
    if queue : print(queue.popleft())
    else : print(-1)
  elif(l[0] == "size") :
    print(len(queue))
  elif(l[0] == "empty") :
    if queue : print(0)
    else : print(1)
  elif(l[0] == "front") :
    if queue : print(queue[0])
    else : print(-1)
  elif(l[0] == "back") :
    if queue : print(queue[-1])
    else : print(-1)
