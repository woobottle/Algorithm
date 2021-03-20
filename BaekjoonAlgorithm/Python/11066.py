import sys
import heapq

t = int(sys.stdin.readline().strip())

for _ in range(t) :
  k = int(sys.stdin.readline().strip())
  l = sorted(list(map(int, sys.stdin.readline().strip().split())), reverse=True)
  answer = 0
  while len(l) != 2 :
    first = l.pop()
    second = l.pop()
    temp = first + second
    answer += temp
    l.insert(0, temp)
  answer += sum(l)
  print(answer)