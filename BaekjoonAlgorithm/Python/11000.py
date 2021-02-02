import heapq
import sys 

n = int(sys.stdin.readline().strip())
l = []
for _ in range(n) :
  l.append(list(map(int, sys.stdin.readline().strip().split())))

l.sort()
q = []
heapq.heappush(q, [l[0][1], l[0][0]])
for i in range(1, len(l)) :
  # 끝나는 시간
  if(q[0][0] <= l[i][0]) :
    heapq.heappop(q)
  heapq.heappush(q, [l[i][1], l[i][0]])

print(len(q))
