n = int(input())
l = list(map(int,input().split()))
d = [999999] * (n + 1) 

for i in range(1, n+1) :
  for j in range(1, i+1) :
    d[i] = min(d[i], d[i-j] + l[j-1], l[i-1])

print(d[n])