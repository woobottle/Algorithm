import sys
t = int(sys.stdin.readline().strip())
for _ in range(t) :
  k = int(sys.stdin.readline().strip())
  l = sorted(list(map(int, sys.stdin.readline().strip().split())))
  print(l)