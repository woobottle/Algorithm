l = [0] * 12
l[1] = 1
l[2] = 2
l[3] = 4

for i in range(4, 11) :
  l[i] = l[i-3] + l[i-2] + l[i-1]


t = int(input())
for _ in range(t) :
  n = int(input())
  print(l[n])