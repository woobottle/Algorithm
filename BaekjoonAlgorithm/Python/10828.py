import sys 

n = int(input())
l = []

for i in range(n) :
  t = list(sys.stdin.readline().strip().split())
  if(t[0] == "push") :
    l.append(t[1])
  elif(t[0] == "pop") :
    if l : print(l.pop())
    else : print(-1)
  elif(t[0] == "size"):
    print(len(l))
  elif(t[0] == "empty"):
    if l : print(0)
    else : print(1)
  elif(t[0] == "top"):
    if l : print(l[-1])
    else : print(-1)
