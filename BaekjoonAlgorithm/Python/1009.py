import sys
n = int(sys.stdin.readline().strip())

for _ in range(n) :
  a,b = map(int, sys.stdin.readline().strip().split())
  data = pow(a,b,10)
  if(data == 0) : data = 10
  print(data)