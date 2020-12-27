n = int(input())
l = sorted(list(map(int, input().split())))

count = 0
for i in range(len(l)) :
  count += l[i] * (len(l) - i)

print(count)
