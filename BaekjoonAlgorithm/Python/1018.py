import sys 
import math

answer = 1000000000

def calc(a,b) :
  num1 = 0
  num2 = 0
  for i in range(a, a+8) :
    for j in range(b, b+8) :
      if (i-a+j-b) % 2 == 0 :
        if(graph[i][j] == "W") :
          num1 += 1
      else :
        if(graph[i][j] == "B") :
          num1 += 1 
  for i in range(a, a+8):
    for j in range(b, b+8):
      if (i-a+j-b) % 2 == 0:
        if(graph[i][j] == "B"):
          num2 += 1 
      else:
        if(graph[i][j] == "W"):
          num2 += 1
  return min(num1, num2)

n,m = map(int, sys.stdin.readline().strip().split())
graph = [[] for _ in range(n)]
visited = [[False] * m for _ in range(n)]
for i in range(n) :
  l = sys.stdin.readline().strip()
  for j in l :
    graph[i].append(j)

for i in range(n-7) :
  for j in range(m-7) :
    answer = min(answer, calc(i,j))

print(answer)
