n, c = map(int, input().split())
l = []
ans = [0] * (c + 1)

for _ in range(n) :
  l.append(int(input()))

for i in l : 
  for j in range(i, c+1, i) :
    if(ans[j] == 0) : ans[j] = 1

print(sum(ans))