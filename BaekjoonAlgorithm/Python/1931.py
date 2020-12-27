n = int(input())
l = []
for _ in range(n) :
  l.append(list(map(int, input().split())))

l = sorted(l, key = lambda list: (list[1], list[0]))

count = 1
end_at = l[0][1]

for i in range(1, len(l)) :
  if l[i][0] >= end_at :
    count += 1
    end_at = l[i][1]

print(count)