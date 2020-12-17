t = int(input())

for i in range(t) :
  n,m = map(int, input().split())
  print((m*2 - n), m - (m*2 - n))
