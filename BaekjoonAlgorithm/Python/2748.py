l = [0] * 91
l[1] = 1
for i in range(2, 91):
  l[i] = l[i-1] + l[i-2]

n = int(input())

print(l[n])
