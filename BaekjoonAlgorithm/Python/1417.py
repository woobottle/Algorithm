n = int(input())
l = []
for i in range(n) :
  l.append(int(input()))

print(max(l) - l[0])