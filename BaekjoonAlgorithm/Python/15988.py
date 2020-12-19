l = [0] * 1000001
l[1] = 1
l[2] = 2
l[3] = 4

for i in range(4, 1000001):
  l[i] = (l[i-3] % 1000000009 + l[i-2] %
          1000000009 + l[i-1] % 1000000009)
  
t = int(input())
for _ in range(t):
  n = int(input())
  print(l[n]%1000000009)
