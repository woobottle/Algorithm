d = [0] * 1001
d[0] = 0
d[1] = 1
d[2] = 2

n = int(input())
for i in range(3, n+1) :
  d[i] = (d[i-2] + d[i-1]) % 10007

print(d[n])
