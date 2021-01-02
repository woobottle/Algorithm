import sys
from collections import deque

left_deque = deque()
right_deque = deque()
s = sys.stdin.readline().rstrip()

for i in s :
  left_deque.append(i)

n = int(input())
for i in range(n) :
  t = list(sys.stdin.readline().strip().split())
  if(t[0] == 'P') :
    left_deque.append(t[1])
  elif(t[0] == 'L') :
    if not left_deque : continue
    temp = left_deque.pop()
    right_deque.appendleft(temp)
  elif(t[0] == 'D') :
    if not right_deque : continue
    temp = right_deque.popleft()
    left_deque.append(temp)
  elif(t[0] == 'B') :
    if not left_deque : continue
    left_deque.pop()

print(''.join(left_deque + right_deque))
