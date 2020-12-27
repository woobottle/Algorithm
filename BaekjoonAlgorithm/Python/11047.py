import bisect
n,k = map(int, input().split())
l = []
for _ in range(n) :
  l.append(int(input()))

count = 0
start_index = bisect.bisect(l, k)
if(start_index == 0) : start_index = len(l)
for i in range(start_index, 0, -1) :
  count += k // l[i-1]
  k %= l[i-1]

print(count)
