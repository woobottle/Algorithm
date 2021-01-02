import sys
from collections import deque

dequeD = deque()
n = int(input())
for i in range(n) :
  t = list(sys.stdin.readline().strip().split())
  if(t[0] == "push_front") :
    dequeD.appendleft(t[1])
  elif(t[0] == "push_back") :
    dequeD.append(t[1])
  elif(t[0] == "pop_front"):
    if dequeD :
      temp = dequeD.popleft()
      print(temp)
    else : print(-1)
  elif(t[0] == "pop_back"):
    if dequeD :
      temp = dequeD.pop()
      print(temp)
    else : print(-1)
  elif(t[0] == "size"):
    print(len(dequeD))
  elif(t[0] == "empty"):
    if dequeD : print(0)
    else : print(1)
  elif(t[0] == "front"):
    if dequeD : print(dequeD[0])
    else : print(-1)
  elif(t[0] == "back"):
    if dequeD : print(dequeD[-1])
    else : print(-1)
  
