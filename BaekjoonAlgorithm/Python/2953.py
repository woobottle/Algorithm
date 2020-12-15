import sys 

l = []
for _ in range(5) :
  l.append(sum(map(int, sys.stdin.readline().split())))

print(l.index(max(l)) + 1, max(l))

