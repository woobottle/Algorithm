n = int(input())
l = []
for _ in range(n) :
  l.append(list(map(int, input().split())))

l.sort(key = lambda i : (-i[1]))

answer = 0
done = [False] * 1001

for d,w in l :
  for i in range(d, 0, -1) :
    if not done[i] :
      done[i] = True
      answer += w
      break
print(answer)