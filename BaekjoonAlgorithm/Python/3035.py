import sys

r, c, zr, zc = map(int, sys.stdin.readline().strip().split())
l = []
for _ in range(r) :
  l.append(list(sys.stdin.readline().strip()))

for i in range(r) :
  for k in range(zr) :
    a = ""
    for j in range(c) :
      for m in range(zc) :
        a += l[i][j]
    print(a)