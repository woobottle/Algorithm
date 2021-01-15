n = int(input())

d = [0] * 100001
d[1] = 1
d[2] = 1
d[3] = 2
d[4] = 3

for i in range(5, 100001) :
  d[i] = (d[i-3] + d[i-2] + d[i-1] - 2) % 1000000009

for i in range(n) :
  t = int(input())
  print(d[t])
  