import sys
n = int(input())

for _ in range(n) :
  t = input()
  l = list(map(int, sys.stdin.readline().split(" ")))
  print((max(l) - min(l))*2)
  