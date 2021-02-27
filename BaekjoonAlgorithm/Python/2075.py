n = int(input())
l = []

for _ in range(n) :
  arr = list(map(int, input().split()))
  l += arr
  l = sorted(l, reverse = True)[:n]

print(l[n-1])
