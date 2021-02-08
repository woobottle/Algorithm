import sys 
n,m = map(int, sys.stdin.readline().strip().split())
graph = [[] for _ in range(n)]
for i in range(n) :
  l = sys.stdin.readline().strip()
  for j in l :
    graph[i].append(j)

